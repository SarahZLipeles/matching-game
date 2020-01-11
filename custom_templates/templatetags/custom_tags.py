from django import template
import os
register = template.Library()

@register.inclusion_tag('_delayed_next.html')
def delayed_next(wait=2000):
    return {}
