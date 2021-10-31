from django.shortcuts import render


def shopping_bag(request):

    template = 'shopping_bag/shopping_bag.html'

    context = {}

    return render(request, template, context)