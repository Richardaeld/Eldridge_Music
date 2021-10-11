from django import template
register = template.Library()


@register.simple_tag
def convert_str(instance):
    return str(instance)


@register.simple_tag
def convert_str_list(instances):
    item_list = []
    for item in instances:
        item_list.append(str(item))
    return item_list


@register.simple_tag
def title_image_name(name):
    return str(name).title()
