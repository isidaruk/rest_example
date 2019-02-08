from django.contrib.auth.models import User

from rest_framework import serializers

from houses.models import House


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = House
        fields = ('url', 'id', 'owner', 'name',
                  'city', 'country', 'number_of_rooms', 'rating', 'price_per_day', 'avaliable')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    houses = serializers.HyperlinkedRelatedField(many=True, view_name='house-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'houses')
