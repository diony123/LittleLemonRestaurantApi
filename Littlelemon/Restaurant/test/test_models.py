from django.test import TestCase
from Restaurant.models import Menu,Booking
class BookingsTestCase(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name='tony', reservation_date='2023-04-06', No_of_guests=2)
        itemstr = str(item)
        self.assertEqual(itemstr, 'tony--->Booking Date: 2023-04-06---> Guests: 2')

class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Salad', price=11.99, menu_item_description='Salad')
        itemstr = str(item)
        self.assertEqual(itemstr, 'Salad : 11.99')