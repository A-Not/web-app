from .serializers import PostSerializer, LiveSerializer, TerminateSerializer, ImageDetectionSerializer
from .models import Post, LiveCam, Terminate, ImageDetection
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import os
import subprocess
from rest_framework import viewsets
from django.contrib.auth.models import User

# Create your views here.


class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        path = os.getcwd()

        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            file = request.data.get("file")
            dat = file.name
            os.system("start/min darknet.exe detector demo ./data/obj.data yolov4-tiny.cfg yolov4-tiny_best.weights ./media/" +
                      dat+" -json_port 8070 -mjpeg_port 8090 -ext_output -dont")

            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetectionView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        path = os.getcwd()
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            file = request.data.get("file")
            dat = file.name
            os.system("start/min darknet.exe detector test ./data/obj.data yolov4-tiny.cfg yolov4-tiny_best.weights ./media/" +
                      dat+" -ext_output")
            #os.system("start/min python move.py")

            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LiveView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = LiveCam.objects.all()
        serializer = LiveSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        path = os.getcwd()
        posts_serializer = LiveSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            print(path)
            os.system("start/min darknet.exe detector demo ./data/obj.data yolov4-tiny.cfg yolov4-tiny_best.weights -c 1 -json_port 8070 -mjpeg_port 8090 -ext_output -dont_show -thresh 0.50" )
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TerminateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Terminate.objects.all()
        serializer = TerminateSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        path = os.getcwd()
        posts_serializer = TerminateSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            os.system("taskkill/IM darknet.exe")
           
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
