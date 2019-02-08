from rest_framework import serializers
from houses.models import House, COUNTRY_CHOICES

from django.contrib.auth.models import User

# -- Using ModelSerializers -- #


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'name', 'city', 'country', 'number_of_rooms', 'rating', 'price_per_day', 'avaliable')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
