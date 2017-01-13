from django.contrib import admin

# Register your models here.
from .models import Conference, Person, Registrant, Accommodation, AccommodationRoomOccupant

admin.site.register(Conference)
admin.site.register(Person)
admin.site.register(Registrant)
admin.site.register(Accommodation)
admin.site.register(AccommodationRoomOccupant)
