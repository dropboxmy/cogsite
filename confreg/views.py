from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model

from .models import Conference, Person, Registrant, \
    Accommodation, AccommodationRoomOccupant
from .forms import ConferenceForm, PersonForm, RegistrantForm, \
    AccommodationForm, AccommodationRoomOccupantForm

APP_NAME='Enjoy God!'
BOOTSTRAP_PARAM = {
        'bootstrap_min_url'       : 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'bootstrap_min_integrity' : 'sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
        'crossorigin'             : 'anonymous',
    }

def landing(request, conference_id=None):
    if request.method=='POST':
        conference = get_object_or_404(Conference)
        form = ConferenceForm(request.POST)#, instance=conference)
        if form.is_valid():# and form_saved_or_updated(form, conference, request.user):
            form.save()
        #     return redirect(
        #          'manage_conference'
        #     )
        # else:
        #     return HttpResponse('Invalid form detected')
#    else:
    formset = ConferenceForm()
    conferences = Conference.objects.all()
    PAGE_PARAM = {
        'app_name':APP_NAME,
        'page_title': 'Conference details',
        'sub_title': 'Listing',
        'formset': formset,
        'conferences':conferences,
    }
    PP = dict(PAGE_PARAM, **BOOTSTRAP_PARAM)
    return render(request=request, template_name='confreg/conferences-manage.html', context=PP)

def manage_conference(request, conference_id=None):
    if request.method=='POST':
        conference = ConferenceForm()
        if pk=='0':
            form = ConferenceForm(request.POST)
        else:
            conference = get_object_or_404(Conference, conference_id=conference_id)
            # TO-DO: Check if the key exists before proceed
            form = ConferenceForm(request.POST, instance=conference)
        if form.is_valid() and form_saved_or_updated(form, conference, request.user):
            return redirect(
                 'manage_conference'
            )
        else:
            return HttpResponse('Invalid form detected')
    else:
        PAGE_PARAM = {
            'app_name':APP_NAME,
            'page_title': 'Conference details',
            'sub_title': 'Listing',
            'conference': Conference.objects.get(pk=pk),
        }
        PP = dict(PAGE_PARAM, **BOOTSTRAP_PARAM)
        return render(request, 'confreg/conferences-manage.html', PP)


def conference_registrant_list(request):
    obj = Registrant.objects.all()
    persons = Person.objects.all()
    conferences = Conference.objects.all()
    formset = PersonForm()
    PAGE_PARAM = {
        'app_name':APP_NAME,
        'page_title': 'Conference details',
        'sub_title': 'Listing',
        'parent_id': 2,
        'formset':formset,
        'conferences': conferences,
        'persons': persons,
        'obj': obj,
    }
    PP = dict(PAGE_PARAM, **BOOTSTRAP_PARAM)
    return render(request, 'confreg/registrant-list.html', PP)


def conference_registrant_create(request):
    if request.method=='POST':
        person = PersonForm()
        form = PersonForm(request.POST)
        print()
        print(form)
        print (form.is_valid())
        if form.is_valid():
            form.save()
    return redirect('conference_registrant_list')

def conference_accommodation(request):
    conference_id=1

    obj = Registrant.objects.filter(conference_id=conference_id)
    rooms = Accommodation.objects.filter(conference_id=conference_id)
    formset = AccommodationRoomOccupantForm()
    #AccommodationRoomOccupantForm
    PAGE_PARAM = {
        'app_name':APP_NAME,
        'page_title': 'Accommodation details',
        'sub_title': 'Listing',
        'parent_id': 1,
        'formset':formset,
        'rooms': rooms,
        'obj': obj,
    }
    PP = dict(PAGE_PARAM, **BOOTSTRAP_PARAM)
    return render(request, 'confreg/conf-accommodation.html', PP)


def form_saved_or_updated(form, item, action_by):
    try:
        item = form.save(commit=False)
        #item.created_by = action_by
        #item.modified_date = timezone.now()
        item.save()
        return True
    except:
        return False
