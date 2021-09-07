from django.shortcuts import render

def coaxsio(request):
    """ This view is for the online piano the coaxsio """
    return render(request, 'coaxsio/coaxsio.html')