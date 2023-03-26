from django.contrib import admin
from .models import User, Admin,Booking,WrapUser



# Register your models here.
admin.site.register(User)
admin.site.register(WrapUser)
admin.site.register(Booking)
admin.site.register(Admin)