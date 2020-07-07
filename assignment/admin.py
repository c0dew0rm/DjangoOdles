from django.contrib import admin

# Register your models here.
from .models import Address, User

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass