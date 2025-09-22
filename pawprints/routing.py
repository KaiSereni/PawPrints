"""
Author: Peter Zujko (@zujko)
        Lukas Yelle (@lxy5611)
Desc: Implements channels routing for the whole pawprints app.
"""
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import petitions.routing
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            petitions.routing.websocket_urlpatterns
        )
    ),
})
