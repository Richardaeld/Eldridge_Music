from django.http import HttpResponse


class StripeWH_Hndler:
    """
    Controls webhooks from Stripe
    """

    def __init__(self,request):
        self.request = request

    def handle_event(self,event):
        """
        Contorls generic/unknown/unexpected webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
            )
