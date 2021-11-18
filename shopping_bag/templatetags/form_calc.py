from django import template
register = template.Library()


# multiples items by quantity
@register.simple_tag
def sub_total(amount, quantity):
    return amount * quantity
