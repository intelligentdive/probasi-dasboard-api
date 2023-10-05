from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from servicename.views import TaskViewSet
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("user.urls")),
    path('api/', include(router.urls)),
    path("api/", include("status.urls")),
    path('api/', include('blog.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
