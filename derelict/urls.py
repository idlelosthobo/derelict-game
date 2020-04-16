from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views import generic
from app.core.views import home

admin.site.site_header = "Derelict Administration"
admin.site.site_title = "Derelict Admin Portal"
admin.site.index_title = "Welcome to the Derelict Game Administration Portal"

urlpatterns = [
 path('', home, name='home'),
 path('admin/', admin.site.urls),
 path('api/', include(router.urls), name='api'),
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

# Other
urlpatterns += [
    path('palette/', generic.TemplateView.as_view(template_name='palette.html')),
]
