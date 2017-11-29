from django import template


register = template.Library()


def minusculas(valor):
    return valor.lower()


register.filter('minusculas',minusculas)