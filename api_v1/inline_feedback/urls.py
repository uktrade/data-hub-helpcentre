from django.urls import path

from .views import InlineFeedBackViewSet

urlpatterns = [
    path(
        "inline_feedback",
        InlineFeedBackViewSet.as_view({"post": "create"}),
        name="create",
    ),
    path(
        "inline_feedback/<int:pk>",
        InlineFeedBackViewSet.as_view({"patch": "partial_update"}),
        name="update",
    ),
]
