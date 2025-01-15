from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

def environment(**options):
    autoescape = options.pop('autoescape', True)
    loader = options.pop('loader', None)
    env = Environment(
        autoescape=autoescape,
        loader=loader,
        **options
    )

    env.globals.update({
        'static': static,
        'url': reverse
    })

    return env
