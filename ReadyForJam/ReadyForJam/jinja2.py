from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def environment(**options):
    env = Environment(**options)
    env.globals.update({
       'url': reverse,
    })
    return env
