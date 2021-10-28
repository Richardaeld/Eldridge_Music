from django.shortcuts import render

def merchandise(request):

    template = 'merchandise/merchandise.html'

    context = {}

    return render(request, template, context)