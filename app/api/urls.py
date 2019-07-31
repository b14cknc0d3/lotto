from django.contrib import admin
from django.urls import path, include
from drest import urls as router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router)),

    path('api/auth/', include('rest_auth.urls')),
]
