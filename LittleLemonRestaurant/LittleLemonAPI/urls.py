from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from djoser.urls.base import User
urlpatterns = [
    path(r'registration/', include('djoser.urls.base')),
    path('menu', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleItemView.as_view()),
    path('bookings/',views.BookingView.as_view()),
    path('bookings/<int:pk>/', views.SingleBookingItemView.as_view()),
]