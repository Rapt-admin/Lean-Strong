from django.shortcuts import redirect, render
from home.models import *


def adminUserDash(request):
    return render(request,'admin-dashboard.html')

def allUsers(request):
    return render(request,'admin-all-users.html')

def manageCampaigns(request):
    return render(request,'admin-campaigns.html')

def manageBlogs(request):
    return render(request,'admin-blogs.html')

def manageCompanyContatcInfo(request):
    return render(request,'admin-company-contact.html')

def manageFaq(request):
    return render(request,'admin-faq.html')

def manageSubscriptionPlans(request):
    return render(request,'admin-subscription-plans.html')

def manageUsersForRenewal(request):
    return render(request,'admin-users-for-renewal.html')

def manageDietitianActiveSession(request):
    return render(request,'admin-dietition-active-sessions.html')

def manageDietitianInactiveSession(request):
    return render(request,'admin-dietition-inactive-sessions.html')

def manageDietitianMissedSession(request):
    return render(request,'admin-dietition-missed-sessions.html')

def manageFitnessCoachActiveSession(request):
    return render(request,'admin-fitnessCoach-active-sessions.html')

def manageFitnessCoachInactiveSession(request):
    return render(request,'admin-fitnessCoach-inactive-sessions.html')

def manageFitnessCoachMissedSession(request):
    return render(request,'admin-fitnessCoach-missed-sessions.html')

def manageEnquiries(request):
    return render(request,'admin-enquiries.html')

def manageAdminUserProfile(request):
    return render(request,'admin-users-profile.html')
