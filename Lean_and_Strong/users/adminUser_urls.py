from django.contrib import admin
from django.urls import path
from home.adminUserViews import *

urlpatterns = [
      
    path('',adminUserDash,name='adminUserDash'),
    path('aau',allUsers,name='allUsers'),
    path('amc',manageCampaigns,name='manageCampaigns'),
    path('amb',manageBlogs,name='manageBlogs'),
    path('amcc',manageCompanyContatcInfo,name='manageCompanyContatcInfo'),
    path('af',manageFaq,name='manageFaq'),
    path('amsp',manageSubscriptionPlans,name='manageSubscriptionPlans'),
    path('amur',manageUsersForRenewal,name='manageUsersForRenewal'),
    path('amdas',manageDietitianActiveSession,name='manageDietitianActiveSession'),
    path('amdis',manageDietitianInactiveSession,name='manageDietitianInactiveSession'),
    path('amdms',manageDietitianMissedSession,name='manageDietitianMissedSession'),
    path('amfas',manageFitnessCoachActiveSession,name='manageFitnessCoachActiveSession'),
    path('amfis',manageFitnessCoachInactiveSession,name='manageFitnessCoachInactiveSession'),
    path('amfms',manageFitnessCoachMissedSession,name='manageFitnessCoachMissedSession'),
    path('ame',manageEnquiries,name='manageEnquiries'),
    path('amup',manageAdminUserProfile,name='manageAdminUserProfile'),  

    

]
