import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'hastexo_guacamole_client.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from .consumers import GuacamoleWebSocketConsumer  # noqa E402

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        #AuthMiddlewareStack(
            URLRouter([
                path('hastexo-xblock/websocket-tunnel',
                     GuacamoleWebSocketConsumer.as_asgi()),
            ])
        #)
    ),
})
