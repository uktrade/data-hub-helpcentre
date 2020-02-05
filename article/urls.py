from django.urls import path

from .views import (
    child_article_feed,
)

urlpatterns = [
    path('<slug:slug>', child_article_feed, name='child_article_feed'),
]
