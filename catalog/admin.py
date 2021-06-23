from django.contrib import admin

# Register your models here.
from .models import Customer, Services, Servis_order

admin.site.register(Customer)
admin.site.register(Services)
admin.site.register(Servis_order)

