from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# from servicename.views import ServiceViewSet
router = routers.DefaultRouter()
# router.register(r'Service', ServiceViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("user.urls")),
    path('api/', include(router.urls)),
    path("api/", include("status.urls")),
    path('api/', include('blog.urls')),
    path('api/', include('servicename.urls')),

     path('api/', include('oversea_recruitment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
