from django import template
from django.utils import timezone
from django.conf import settings
register = template.Library()

@register.inclusion_tag("manager/tags/search.html")
def searchlist():
    return {}