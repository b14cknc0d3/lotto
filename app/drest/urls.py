from dynamic_rest import routers
from . import views
from django.conf.urls import include
from django.urls import path

router = routers.DynamicRouter()
router.register(r'filter', views.LnoViewSet)
# router.register(r'users', views.ResellerViewSet)
router.register(r'sale', views.LnoFilterViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls))
]
