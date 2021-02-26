from rest_framework import serializers

from .models import Image, ImageAction


class ImageActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageAction
        fields = '__all__'


class ImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'user', 'image')


class ImageListSerializer(serializers.ModelSerializer):
    actions = ImageActionSerializer(many=True)

    class Meta:
        model = Image
        fields = ('id', 'user', 'image', 'actions')



