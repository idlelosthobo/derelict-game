from django.urls import path
from app.character import views

urlpatterns = [
    path('create/', views.CharacterCreateFormView.as_view(), name='character_create_view'),
    path('select/', views.CharacterSelectView.as_view(), name='character_select_view'),
    path('pick/<int:pk>/', views.character_pick, name='character_pick'),
]