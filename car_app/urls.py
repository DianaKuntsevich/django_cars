from django.urls import path

from .views import AutoListView, AutoDetailView

urlpatterns = [
    path('', AutoListView.as_view(), name='cars_list'),
    path('<int:pk>/', AutoDetailView.as_view(), name='cars_detail'),
]

