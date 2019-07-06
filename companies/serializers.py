from rest_framework import serializers
from .models import Stock
from django.contrib.auth.models import User, Group


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        # fields = ('ticker', 'volume')
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('url', 'username', 'email', 'groups')
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = ('url', 'name')
        fields = '__all__'