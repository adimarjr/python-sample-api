from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from sampleApi.serializers import UserSerializer, GroupSerializer
from item.models import Item

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
def home_page(request):
    # my_title = "Hello there...."
    qs = Item.objects.all()[:5]
    context = {"title": "Welcome to test", 'item_list': qs}
    return render(request, "home.html", context)