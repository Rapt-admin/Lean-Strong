# yourapp/templatetags/custom_filters.py
from django import template

from home.models import SubscriptionPlanFeatureDetails, SubscriptionPlanSubFeatureDetails

register = template.Library()

@register.filter
def get_value(organize_subfeatures, feature_id): 
    return organize_subfeatures.get(feature_id,"sub_feature_name")

def get_values(organize_subfeatures, args): 
    feature_id, sub_feature_name = args.split(',')
    return organize_subfeatures.get(feature_id, {}).get(sub_feature_name, None)


@register.filter(name='feature_check')
def feature_check(id, feature_id):
    subscription_plan_ids=[int(id)]
     # Define the subscription_plan_id values you want to check
    
    for plan_id in subscription_plan_ids:
        if SubscriptionPlanFeatureDetails.objects.filter(
                subscription_plan_id=plan_id,
                subscription_plan_feature_id=feature_id
        ).exists():
            return 'True'
    
    return 'False'
     


@register.filter(name='subfeature_check')
def feature_check(id, feature_id):
    subscription_plan_ids=[int(id)]
     # Define the subscription_plan_id values you want to check   
    for plan_id in subscription_plan_ids:
        if SubscriptionPlanSubFeatureDetails.objects.filter(
                subscription_plan_id=plan_id,
                subscription_plan_sub_feature_id=feature_id
        ).exists():
            return 'True'
    
    return 'False'