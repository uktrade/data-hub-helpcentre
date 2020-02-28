import tempfile
import os
import io
import zipfile
import logging

from django.http import HttpResponse
from django.core.files.storage import get_storage_class
from django.shortcuts import render

from wagtail.images.models import Image


def display_all_images(request):
    all_images = Image.objects.all()

    return render(request, 'all_images.html', {
        'images': all_images
    })


def download_images(request):
    all_images = Image.objects.all()

    file_storage = get_storage_class()()

    with tempfile.TemporaryDirectory() as tempdir:
        zip_filename = os.path.join(tempdir, 'content.zip')

        logs = f"Exporting all images"

        with zipfile.ZipFile(zip_filename, 'w') as zf:

            for image_def in all_images:
                if not image_def:
                    continue

                filename = image_def.file.name

                try:
                    with file_storage.open(filename, 'rb') as f:
                        zf.writestr(filename, f.read())
                except FileNotFoundError:
                    msg = "File " + str(filename) + " is not found on local file storage and was not exported."
                    logging.error(msg)
                    logs += msg + "\n"

            zf.writestr('report.txt', logs)

        with open(zip_filename, 'rb') as zf:
            data = zf.read()
            b = io.BytesIO(data)

    response = HttpResponse(b.getvalue(), content_type='application/x-zip-compressed')
    response['Content-Disposition'] = 'attachment; filename=wagtail-export.zip'

    return response
