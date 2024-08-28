import logging

from django.shortcuts import render, redirect
from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from wagtail.models import Site

from .models import ArticlePage, UserInlineFeedbackSurvey
from .serializers import FeedbackSerializer

from .hawk import HawkAuthentication

logger = logging.getLogger(__name__)

def submit_feedback(request):
    if request.method == "POST":
        feedback_value = request.POST.get('feedback')
        page_url = request.META.get('HTTP_REFERER', '')  # Capture the page where feedback is submitted

        if feedback_value in ['Yes', 'No']:
            UserInlineFeedbackSurvey.objects.create(page=page_url, feedback=feedback_value)

    return redirect(page_url)  # Redirect back to the page where feedback was submitted

class ChildArticleFeedView(APIView):
    authentication_classes = (HawkAuthentication,)

    def get(self, request, path, format=None):
        logger.debug(path)
        path_components = [component for component in path.split("/") if component]
        logger.debug(f"components {path_components}")

        page = (
            Site.find_for_request(request)
            .root_page.specific.route(request, path_components)
            .page.specific
        )
        logger.debug(page)

        limit_query = request.GET.get("limit", 3)
        limit = int(limit_query)
        logger.debug(f"limit: {limit}")

        recent_articles = ArticlePage.objects.live().descendant_of(page).order_by("-date")[:limit]
        site_root = Site.find_for_request(request).root_url

        count = len(recent_articles)
        logger.debug(f"found {count} articles for {path}")

        result = {"count": len(recent_articles), "articles": []}

        for recent in recent_articles:
            path = f"{site_root}{recent.url}"
            article = {
                "html_url": path,
                "title": recent.title,
                "created_at": recent.date,
            }
            result["articles"].append(article)

        return Response(result)

class InlineFeedBackViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = UserInlineFeedbackSurvey.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        location = serializer.validated_data.get("location")
        was_this_page_helpful = serializer.validated_data.get("was_this_page_helpful")
        serializer.save(was_this_page_helpful=was_this_page_helpful)
        serializer.save(location=location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        inline_feedback_choices = serializer.validated_data.get("inline_feedback_choices")
        more_detail = serializer.validated_data.get("more_detail")
        serializer.save(inline_feedback_choices=inline_feedback_choices)
        serializer.save(more_detail=more_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
