from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from car_app.models import Auto
from .serializer import AutoSerializer
from .permission import IsAdminOrReadOnly


class AutoListViewSet(ModelViewSet):
    queryset = Auto.objects.all().prefetch_related('images')
    serializer_class = AutoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('price_usd', 'price_byn', 'price_eur', "price_rub", "city_location", "year", "brand", "model")
    search_fields = ('abs', 'alloy_wheels', 'anti_slip_system', 'aux_ipod', 'bluetooth', 'body_type', 'brand',
                     'cd_mp3_player', 'city_location', 'climate_control', 'color', 'condition', 'cruise_control',
                     'description', 'drive_type', 'electro_seat_adjustment', 'engine_capacity', 'engine_type', 'esp',
                     'exchange', 'fog_lights', 'front_glass_lift', 'front_safebags', 'generation', 'generation_with_years',
                     'hatch', 'immobilizer', 'interior_color', 'interior_material', 'led_lights', 'media_screen',
                     'mileage_km', 'mirror_heating', 'model', 'number_of_seats', 'organization', 'parktronics',
                     'price_byn', 'price_eur', 'price_rub', 'price_usd', 'rain_detector', 'rear_glass_lift',
                     'rear_safebags', 'rear_view_camera', 'seat_heating', 'seller', 'side_safebags',
                     'steering_wheel_heating', 'steering_wheel_media_control', 'transmission_type', 'usb',
                     'xenon_lights', 'year')
    ordering_fields = ('price_usd', 'price_byn', 'price_eur', "price_rub", "city_location", "year", "brand", "model")
    permission_classes = IsAdminOrReadOnly,

