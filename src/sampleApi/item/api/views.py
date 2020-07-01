from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from item.models import Item
from .serializers import ItemSerializer

class ItemListAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Item.objects.all()
        serializer = ItemSerializer(qs, many=True)
        return Response(serializer.data)

class ItemAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = ItemSerializer

    def get_queryset(self):
        qs = Item.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(name__icontains=query)
        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ItemDetailAPIView(
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)