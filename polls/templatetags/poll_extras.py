from django import template

register = template.Library()

# custom functions for html files, subtraction and supplementation

@register.filter
def subtract(value, arg):
    return value - arg



@register.filter
def add(value, arg):
    return value + arg