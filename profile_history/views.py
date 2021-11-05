from django.shortcuts import get_object_or_404, render

from invoice.models import Invoice
from .models import User_Profile_History
from invoice.forms import InvoiceForm
from django.contrib import messages
from .forms import User_Profile_History_Form


def profile(request):

    userProfile = get_object_or_404(User_Profile_History, user=request.user)
    
    form = User_Profile_History_Form(instance=userProfile)
    invoices = userProfile.invoices.all()

    if request.method == 'POST':
        form = User_Profile_History_Form(request.POST, instance=userProfile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated")

    # invoice = InvoiceForm(initial={
    #     'name': userProfile.default_full_name,
    #     'email': userProfile.default_email,
    #     'phone': userProfile.default_phone,
    #     # 'pronouns': userProfile.default_pronouns,
    #     'city': userProfile.default_city,
    #     'street_address_billing': userProfile.default_street_address_billing,
    #     'street_address_shipping': userProfile.default_street_address_shipping,
    #     'state_county': userProfile.default_state_county,
    #     'post_code': userProfile.default_post_code,
    #     'country': userProfile.default_country,
    # })

    # if request.method == 'POST':
    #     update_user_info = User_Profile_History_Form(request.POST, instance=userProfile)
    #     if update_user_info.is_valid():
    #         update_user_info.save()
    #         messages.success(request, "Profile has been updated")
    #     else:
    #         messages.error(request, "An error occurred please try again later")
        # user = get_object_or_404(User_Profile_History, user=request.user)
        # update_user = {
        # 'default_full_name': request.POST['name'],
        # 'default_email': request.POST['email'],
        # 'default_phone': request.POST['phone'],
        # # 'default_pronouns': request.POST['default_pronouns'],
        # 'default_city': request.POST['city'],
        # 'default_street_address': request.POST['street_address'],
        # 'default_state_county': request.POST['state_county'],
        # 'default_post_code': request.POST['post_code'],
        # 'default_country': request.POST['country'],
        # }


    context = {
        'form': form,
        'invoices': invoices,
        'on_profile_history_page': True


        # 'user': userProfile,
        # 'invoice': invoice,
        # 'update_user_info': update_user_info,
    }

    return render(request, 'profile_history/profile.html', context)
    

def invoice_history(request, invoice_number):
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)

    messages.info(request, (
        f'This is a past confirmation for invoice number {invoice_number}. '
        'A conformation email was sent on the invoice date.'
    ))

    template = 'invoice/checkout_success.html'
    context = {
        'invoice': invoice,
        'from_profile': True
    }
    return render(request, template, context)