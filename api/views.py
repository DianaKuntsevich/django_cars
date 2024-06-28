from rest_framework.viewsets import ModelViewSet

from car_app.models import Auto

class AutoListViewSet(ModelViewSet):
    queryset = Auto.objects.all().prefetch_related('images')



