from django import template
register = template.Library()


@register.simple_tag
def sub_total(amount, quantity):
    return amount * quantity