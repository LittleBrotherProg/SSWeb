from django.db import models
import uuid

# Create your models here.

class Services(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """

    servis_name = models.CharField(max_length=30)
    photo_id = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        """
        String for representing the Model object
        """

        return '%s %s' % (self.servis_name, self.photo_id)


class Customer(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Phone_numb = models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s, %s' % (self.First_name, self.Last_name, self.Phone_numb)


class Servis_order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="ID заказа")

    cust = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)

    Services = models.ForeignKey('Services', on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return 'id (%s), ИФ (%s %s), %s' % (self.id, self.cust.First_name, self.cust.Last_name, self.Services.servis_name)
