from channels.routing import ProtocolTypeRouter, URLRouter
from . import middlewares
from core import routing as core_routing

application = ProtocolTypeRouter({
    "websocket": middlewares.UniversalAuthMiddlewareStack(
        URLRouter(
            core_routing.websocket_urlpatterns
        )
    ),
})
