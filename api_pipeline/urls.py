from django.urls import path

from .views import UserInlineFeedbackSurveyViewSet

urlpatterns = [
    path(
        "user-inline-feedback-survey",
        UserInlineFeedbackSurveyViewSet.as_view({"get": "list"}),
        name="user-inline-feedback-survey",
    ),
]
