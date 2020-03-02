from django.urls import path

from .views import (
    child_article_feed,
)

urlpatterns = [
    path('<path:path>', child_article_feed, name='child_article_feed'),

]
