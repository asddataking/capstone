from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyModel, User

admin.site.register(MyModel)
admin.site.register(User, UserAdmin)

