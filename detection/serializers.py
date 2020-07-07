from rest_framework import serializers
from .models import Post, LiveCam, Terminate, ImageDetection
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveCam
        fields = '__all__'


class TerminateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminate
        fields = '__all__'


class ImageDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageDetection
        fields = '__all__'
