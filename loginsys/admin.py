from django.contrib import admin
from loginsys.models import *
from datetime import datetime
from django.contrib.auth.models import User


# class UserSet(admin.ModelAdmin):
#     fields = ('first_name', 'last_name')
#     list_filter = ('first_name',)
#     list_display = ('last_name', 'first_name', 'calculate')
#     search_fields = ('first_name', 'last_name')
#     list_per_page = 10
#
#     def calculate(self, obj):
#         d1 = obj.first_name
#         return d1
#
# # Register your models here.
# admin.site.register(UserSet)