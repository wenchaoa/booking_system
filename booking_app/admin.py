from django.contrib import admin
from booking_app.models import Building, Room, Date, Timeperiod
from booking_app.models import UserProfile, Event

# Register your models here.


class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'building', 'number', 'manager')
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'date', 'room')

# Register models with the admin interface
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(UserProfile)

admin.site.register(Date)
admin.site.register(Timeperiod)
admin.site.register(Event, EventAdmin)

"""
Booking_app admin.py
make model data accessible via the Django admin web interface
"""
