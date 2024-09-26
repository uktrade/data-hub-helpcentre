from django.urls import include, path

urlpatterns = [
    path(
        "",
        include(
            ("api_v1.inline_feedback.urls", "api_v1"),
            namespace="inline_feedback",
        ),
    ),
]
