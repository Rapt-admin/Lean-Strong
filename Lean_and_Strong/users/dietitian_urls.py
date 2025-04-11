from django.contrib import admin
from django.urls import path
from home.dietitianViews import *

urlpatterns = [
      
    path('',dtDash,name='dtDash'),
    path('dts/',dtTodaySession,name='dtTodaySession'),
    path('dus',dtUpcomingSession,name='dtUpcomingSession'),
    path('dcs',dtCompletedSession,name='dtCompletedSession'),
    path('dms',dtMissedSession,name='dtMissedSession'),
    path('dac',dtAllClients,name='dtAllClients'),
    path('dacc',dtActiveClients,name='dtActiveClients'),
    path('dal',dtAllLeads,name='dtAllLeads'),
    path('dcl',dtConvertedLeads,name='dtConvertedLeads'),
    path('dcr',dtClientsForRenewal,name='dtClientsForRenewal'),
    path('dp',dtProfile,name='dtProfile'),
    

]
