from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from profiles.models import get_request_profile

from .models import Spellbook


def needs_login(func):
    """Redirects route to the loggin page if the user is not logged in"""
    def redirect_if_not_logged_in(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        return func(request, *args, **kwargs)

    return redirect_if_not_logged_in


def needs_login_or_token(func):
    """
    Checks that a spellbook route is accessed either through the owning profile or
    with the use of the spellbook token. If not, serves a 404.
    """
    def redirect_if_not_profile_or_token(request, pk, *args, **kwargs):
        spellbook = get_object_or_404(Spellbook, pk=pk)

        if request.GET.get('token') != spellbook.token and \
                spellbook.profile != get_request_profile(request):
            raise Http404('No Spellbook matches the given query.')

        return func(request, pk, *args, **kwargs)

    return redirect_if_not_profile_or_token
