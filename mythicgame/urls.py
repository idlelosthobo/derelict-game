from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views import generic

admin.site.site_header = "Mythic Game"
admin.site.site_title = "Mythic Admin Portal"
admin.site.index_title = "Welcome to the System Administration Portal"

urlpatterns = [
 path('', generic.TemplateView.as_view(template_name='core/page.html')),
 path('admin/', admin.site.urls),
 path('api/', include(router.urls)),
]

# Account
urlpatterns += [
    path('accounts/', include('app.registration.urls')),
]
