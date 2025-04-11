from django.shortcuts import redirect, render
from home.models import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from xhtml2pdf.files import pisaFileObject
from xhtml2pdf import pisa, default
from xhtml2pdf.default import DEFAULT_CSS

import logging
logger = logging.getLogger()


def dashboard(request):
    user_details = request.session['user_data']
    user_id = user_details["user_id"]
    userActiveSubscription =  UserSubscriptions.objects.filter(user_id=user_id).exclude(delete_ind = 1)
    userSubscriptionHistory =  UserSubscriptions.objects.filter(user_id=user_id)
    logger.info("userActiveSubscription:")
    logger.info(userActiveSubscription.query)
    havingActiveSubscriptionPlan  = "Yes" if userActiveSubscription else "No"
    logger.info("havingActiveSubscriptionPlan:"+havingActiveSubscriptionPlan)
    userSubscriptionDetails = {
        "havingActiveSubscriptionPlan" : havingActiveSubscriptionPlan,
        "userSubscriptionHistory" : userSubscriptionHistory
    }

    redirectURL = 'userDashboard.html'
    if(havingActiveSubscriptionPlan  == "No"):
        redirectURL = "purchase-services.html"
    
    return render(request, redirectURL, userSubscriptionDetails)


def purchaseService(request):
    return render(request,'purchase-services.html')

def upgradeService(request):
    return render(request,'upgrade-services.html')

def subscriptionHistory(request):
    return render(request,'subscription-history.html')

def renewService(request):
    return render(request,'renew-service.html')

def appointmentCallwithNutritionist(request):
    return render(request,'audiocall-nutritionist.html')

def appointmentCallWithFitnessCoach(request):
    return render(request,'audiocall-fitnesscoach.html')

def todaySession(request):
    return render(request,'todays-sessions.html')

def upcomingSession(request):
    return render(request,'upcoming-sessions.html')

def completedSession(request):
    return render(request,'completed-sessions.html')

def bookGroupSession(request):
    return render(request,'book-group-sessions.html')

def dietPlan(request):
    user_details = request.session['user_data']
    user_id = user_details["user_id"]
    print("Logged in User ID:",user_id)
    diet_plans = UserDietPlan.objects.filter(user_id=user_id)
    context = {
        'diet_plans': diet_plans
    }
    return render(request,'diet-plan.html',context)

def downLoadDietPlan(request, userDietPLanId):
    print("*****Method called")
    userDietPlan = UserDietPlan.objects.get(pk=userDietPLanId)
    template_path = 'diet-plan-pdf.html'
    dietPlanDetails = {
        'userDietPlan': userDietPlan
    }
    return render(request,'diet-plan-pdf.html',dietPlanDetails)

def workoutPlan(request):
    return render(request,'workout-plan.html')

def showCampaigns(request):
    return render(request,'campaigns.html')

def userRecipes(request):
    return render(request,'add-recipes.html')

def userNotifications(request):
    return render(request,'notifications.html')

def offers(request):
    return render(request,'offers.html')

def userProfile(request):
    return render(request,'users-profile.html')

def userLifeTracker(request):
    return render(request,'lifestyle-tracker.html')

def userHealthTracker(request):
    return render(request,'health-tracker.html')

def userBodyMeasurementUpdate(request):
    return render(request,'body-measurement-update.html')

def userBodyCompositionAnalysis(request):
    return render(request,'body-composition-analysis.html')
