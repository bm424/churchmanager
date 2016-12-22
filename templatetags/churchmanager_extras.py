import re

from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def town_or_village(context, urlname):
    pattern = "^" + reverse(urlname)
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''
