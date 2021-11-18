from django import template
register = template.Library()


# Used to combine a URL with search string
@register.simple_tag
def find_active_search(url, search_str):
    return url + search_str


# Determines if a key word is in a URL
@register.simple_tag
def find_page(url, name):
    url = url.split('/')
    if name in url:
        return True
    else:
        return False
