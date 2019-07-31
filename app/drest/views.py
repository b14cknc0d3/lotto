from rest_framework.response import Response
from dynamic_rest.viewsets import DynamicModelViewSet
from .serailizer import LnoSerializer
from .models import Lno
from .permissions import *


class LnoViewSet(DynamicModelViewSet):
    permission_classes = (OwnerOrReadOnly, IsAuthenticated)
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.INCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )
    model = Lno
    queryset = Lno.objects.all()
    serializer_class = LnoSerializer

    def create(self, request, *args, **kwargs):
        serializer = LnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(rname=request.user)
        return Response(serializer.data)


# class UserViewSet(DynamicModelViewSet):
#     model = user
#     queryset = user.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class SaleViewSet()
class LnoFilterViewSet(DynamicModelViewSet):
    permission_classes = (OwnerOrReadOnly, IsAuthenticated)
    serializer_class = LnoSerializer
    model = Lno
    features = (
        DynamicModelViewSet.INCLUDE, DynamicModelViewSet.EXCLUDE,
        DynamicModelViewSet.FILTER, DynamicModelViewSet.SORT,
        DynamicModelViewSet.SIDELOADING, DynamicModelViewSet.DEBUG
    )

    def list(self, request, *args, **kwargs):
        queryset = Lno.objects.filter(rname=request.user)
        serializer = LnoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = LnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(rname=request.user)
        return Response(serializer.data)

#
# class userViewSet(DynamicModelViewSet):
#     model = user
#     queryset = user.objects.all()
#     serializer_class = userSerializer
#     permission_classes = (userOwnerOrReadOnly, IsAuthenticated)
