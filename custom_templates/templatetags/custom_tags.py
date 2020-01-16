from django import template
import os
register = template.Library()

@register.inclusion_tag('_delayed_next.html')
def delayed_next(wait=2000):
    return {}

@register.inclusion_tag('_matching_box.html')
def matching_box(choices=[8,3,8,7,0,6,8,1,5], matching_box_id="matching_box", rounds=1):
    template_vars = {
        "choices": choices,
        "matching_box_id": matching_box_id,
        "rounds": rounds
    }
    return template_vars
