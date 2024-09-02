from django.urls import path

from .views import ChildArticleFeedView

urlpatterns = [
    path("<path:path>", ChildArticleFeedView.as_view(), name="child_article_feed"),
]