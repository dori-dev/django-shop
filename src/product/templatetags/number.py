from django import template

register = template.Library()


@register.filter
def format_comma(number):
    if isinstance(number, int):
        return f"{number:,}"
    if isinstance(number, str) and number.isdigit():
        return f"{int(number):,}"
    return 0
