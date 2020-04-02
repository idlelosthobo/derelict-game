from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views import generic
from app.core.views import home

admin.site.site_header = "Mythic Game"
admin.site.site_title = "Mythic Admin Portal"
admin.site.index_title = "Welcome to the System Administration Portal"

urlpatterns = [
 path('', home, name='home'),
 path('admin/', admin.site.urls),
 path('api/', include(router.urls)),
]

# Account
urlpatterns += [
    path('accounts/', include('app.registration.urls')),
]

# Character
urlpatterns += [
    path('character/', include('app.character.urls')),
]

# Ui
urlpatterns += [
    path('ui/', include('app.ui.urls')),
]
