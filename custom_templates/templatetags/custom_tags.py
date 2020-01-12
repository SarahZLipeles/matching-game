from django import template
import os
register = template.Library()

@register.inclusion_tag('_delayed_next.html')
def delayed_next(wait=2000):
    return {}

@register.inclusion_tag('_matching_box.html')
def matching_box():
    return {}
