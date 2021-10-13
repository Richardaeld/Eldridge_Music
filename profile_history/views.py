from django.shortcuts import render

def profile(request):

    context = {}

    return render(request, 'profile_history/profile.html', context)
    