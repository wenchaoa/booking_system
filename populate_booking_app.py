import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_system.settings')

import django
django.setup()
from booking_app.models import Building, Room

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
    # Sir Alwyn Williams Building
    building1 = [
        # Room1
        {'name': 'SCADA Lab',
         'number':'SAWB 208',
         'manager':'Marco Cook',
         'views': 114,
         'bookmarked': 10},
         
        {'name':'Baxter Lab',
         'number':'SAWB 105',
         'manager':'Gerardo Aragon Camarasa',
         'views': 53,
         'bookmarked': 9},
         
        {'name':'VR Suite',
         'number':'SAWB 408',
         'manager':'Julie Williamson',
         'views': 20,
         'bookmarked': 8} ]
    
    building2 = [
        {'name':'HCI Lab',
         'number':'G133',
         'manager':'Steve Brewster',
         'views': 32,
         'bookmarked': 7},
         
        {'name':'Net Lab',
         'number':'G131',
         'manager':'Kyle Simpson',
         'views': 12,
         'bookmarked': 6} ]
    
    #no_pages = []
    
    buildings = {'Sir Alwyn Williams Building': {'rooms': building1, 'views': 100, 'likes': 50},
                         '18 Lilybank Gardens': {'rooms': building2, 'views': 80, 'likes': 40},}
                
    for building, building_data in buildings.items():
        b = add_building(building, views=building_data['views'], likes=building_data['likes'])
        for r in building_data['rooms']:
            add_room(b, r['name'], r['number'], r['manager'], views=r['views'], bookmarked=r['bookmarked'])
    
    for b in Building.objects.all():
        for r in Room.objects.filter(building=b):
            print(f'- {b}: {r}')


def add_room(building, name, number, manager, views=0, bookmarked=0):
    r = Room.objects.get_or_create(building=building, name=name)[0]
    r.number=number
    r.manager=manager
    r.views=views
    r.bookmarked=bookmarked
    r.save()
    return r

def add_building(name, views=0, likes=0):
    b = Building.objects.get_or_create(name=name)[0]
    b.views = views
    b.likes = likes
    b.save()
    return b

# Start execution here!
if __name__ == '__main__':
    print('Starting booking system population script...')
    populate()
