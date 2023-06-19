from django import template

register = template.Library()


@register.filter
def lower(value):
    return_value = f"{value} - lorem ipsum dollar"
    return return_value