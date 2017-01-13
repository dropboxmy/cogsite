from django import forms

from .models import Conference, Person, Registrant, \
    Accommodation, AccommodationRoomOccupant

class ConferenceForm(forms.ModelForm):
    
    class Meta:
        model = Conference
        fields = ['name']

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['family_name', 'given_name', 'date_of_birth']

class RegistrantForm(forms.ModelForm):
    conference = forms.ModelMultipleChoiceField(queryset=Conference.objects.all())
    class Meta:
        model = Registrant
        fields = ['conference', 'accommodation', 'remark']

class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['room', 'capacity', 'remark']

class AccommodationRoomOccupantForm(forms.ModelForm):
    accommodation = forms.ModelMultipleChoiceField(queryset=Accommodation.objects.all())
    registrant = forms.ModelMultipleChoiceField(queryset=Registrant.objects.all())
    class Meta:
        model = AccommodationRoomOccupant
        fields = ['accommodation', 'registrant']