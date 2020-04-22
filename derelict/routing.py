# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from app.chat.routing import chat_websocket_urlpatterns
from app.game.routing import game_websocket_urlpatterns
from app.ui.routing import ui_websocket_urlpatterns

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat_websocket_urlpatterns +
            game_websocket_urlpatterns +
            ui_websocket_urlpatterns
        )
    ),
})