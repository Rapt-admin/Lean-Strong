from django.shortcuts import redirect, render
from home.models import *


def fcDash(request):
    return render(request,'fc_dashboard.html')

def fcTodaySession(request):
    return render(request,'fc_todays-sessions.html')

def fcUpcomingSession(request):
    return render(request,'fc_upcoming-sessions.html')

def fcCompletedSession(request):
    return render(request,'fc_completed-sessions.html')

def fcMissedSession(request):
    return render(request,'fc_missed-sessions.html')

def fcCreateGroupSession(request):
    return render(request,'fc_create-group-session')

def fcAllClients(request):
    return render(request,'fc_all-clients.html')

def fcActiveClients(request):
    return render(request,'fc_active-clients.html')

def fcUserOverview(request):
    return render(request,'fc_user-overview.html')

def fcWorkoutPlan(request):
    return render(request,'fc_workout-plan.html')

def fcClientsForRenewal(request):
    return render(request,'fc_renewal-clients.html')

def fcProfile(request):
    return render(request,'fc_users-profile.html')
