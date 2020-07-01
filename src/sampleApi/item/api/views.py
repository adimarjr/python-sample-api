from rest_framework import generics
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

class ItemAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = ItemSerializer

    def get_queryset(self):
        qs = Item.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(name__icontains=query)
        return qs

class ItemCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

class ItemUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

class ItemDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'