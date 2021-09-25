from django import template
register = template.Library()

@register.simple_tag
def find_active_search(url, search_str):
    return url + search_str
