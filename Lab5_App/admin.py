from django.contrib import admin
from loginsys import models
# Register your models here.


class ServiceClass(admin.ModelAdmin):
    fields = (('id', 'title'), 'price', 'picture')
    list_filter = ('price',)
    list_display = ('id', 'title', 'price', 'picture')
    search_fields = ('title', 'id')
    list_per_page = 10

class UserServiceClass(admin.ModelAdmin):
    fields = (('id', 'service'), 'user', 'description', 'desc_picture')
    list_filter = ('id', 'user')
    list_display = ('id', 'service', 'user', 'description', 'desc_picture')
    search_fields = ('user', 'service')
    list_per_page = 10


admin.site.register(models.Service, ServiceClass)
admin.site.register(models.UserService, UserServiceClass)
