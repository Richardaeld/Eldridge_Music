from django.shortcuts import get_object_or_404, render
from .models import User_Profile_History
from invoice.forms import InvoiceForm

def profile(request):

    user = get_object_or_404(User_Profile_History, user=request.user)
    invoice = InvoiceForm(initial={
        'name': user.default_full_name,
        'email': user.default_email,
        'phone': user.default_phone,
        'pronouns': user.default_pronouns,
        'city': user.default_city,
        'street_address_billing': user.default_street_address,
        'state_county': user.default_state_county,
        'post_code': user.default_post_code,
        'country': user.default_country,
    })


    context = {
        'user': user,
        'invoice': invoice,
    }

    return render(request, 'profile_history/profile.html', context)
    