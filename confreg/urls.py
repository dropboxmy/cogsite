from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.log_me_out, name='log_me_out'),
    url(r'^createaccount/$', views.create_account, name='create_account'),

    url(r'^account/registrants/$', views.account_registrant_list, name='account_registrant_list'),
    

    url(r'^landing/$', views.landing, name='landing'),
    url(r'^(?P<conference_id>[0-9]+)/$', views.manage_conference, name='manage_conference'),

    url(r'^registrant/$', views.conference_registrant_list, name='conference_registrant_list'),
    url(r'^registrant/create/$', views.conference_registrant_create, name='conference_registrant_create'),

    url(r'^accommodation/$', views.conference_accommodation, name='conference_accommodation'),
    url(r'^registrant/accommodation/$', views.registrant_accommodation, name='registrant_accommodation'),

    url(r'^reports/(?P<report_name>[\w-]+)/$', views.reports, name='reports'),


#conference_accommodation
]
