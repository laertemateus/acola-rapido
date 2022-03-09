'''
Tags utilitárias
'''

from django.utils.safestring import mark_safe
from django import template
  
register = template.Library()

@register.simple_tag
def icon(icon):
    '''
    Gera o código HTML para a tag
    '''
    return mark_safe('<i class="fa fa-'+icon+'"></i>')

@register.filter
def debug(obj):
    return dir(obj)