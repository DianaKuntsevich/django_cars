from django.urls import path

from .views import AutoListView

urlpatterns = [
    path('', AutoListView.as_view(), name='cars_list'),
]

