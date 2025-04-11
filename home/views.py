from django.shortcuts import redirect, render
from home.models import *
from home.entities.contact_us_form import ContactUsForm
from django.contrib import messages
from django.forms.models import model_to_dict
from django.http import JsonResponse
#from django.core import serializers
import json
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from home.entities.constants import Constants

from django.views import View
from rest_framework.response import Response
from rest_framework import status

from Lean_and_Strong.settings import env
from home.entities.SignupForm import SignupForm
import logging

####
# Create your views here.
def show(request):
  logger = logging.getLogger()
  logger.info("Welcome to Lean and strong")
  return render(request,'index.html')  

def about_us(request):
  return render(request,'about.html')  

def blog_single(request):
    return render(request,'blog-single.html')

def blogs(request):
    return render(request,'blogs.html')

def bmr(request):
    return render(request,'bmr.html')

def campaign_1(request):
    return render(request,'campaign-1.html')

def campaign_2(request):
    return render(request,'campaign-2.html')


def campaign_3(request):
    return render(request,'campaign-3.html')


def campaign_4(request):
    return render(request,'campaign-4.html')


def campaigns(request):
    return render(request,'campaigns.html')


def cart(request):
    return render(request,'cart.html')


def faq(request):
    return render(request,'faq.html')

def forgot_password(request):
    return render(request,'forgort-password.html')

def privacy(request):
    return render(request,'privacy.html')

def profile(request):
    return render(request,'profile.html')

def recipe_1(request):
    return render(request,'recipe-1.html')

def recipe_2(request):
    return render(request,'recipe-2.html')

def recipe_3(request):
    return render(request,'recipe-3.html')

def recipe_4(request):
    return render(request,'recipe-4.html')

def recipes(request):
    return render(request,'recipes.html')

def terms(request):
    return render(request,'terms.html')

def testimonials(request):
    return render(request,'testimonials.html')

def whr(request):
    return render(request,'whr.html')

def contact_us(request):
    return render(request,'contact.html')


# @login_required
def contact_us(request):
    print(request.method)
    if request.method == "POST":

        contactUsFormData = ContactUsForm(request.POST)

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        enquired_about = request.POST.get('enquired_about')
        status = "PENDING"

        print("name-----"+name+"---surname---"+surname+"---email----"+email+"---mobileNumber----"+mobile_number+"---Message---"+enquired_about)

        if contactUsFormData.is_valid():

            # Create a new contact instance and save it to the database
            user_contact = ContactUs.objects.create(
                name=name,
                surname=surname,
                email=email,
                mobile_number=mobile_number,
                enquired_about=enquired_about,
                status=status,
            )
            messages.success(request, 'We appreciate you reaching out. Our team will be in touch with you shortly')
            return render(request, 'contact-inner.html')
        else:

         # redirect back to the user page with errors
         print("Please enter valid data")
         return render(request, 'contact-inner.html', {'contactUsForm':contactUsFormData})
      
    else:
            #companyContactDetailsData = CompanyContactDetails.objects.exclude(address='198 West 21th Street, Pune - 400006, Maharashtra')
            companyContactDetailsData = CompanyContactDetails.objects.exclude(delete_ind = 1)
           # companyContactDetailsData.toJson()
            #print(companyContactDetailsData.first().address)
            companyContactDetailsData_Dic = {
                "companyContactDetailsData": companyContactDetailsData
            }
            return render(request, 'contact.html', companyContactDetailsData_Dic)



def planpricing(request):

            features_name = SubscriptionPlanFeatures.objects.all()
            features_mapping = SubscriptionPlanFeatureDetails.objects.all()       
            subfeatures = SubscriptionPlanSubFeature.objects.all()
            subfeature_ids = set(subfeatures.values_list('subscription_plan_feature_id', flat=True))
            subfeatures_mapping = SubscriptionPlanSubFeatureDetails.objects.all()
   
            # logger = logging.getLogger(__name__)
            # logger.debug("organized_subfeature: %s", dict(organized_subfeatures))
            print(subfeature_ids)
            # pprint.pprint(subfeature_ids)

            # Prepare the context for the response
            # print("test feature_name------")
            # print(features_name.first().feature_name)
            
            context = {
                "list_of_features": features_name,
                "list_of_features_mapping": features_mapping,
                "list_of_subfeatures": subfeatures,
                "listofsubfeaturesmapping": subfeatures_mapping,
                'subfeature_ids': subfeature_ids,
                "testFeatureNameData": features_name.first().feature_name if features_name  else "test"
                
            }
            
            return render(request,'plan&pricing.html',context)



def contextform(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            duration = request.POST.get('plan_duration')
            essential = SubscriptionPlanPricing.objects.filter(plan_duration=duration, subscription_plan_id=1).first()
            accelerate = SubscriptionPlanPricing.objects.filter(plan_duration=duration, subscription_plan_id=2).first()
            ultimate = SubscriptionPlanPricing.objects.filter(plan_duration=duration, subscription_plan_id=3).first()
            context = {
                        "status": 200,
                        "message": "Data retrieved successfully.",
                        "essential": model_to_dict(essential) if essential else None,
                        "accelerate": model_to_dict(accelerate) if accelerate else None,
                        "ultimate": model_to_dict(ultimate) if ultimate else None,

                    }
           
            return JsonResponse(context)
    else:
        return render(request, 'plan&pricing.html', context)

def signin(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate using the custom backend
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            # request.session['user'] = user
            
            return signinRedirect(request,user)
            
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'signin.html')

def socialAccLogin(request):
    print(request.GET.get('name'))
    print(request.GET.get('email'))
    
    user_info = {
        'name': request.GET.get('name'),
        'email': request.GET.get('email'),
        'loginVia': request.GET.get('loginVia')
    }
    username = user_info['name']
    user_email = user_info['email']
    loginVia = user_info['loginVia']
    user = User.objects.filter(email=user_email).first()
    if not user:
        print("User doesn't exist")
        user_type_id = env('ROLE_USER')
         # Create the user
        user = User.objects.create(
            firstname=username.split(" ")[0] if username else "default",
            lastname=username.split(" ")[1] if username else "",
            email=user_email,
            user_type_id=user_type_id,
            login_via = loginVia
        )
    return signinRedirect(request, user)
    
def signinRedirect(request, user):
    user_data={ 
        "user_id":user.user_id,
        "firstname":user.firstname ,
        "lastname":user.lastname ,
        "mobile_number":user.mobile_number,
        "email":user.email
    }
    request.session['user_data'] = user_data
    print("@@@@@@@@@@@@",user_data)
    finalPageURL = 'dashboard'
    userTypeRole = UserType.objects.filter(user_type_id=user.user_type_id).first().role
    print("userTypeRole:"+userTypeRole)
    request.session['userTypeRole'] = userTypeRole
    if userTypeRole:
        if userTypeRole == Constants.ADMIN or userTypeRole == Constants.MANAGER :
            finalPageURL = "adminUserDash"
        elif userTypeRole == Constants.DIETITIAN :
            finalPageURL = "dtDash"
        elif userTypeRole == Constants.FITNESS_COACH :
            finalPageURL = "fcDash"  
    else:
        print("User Type doesn't exist")
        finalPageURL = 'index'
    
    return redirect(finalPageURL)


from django.contrib.auth.hashers import make_password
from .models import User
from django.core.exceptions import ValidationError

def signup(request):
    if request.method == "POST":
        signupFormData = SignupForm(request.POST)
        
        # first_name = request.POST['username']
        # password = request.POST['password']
        # confirm_password = request.POST['confirm_password']
        # email_address = request.POST['email']
# 
        if signupFormData.is_valid():
            first_name = signupFormData.cleaned_data.get('firstname')
            last_name = signupFormData.cleaned_data.get('lastname')
            password = signupFormData.cleaned_data.get('password')
            confirm_password = request.POST.get('confirm_password')
            mobile_number = signupFormData.cleaned_data.get('mobile_number')
            email_address = signupFormData.cleaned_data.get('email')
            user_type = signupFormData.cleaned_data.get('user_type')   
#   
            # Check if passwords match
            if password != confirm_password:
                signupFormData.add_error('password', 'Passwords do not match')
                return render(request, "signup.html", {'signupForm': signupFormData, 'error': "Passwords do not match"})

            # Check if email already exists
            if User.objects.filter(email=email_address).exists():
                signupFormData.add_error('email', 'Email already exists')
                return render(request, "signup.html", {'signupForm': signupFormData, 'error': "Email already exists"})

            # Hash the password
            hashed_password = make_password(password)
            
            # Hardcoded user type ID
            user_type_id = env('ROLE_USER')  # Ensure this ID exists in your UserType table

            try:
                # Create the user
                User.objects.create(
                    firstname=first_name,
                    lastname=last_name,
                    email=email_address,
                    mobile_number=mobile_number,
                    password=hashed_password,
                    user_type_id=user_type_id
                )
            except ValidationError as e:
                return render(request, "signup.html", {'error': str(e)})
            
            messages.success(request, 'Your account has been created successfully.')
            return render(request, 'signup.html')

            return redirect('index')
        else:
            print(signupFormData.errors)
            # signupFormData = SignupForm()
            return render(request, "signup.html", {'signupForm': signupFormData})
    else:
        signupFormData = SignupForm()
        return render(request, "signup.html", {'signupForm': signupFormData})


def logout(request):
    auth.logout(request)
    #for sesskey in request.session.keys():
   #     del request.session[sesskey]
    #auth.logout(request)
    return render(request, "index.html")

