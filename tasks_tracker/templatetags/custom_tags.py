from django import template

register = template.Library()


@register.filter(name='endswith')
def endswith(value: str, arg):
    return value.lower().endswith(arg)
