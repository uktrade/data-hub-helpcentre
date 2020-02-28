from django.urls import path
from . import views

urlpatterns = [
    path('all_images/', views.display_all_images, name='display_images'),
]
