from django.urls import path

from .views import ChildArticleFeedView, InlineFeedBackViewSet

urlpatterns = [
    path("<path:path>", ChildArticleFeedView.as_view(), name="child_article_feed"),
    path(
        "submit_feedback", InlineFeedBackViewSet.as_view({"post": "create"}), name="submit_feedback"
    ),
    path(
        "submit_feedback",
        InlineFeedBackViewSet.as_view({"patch": "partial_update"}),
        name="update",
    ),
]
