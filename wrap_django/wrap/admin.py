from django.contrib import admin
from .models import User, Admin,Booking,WrapUser,PurchaseBin,Redeem



# Register your models here.
admin.site.register(User)
admin.site.register(PurchaseBin)
admin.site.register(Redeem)
admin.site.register(WrapUser)
admin.site.register(Booking)
admin.site.register(Admin)