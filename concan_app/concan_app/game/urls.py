from django.urls import path

from .views.index import IndexView
from .views.lobby import LobbyView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('lobby/', LobbyView.as_view(), name='lobby')
]