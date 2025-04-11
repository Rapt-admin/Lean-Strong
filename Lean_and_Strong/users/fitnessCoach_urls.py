from django.contrib import admin
from django.urls import path
from home.fitnessCoachViews import *

urlpatterns = [
      
    path('',fcDash,name='fcDash'),  
    path('fcts',fcTodaySession,name='fcTodaySession'),  
    path('fccs',fcCompletedSession,name='fcCompletedSession'),  
    path('fcus',fcUpcomingSession,name='fcUpcomingSession'),  
    path('fcms',fcMissedSession,name='fcMissedSession'),  
    path('fccg',fcCreateGroupSession,name='fcCreateGroupSession'),  
    path('fcac',fcAllClients,name='fcAllClients'), 
    path('fcacc',fcActiveClients,name='fcActiveClients'),  
    path('fcuo',fcUserOverview,name='fcUserOverview'),  
    path('fcwp',fcWorkoutPlan,name='fcWorkoutPlan'),  
    path('fccr',fcClientsForRenewal,name='fcClientsForRenewal'),  
    path('fcp',fcProfile,name='fcProfile'),  

]
