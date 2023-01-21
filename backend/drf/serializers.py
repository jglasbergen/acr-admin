from rest_framework import serializers
from django.contrib.auth.models import User, Group
from containerreg.models import Registry, Image


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class RegistrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registry
        fields = ["reg_code", "name"]


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ["image_tag", "registry"]
