from django.urls import reverse
from django.utils.http import urlencode


def build_url(*args, **kwargs):
    """Builds a url just like reverse, but adds get parameters to it"""
    get_params = kwargs.pop('get', {})
    # Filter empty get params
    get_params = {
        key: value
        for key, value in get_params.items()
        if value or value == 0
    }

    url = reverse(*args, **kwargs)

    return ('{url}?{params}'.format(url=url, params=urlencode(get_params))
            if get_params
            else url)
