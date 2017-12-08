from django import template


register = template.Library()

@register.filter('min')
def minusculas(valor):
    return 'hi'



