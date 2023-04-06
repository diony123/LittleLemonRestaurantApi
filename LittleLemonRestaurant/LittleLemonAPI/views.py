from django.shortcuts import render
from rest_framework import generics
from .models import MenuItems,Booking
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
# Create your views here.
class MenuItemView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = ['price']
    search_fields = ['title']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class SingleItemView(generics.RetrieveUpdateDestroyAPIView, generics.RetrieveAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    

class BookingView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    ordering_fields = ['date']
    search_fields = ['date','name']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class SingleBookingItemView(generics.RetrieveUpdateDestroyAPIView, generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]