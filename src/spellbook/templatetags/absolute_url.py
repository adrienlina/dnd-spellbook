from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def absolute_url(context, route, *args, **kwargs):
    """The absolute url for a request and a route"""

    return context.request.build_absolute_uri(reverse(route, args=args, kwargs=kwargs))
