from django.urls import path
from app.ui import views

urlpatterns = [
    path('', views.ui_game, name='ui_game'),
]
