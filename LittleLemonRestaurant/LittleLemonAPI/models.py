from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    No_of_guests = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'{self.name}--->Booking Date: {self.date}---> Guests: {self.No_of_guests}'


# Add code to create Menu model
class MenuItems(models.Model):
   title = models.CharField(max_length=200) 
   price = models.DecimalField(null=False,max_digits=5, decimal_places=2) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   class Meta:
     verbose_name_plural = 'Menu Items'

   def __str__(self):
        return f'{self.title} : {self.price:.2f}'