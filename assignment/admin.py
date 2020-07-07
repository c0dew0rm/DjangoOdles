from django.contrib import admin

# Register your models here.
from .models import Address, Profile

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass