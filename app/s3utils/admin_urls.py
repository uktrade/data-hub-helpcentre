from django.urls import path
from . import views

urlpatterns = [
    path('dump_images/', views.dump_images , name="dump_images"),
]
