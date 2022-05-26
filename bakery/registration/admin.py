from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    search_fields = ["id", "email", "name"]

    class Meta:
        model = User


# Register your models here.
admin.site.register(User, UserAdmin)
