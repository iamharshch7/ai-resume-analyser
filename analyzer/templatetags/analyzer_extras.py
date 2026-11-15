from django import template
import json

register = template.Library()

@register.filter
def json_load(value):
    try:
        return json.loads(value)
    except:
        return []
