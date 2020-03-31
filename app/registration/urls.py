from django.urls import path, include
from app.registration import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_success/', views.register_success, name='register_success'),
    path('', include("django.contrib.auth.urls")),
]
