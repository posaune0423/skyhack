from django import template

register = template.Library()


@register.filter
def subtract(value1, value2):
    return value2 - value1
