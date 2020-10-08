from django import template
from booking_app.models import Room

register = template.Library()

@register.inclusion_tag('booking_app/rooms.html')
def get_room_list(current_room=None):
    return {'rooms': Room.objects.all(),
            'current_room': current_room}
