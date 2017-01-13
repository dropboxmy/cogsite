from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Person(models.Model):
    family_name = models.CharField(max_length=25)
    given_name  = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    conference = models.ManyToManyField(Conference, 
        through='Registrant',
        through_fields=('person', 'conference'))
    
    def __str__(self):
        return '{} {}'.format(self.family_name, self.given_name)


class Accommodation(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    room = models.CharField(max_length=30)
    capacity = models.IntegerField()
    remark = models.CharField(max_length=200, blank=True, null=True)    

    def __str__(self):
        return '{} ({})'.format(
            self.room, 
            self.capacity
        )

class Registrant(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    person  = models.ForeignKey(Person, on_delete=models.CASCADE)
    remark = models.CharField(max_length=200, blank=True, null=True)
    accommodation = models.ManyToManyField(Accommodation, 
        through='AccommodationRoomOccupant',
        through_fields=('registrant', 'accommodation'))
    
    def __str__(self):
        return '{} - {} {}'.format(
            self.conference.name, 
            self.person.given_name,
            self.person.family_name,
        )

class AccommodationRoomOccupant(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    registrant  = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    # remark = models.CharField(max_length=200, blank=True, null=True)    

    def __str__(self):
        return '{} - {} {}'.format(
            self.accommodation.room, 
            self.registrant.person.given_name,
            self.registrant.person.family_name,
        )
