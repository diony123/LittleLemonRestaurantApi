from django.test import TestCase
from .models import MenuItems,Booking

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


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItems.objects.create(title='Far breton', price=8.50, menu_item_description="Gateux à la part 1")
        self.item2 = MenuItems.objects.create(title='Tarte aux fraises', price=5.50, menu_item_description="Gateux à la part 2")
        self.item3 = MenuItems.objects.create(title='Tarte au citron', price=4.50, menu_item_description="Gateux à la part 3")
        self.item4 = MenuItems.objects.create(title='Flan nature', price=7.99, menu_item_description="Gateux à la part 4")

    def test_getall(self):
        farbreton = MenuItems.objects.get(title='Far breton')
        tarteauxfraises = MenuItems.objects.get(title='Tarte aux fraises')
        tarteaucitron = MenuItems.objects.get(title='Tarte au citron')
        flannature = MenuItems.objects.get(title='Flan nature')

        self.assertEqual(str(farbreton), 'Far breton : 8.50')
        self.assertEqual(farbreton.menu_item_description,"Gateux à la part 1")
        self.assertEqual(str(tarteauxfraises), 'Tarte aux fraises : 5.50')
        self.assertEqual(tarteauxfraises.menu_item_description,"Gateux à la part 2")
        self.assertEqual(str(tarteaucitron), 'Tarte au citron : 4.50')
        self.assertEqual(tarteaucitron.menu_item_description,"Gateux à la part 3")
        self.assertEqual(str(flannature), 'Flan nature : 7.99')
        self.assertEqual(flannature.menu_item_description,"Gateux à la part 4")