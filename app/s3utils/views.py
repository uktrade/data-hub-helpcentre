from django.shortcuts import render

from wagtail.images.models import Image


def display_all_images(request):
    all_images = Image.objects.all()

    return render(request, 'all_images.html', {
        'images': all_images
    })
