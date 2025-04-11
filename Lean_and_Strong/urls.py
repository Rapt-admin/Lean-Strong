"""
URL configuration for Lean_and_Strong project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.views import *
from home.userViews import *
from home.dietitianViews import *
from home.fitnessCoachViews import *
from home.adminUserViews import *
from home.entities.social_media.GoogleAPIEntity import  *
from home.entities.social_media.FacebookAPIEntity import  *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',show,name="index"),
    path('about',about_us,name="about"),
    path('blog-single/', blog_single, name='blog-single'),
    path('blogs/', blogs, name='blogs'),
    path('bmr/', bmr, name='bmr'),
    path('campaign-1/', campaign_1, name='campaign-1'),
    path('campaign-2/', campaign_2, name='campaign-2'),
    path('campaign-3/', campaign_3, name='campaign-3'),
    path('campaign-4/', campaign_4, name='campaign-4'),
    path('campaigns/', campaigns, name='campaigns'),
    path('cart/', cart, name='cart'),
    path('faq/', faq, name='faq'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('plan&pricing/', planpricing, name='plan&pricing'),
    path('privacy/', privacy, name='privacy'),
    path('profile/', profile, name='profile'),
    path('recipe-1/', recipe_1, name='recipe-1'),
    path('recipe-2/', recipe_2, name='recipe-2'),
    path('recipe-3/', recipe_3, name='recipe-3'),
    path('recipe-4/', recipe_4, name='recipe-4'),
    path('recipes/', recipes, name='recipes'),
    path('terms/', terms, name='terms'),
    path('testimonials/', testimonials, name='testimonials'),
    path('whr/', whr, name='whr'),
    path('contact/', contact_us, name='contact'),
    path('contextform',contextform,name="contextform"),
    path('signin/',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('google-login/', GoogleLoginRedirectApi.as_view(), name='google-login'),
    path('socialAccLogin/', socialAccLogin, name='socialAccLogin'),
    path('google-callback/', GoogleCallbackApi.as_view(), name='google-callback'),
    path('facebook/login/', FacebookLoginRedirectApi.as_view(), name='facebook-login'),
    path('facebook/callback/', FacebookLoginApi.as_view(), name='facebook-callback'),

    path('ui/', include('Lean_and_Strong.users.user_urls')),
    path('au/', include('Lean_and_Strong.users.adminUser_urls')),
    path('dt/', include('Lean_and_Strong.users.dietitian_urls')),
    path('fc/', include('Lean_and_Strong.users.fitnessCoach_urls')),
    

]
