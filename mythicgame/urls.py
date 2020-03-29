from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views import generic

urlpatterns = [
 path('', generic.TemplateView.as_view(template_name='core/base.html')),
 path('admin/', admin.site.urls),
 path('api/', include(router.urls)),
]
