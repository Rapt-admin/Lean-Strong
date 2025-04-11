from django.contrib import admin
from django.urls import path
from home.userViews import *

urlpatterns = [

    path('',dashboard,name='dashboard'),
    path('pser/',purchaseService,name='purchaseService'),
    path('upser/',upgradeService,name='upgradeService'),
    path('subHist/',subscriptionHistory,name='subscriptionHistory'),
    path('renewServ/',renewService,name='renewService'),
    path('audCallNut/',appointmentCallwithNutritionist,name='appointmentCallwithNutritionist'),
    path('audCallFC/',appointmentCallWithFitnessCoach,name='appointmentCallWithFitnessCoach'),
    path('toSess/',todaySession,name='todaySession'),
    path('upSess/',upcomingSession,name='upcomingSession'),
    path('compSess/',completedSession,name='completedSession'),
    path('dp/',dietPlan,name='dietPlan'),
    path('wp/',workoutPlan,name='workoutPlan'),
    path('showCamp/',showCampaigns,name='showCampaigns'),
    path('userRecp/',userRecipes,name='userRecipes'),
    path('userNoti/',userNotifications,name='userNotifications'),
    path('offers/',offers,name='offers'),
    path('userPro/',userProfile,name='userProfile'),
    path('ult/',userLifeTracker,name='userLifeTracker'),
    path('uht/',userHealthTracker,name='userHealthTracker'),
    path('ubmu/',userBodyMeasurementUpdate,name='userBodyMeasurementUpdate'),
    path('bgp/',bookGroupSession,name='bookGroupSession'),

    path('downLoadDietPlan/<int:userDietPLanId>/', downLoadDietPlan, name='downLoadDietPlan'),
]
