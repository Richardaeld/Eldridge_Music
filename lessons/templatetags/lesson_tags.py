from django import template
register = template.Library()


@register.simple_tag
def convert_str(instance):
    return str(instance)


@register.simple_tag
def title_image_name(name):
    return str(name).title()
