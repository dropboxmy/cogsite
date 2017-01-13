from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^(?P<conference_id>[0-9]+)/$', views.manage_conference, name='manage_conference'),

#(?P<conference_id>[0-9]+)/
    url(r'^registrant/$', views.conference_registrant_list, name='conference_registrant_list'),
    url(r'^registrant/create/$', views.conference_registrant_create, name='conference_registrant_create'),

    url(r'^accommodation/$', views.conference_accommodation, name='conference_accommodation'),

#conference_accommodation
]
