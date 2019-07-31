from django.conf.urls import url

from .views import  (
    recent_article_feed,
)

urlpatterns = [
    url(r'^recent/$', recent_article_feed, name='recent_article_feed'),
]