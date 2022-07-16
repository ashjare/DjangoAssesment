from django.contrib import admin
from .models import emp_details
# Register your models here.
@admin.register(emp_details)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')