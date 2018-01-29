from rest_framework import generics
from django.contrib.auth import get_user_model
from ..models import BlogPost, image
from .serializers import (
    BlogPostSerializers,
    BlogImageSerializers,
    UserLoginSerializer,
    UserCreateSerializer
    )

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.permissions import (
    AllowAny
    )


####################################################################################
####################################################################################
####################################################################################

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializers
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

class  BlogImageListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogImageSerializers

    def get_queryset(self):
        return image.objects.all()

class UserCreateAPIView(generics.CreateAPIView):
    User = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
