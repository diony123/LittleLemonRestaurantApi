from django.test import TestCase
from ..models import MenuItems,Booking
class BookingsTestCase(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name='tony', date='2023-04-06', No_of_guests=2)
        itemstr = str(item)
        self.assertEqual(itemstr, 'tony--->Booking Date: 2023-04-06---> Guests: 2')

class MenuItemsTestCase(TestCase):
    def test_get_item(self):
        item = MenuItems.objects.create(title='Salad', price=11.99, menu_item_description='Salad')
        itemstr = str(item)
        self.assertEqual(itemstr, 'Salad : 11.99')