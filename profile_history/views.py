from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from invoice.models import Invoice
from .models import User_Profile_History
from .forms import User_Profile_History_Form


@login_required
def profile(request):
    """
    Returns a view of a users personal profile page
    """
    userProfile = get_object_or_404(User_Profile_History, user=request.user)

    if request.method == 'POST':
        form = User_Profile_History_Form(request.POST, instance=userProfile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated")
        else:
            messages.error(request, (
                'Update failed. Please check the form for validity.'
            ))
    else:
        form = User_Profile_History_Form(instance=userProfile)

    full_name = userProfile.user.get_full_name()
    invoices = userProfile.invoices.all().order_by('-date_time')

    context = {
        'full_name': full_name,
        'form': form,
        'invoices': invoices,
        'on_profile_history_page': True
    }

    return render(request, 'profile_history/profile.html', context)


def invoice_history(request, invoice_number):
    """
    Returns a view of previous orders made my user
    """
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)

    messages.info(request, (
        f'This is a past confirmation for invoice number {invoice_number}. '
        f'A conformation email was sent on the invoice date.'
    ))

    template = 'invoice/checkout_success.html'
    context = {
        'invoice': invoice,
        'from_profile': True
    }
    return render(request, template, context)
