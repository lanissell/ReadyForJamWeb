from django.core.cache import cache
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def get_cache(name):
    cacheData = cache.get(name)
    if cacheData is None:
        return None
    return cacheData

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'get_cache': get_cache,
    })
    return env