from django.shortcuts import render

from django.conf import settings


def index(request):
    """ This view returns the index page """
    MEDIA_URL = settings.MEDIA_URL

    context = {
        'MEDIA_URL': MEDIA_URL,
    }

    return render(request, 'home/index.html', context)
