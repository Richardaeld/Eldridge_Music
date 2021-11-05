from django.http import HttpResponse


class StripeWH_Handler:
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
            content=f'Generic/Unknown/Unexpected webhook received: {event["type"]}',
            status=200
            )

    def handle_payment_intent_succeeded(self,event):
        """
        Contorls payment_intent.succeeded webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
            )

    def handle_payment_intent_payment_failed(self,event):
        """
        Contorls payement_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
            )
