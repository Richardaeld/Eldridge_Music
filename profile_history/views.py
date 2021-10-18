from django.shortcuts import get_object_or_404, render
from .models import User_Profile_History

def profile(request):

    user = get_object_or_404(User_Profile_History, user=request.user)

    context = {
        'user': user
    }

    return render(request, 'profile_history/profile.html', context)
    