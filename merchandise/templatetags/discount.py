from django import template
register = template.Library()


# Calculates new price from discount value
@register.simple_tag
def discount(merch):
    return round(merch.price - (merch.price * (merch.discount / 100)), 2)
