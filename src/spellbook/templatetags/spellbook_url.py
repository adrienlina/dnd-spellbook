from django import template
from django.urls import reverse

from profiles.models import get_request_profile

register = template.Library()


@register.simple_tag(takes_context=True)
def spellbook_url(context, route, spellbook):
    """The url for a spellbook page, to which we add a token if necessary"""
    url = reverse(route, args=[spellbook.pk])
    user_profile = get_request_profile(context.request)

    return (
        url
        if user_profile == spellbook.profile
        else url + "?token=" + spellbook.token
    )
