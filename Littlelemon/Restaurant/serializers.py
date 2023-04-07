from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User, Group
from decimal import Decimal
from django.db import models
from datetime import datetime

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'reservation_date','reservation_slot', 'No_of_guests']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'menu_item_description']


class UserSerializer(serializers.ModelSerializer):
    Date_Joined = serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(write_only=True, default=datetime.now)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'Date_Joined']

    def get_Date_Joined(self, obj):
        return obj.date_joined.strftime('%Y-%m-%d')

