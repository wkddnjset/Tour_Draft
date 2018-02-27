from rest_framework import generics, serializers
from ..models import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

# 다른 앱 import
from django.apps import apps
Item = apps.get_model('_Item', 'Item')


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 카테 조회 api (생성은 디비에서만 조회가 필요할경우가 있을까봐... 조회만 일단만듦)
class CateDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CateSerializer

    def get_queryset(self):
        return Category.objects.all()


# Review 생성 api
class ReviewCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# 유저-리뷰 조회 (전체조회) api
class UserReviewListView(generics.ListAPIView):     # LIST 조회는 LISTAPI로 !! RUDAPI는 한항목조회만가능 결과가 1개이상이면 ERROR!
    serializer_class = ReviewSerializer

    # lookup_field --> LISTAPI는 룩업필드 안먹힘 아래방법으로 querying 필요

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs['user_id']
        query_set = Review.objects.filter(user_id=user_id)

        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 유저-리뷰 조회 (아이템별개별) api
class UserReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    lookup_field = 'user_id'

    def get_queryset(self, *args, **kwargs):

        item_id=self.kwargs['item_id']
        query_set = Review.objects.filter(item_id=item_id)

        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 아이템-리뷰 조회 (전체조회) api
class ItemReviewListView(generics.ListAPIView):     # LIST 조회는 LISTAPI로 !! RUDAPI는 한항목조회만가능 결과가 1개이상이면 ERROR!
    serializer_class = ReviewSerializer

    # lookup_field --> LISTAPI는 룩업필드 안먹힘 아래방법으로 querying 필요

    def get_queryset(self, *args, **kwargs):
        item_id = self.kwargs['item_id']
        query_set = Review.objects.filter(item_id=item_id)

        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 아이템-리뷰 조회 (유저별개별) api
class ItemReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    lookup_field = 'item_id'

    def get_queryset(self, *args, **kwargs):

        user_id=self.kwargs['user_id']
        query_set = Review.objects.filter(user_id=user_id)

        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Pick 생성 api
class PickCreateView(generics.ListCreateAPIView):
    queryset = Pick.objects.all()
    serializer_class = PickSerializer


# 유저-픽 조회 (전체조회) api
class UserPickListView(generics.ListAPIView):     # LIST 조회는 LISTAPI로 !! RUDAPI는 한항목조회만가능 결과가 1개이상이면 ERROR!
    serializer_class = PickSerializer

    # lookup_field --> LISTAPI는 룩업필드 안먹힘 아래방법으로 querying 필요

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs['user_id']
        query_set = Pick.objects.filter(user_id=user_id)

        if query_set.exists():
            return query_set
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 유저-픽 조회 (아이템별개별) api
class UserPickDetailView(APIView):
    serializer_class = PickSerializer
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        item_id = self.kwargs['item_id']
        query_set = Pick.objects.filter(item_id=item_id, user_id=user_id)

        # print(query_set)
        if query_set.exists():
            return Response({'is_pick' : True})

        else:
            return Response({'is_pick': False})
'''
    def get_queryset(self, *args, **kwargs):
        item_id=self.kwargs['item_id']
        query_set = Pick.objects.filter(item_id=item_id)

        if query_set.exists():
            return Response(True)
        else:
            return Response(False)'''
