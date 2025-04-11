from django.shortcuts import redirect, render
from home.models import *

def dtDash(request):
    return render(request,'dietitian_dashboard.html')

def dtTodaySession(request):
    return render(request,'dietitian_todays-sessions.html')

def dtUpcomingSession(request):
    return render(request,'dietitian_upcoming-sessions.html')

def dtCompletedSession(request):
    return render(request,'dietitian_completed-sessions.html')

def dtMissedSession(request):
    return render(request,'dietitian_missed-sessions.html')

def dtAllClients(request):
    return render(request,'dietitian_all-clients.html')

def dtActiveClients(request):
    return render(request,'dietitian_active-clients.html')

def dtAllLeads(request):
    return render(request,'dietitian_all-leads.html')

def dtConvertedLeads(request):
    return render(request,'dietitian_converted-leads.html')

def dtClientsForRenewal(request):
    return render(request,'dietitian_renewal-clients.html')

def dtProfile(request):
    return render(request,'dietitian_profile.html')



