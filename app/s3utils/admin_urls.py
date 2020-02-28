from django.urls import path
from . import views

urlpatterns = [
    path('download_images/', views.download_images , name="download_images"),
    path('all_images/', views.display_all_images, name='display_images'),
]
