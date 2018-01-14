from django.contrib import admin
from loginsys import models

# Register your models here.

admin.site.register(models.Service)
admin.site.register(models.UserService)