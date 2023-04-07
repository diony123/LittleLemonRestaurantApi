from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'', views.BookingViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('bookings', views.bookings, name='bookings'), 
    path('api/bookings/', include(router.urls)),
    path('api/menu/', views.MenuView.as_view()),
    path('api/menu/<int:pk>/', views.SingleItemView.as_view()),
    path('api/bookings/',views.BookingView.as_view()),
    path('api/bookings/<int:pk>/', views.SingleBookingItemView.as_view()),
    path('api-token-auth/',obtain_auth_token),
    path(r'registration/', include('djoser.urls')),
]