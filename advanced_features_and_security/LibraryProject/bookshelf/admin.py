from django.contrib import admin
from . import CustomUser, CustomUserAdmin
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)