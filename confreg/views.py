from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, get_user_model, logout

from .models import Conference, Person, Registrant, \
    Accommodation, AccommodationRoomOccupant
from .forms import ConferenceForm, PersonForm, RegistrantForm, \
    AccommodationForm, AccommodationRoomOccupantForm

APP_PARAMS = {
        'app_name'                : 'Enjoy God!',
        'fa_class_logo'           : 'fa fa-cutlery',
        'copyright_by'            : '© Church of God (Singapore) 2017',

        'bootstrap_min_url'       : 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'bootstrap_min_integrity' : 'sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
        'bootstrap_crossorigin'   : 'anonymous',
    }
def create_account(request):
    #do create account
    username = request.POST.get('email')
    password = request.POST.get('password')
    email    = request.POST.get('email')
    print (username,password,email)

    PAGE_PARAM = {
            'page_title':'Your details',
        }
    PP = dict(PAGE_PARAM, **APP_PARAMS)
    return render(request, 'confreg/create-account.html', PP)

def login(request):
    print(request.user)

    user_is_authenticated = False
    if request.user is not None and request.user.is_authenticated:
        user_is_authenticated = True

        print ('user is valid')
    else:
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_authenticated:
            user_is_authenticated = True
    
    print(request.user)
    
    if user_is_authenticated:
        # need to create a session to keep the user alive!!!

        #request.user
        PAGE_PARAM = {
                'page_title':'Home',
            }
        PP = dict(PAGE_PARAM, **APP_PARAMS)
        return render(request, 'confreg/account-registrant-list.html', PP,)
    else:
        applicants = Person.objects.order_by('created_date')
        PAGE_PARAM = {
                'login_status': 'failed', 
            }

        PP = dict(PAGE_PARAM, **APP_PARAMS)
        return render(request, 'confreg/login.html', PP)

def log_me_out(request):
    logout(request)
    page_title = 'Logout'
    PAGE_PARAM = {
            'page_title': page_title,
        }
    PP = dict(PAGE_PARAM, **APP_PARAMS)
    return render(request, 'confreg/login.html', PP)
def account_registrant_list(request):
    page_title = 'Persons whom you have registered for'
    PAGE_PARAM = {
            'page_title': page_title,
        }
    PP = dict(PAGE_PARAM, **APP_PARAMS)
    return render(request, 'confreg/account-registrant-list.html', PP)

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
        
        'page_title': 'Conference details',
        'sub_title': 'Listing',
        'formset': formset,
        'conferences':conferences,
    }
    PP = dict(PAGE_PARAM, **APP_PARAMS)
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
            return HttpResponse('Invalid form detected -- check out where!!')
    else:
        PAGE_PARAM = {
            
            'page_title': 'Conference details',
            'sub_title': 'Listing',
            'conference': Conference.objects.get(pk=pk),
        }
        PP = dict(PAGE_PARAM, **APP_PARAMS)
        return render(request, 'confreg/conferences-manage.html', PP)


def conference_registrant_list(request):
    obj = Registrant.objects.all()
    persons = Person.objects.all()
    conferences = Conference.objects.all()
    formset = PersonForm()
    PAGE_PARAM = {
        
        'page_title': 'Conference details',
        'sub_title': 'Listing',
        'parent_id': 2,
        'formset':formset,
        'conferences': conferences,
        'persons': persons,
        'obj': obj,
    }
    PP = dict(PAGE_PARAM, **APP_PARAMS)
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
        
        'page_title': 'Accommodation details',
        'sub_title': 'Listing',
        'parent_id': 1,
        'formset':formset,
        'rooms': rooms,
        'obj': obj,
    }
    PP = dict(PAGE_PARAM, **APP_PARAMS)
    return render(request, 'confreg/conf-accommodation.html', PP)

def registrant_accommodation(request):
    conference_id=1

    obj = Registrant.objects.filter(conference_id=conference_id)
    rooms = Accommodation.objects.filter(conference_id=conference_id)
    formset = AccommodationRoomOccupantForm()
    #AccommodationRoomOccupantForm
    PAGE_PARAM = {
        
        'page_title': 'Accommodation details',
        'sub_title': 'Listing',
        'parent_id': 1,
        'formset':formset,
        'rooms': rooms,
        'obj': obj,
    }
    PP = dict(PAGE_PARAM, **APP_PARAMS)
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
def reports(request,report_name=None):
    if report_name is not None:
        PAGE_PARAM = {
                'page_title': report_name,
                'report_name': report_name,
            }
        PP = dict(PAGE_PARAM, **APP_PARAMS)

        if report_name=='conference_registrant_list':
            conferences = Conference.objects.all().order_by('-id')
            if conferences.count() > 0 :#what if there is no record??
                conference_id_selected = request.POST.get('report_filter_conference', conferences.values('id')[:1])
                conference = Conference.objects.get(pk=conference_id_selected)
                obj = Registrant.objects.filter(conference_id=conference_id_selected)
                PP = dict(
                    {
                        'conferences': conferences,
                        'conference': conference,
                        'obj': obj,
                    }
                    , **PP)
            
        return render(request, 'confreg/reports.html', PP)
    else:
        return HttpResponse('Invalid form detected -- check out where!!')