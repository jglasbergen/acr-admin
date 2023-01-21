from django.contrib.auth.models import User, Group
from containerreg.models import Image, Registry

from rest_framework import viewsets
from rest_framework import permissions
from drf.serializers import (
    UserSerializers,
    GroupSerializer,
    RegistrySerializer,
    ImageSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegistryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
