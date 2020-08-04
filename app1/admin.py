from django.contrib import admin

# Register your models here.
from app1.models import Room, Book


# Register your models here.
class Roomadmin(admin.ModelAdmin):
    pass


class Bookadmin(admin.ModelAdmin):
    pass


admin.site.register(Room, Roomadmin)
admin.site.register(Book, Bookadmin)
