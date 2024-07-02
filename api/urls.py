from django.urls import path, include
from rest_framework import routers

from .views import AutoListViewSet


router_auto = routers.SimpleRouter()
router_auto.register(r'auto', AutoListViewSet,)

urlpatterns = [
    path('', include(router_auto.urls), name='autos')
]