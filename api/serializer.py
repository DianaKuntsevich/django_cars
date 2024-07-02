from rest_framework import serializers

from car_app.models import Auto, Image


class ImageAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')


class AutoSerializer(serializers.ModelSerializer):
    images = ImageAutoSerializer(read_only=True, many=True)

    class Meta:
        model = Auto
        fields = '__all__'
