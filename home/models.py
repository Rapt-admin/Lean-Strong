from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Blog(models.Model):
    blog_id = models.AutoField(db_column='Blog_id', primary_key=True)  # Field name made lowercase.
    blog_title = models.CharField(db_column='Blog_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blog_description = models.CharField(db_column='Blog_description', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blog'


class Campaigns(models.Model):
    campaign_id = models.AutoField(db_column='Campaign_id', primary_key=True)  # Field name made lowercase.
    campaign_title = models.CharField(db_column='Campaign_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campaign_description = models.CharField(db_column='Campaign_description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    launch_locations = models.CharField(db_column='Launch_locations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    launch_locatons_url = models.CharField(db_column='Launch_locatons_url', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    campaign_run_by = models.CharField(db_column='Campaign_run_by', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campaigns'


class CoachUsers(models.Model):
    coach_users_id = models.AutoField(primary_key=True)
    coach = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='coachusers_user_set', blank=True, null=True)
    coach_type = models.CharField(db_column='Coach_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coach_users'


class CommunicationProvider(models.Model):
    communication_provider_id = models.AutoField(db_column='Communication_provider_id', primary_key=True)  # Field name made lowercase.
    provider_name = models.CharField(db_column='Provider_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    login_username = models.CharField(db_column='Login_username', max_length=45, blank=True, null=True)  # Field name made lowercase.
    login_password = models.CharField(db_column='Login_password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    account_id = models.CharField(db_column='Account_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    api_key = models.CharField(db_column='API_Key', max_length=200, blank=True, null=True)  # Field name made lowercase.
    api_secret = models.CharField(db_column='API_Secret', max_length=45, blank=True, null=True)  # Field name made lowercase.
    communication_type = models.CharField(db_column='Communication_type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    api_url = models.CharField(db_column='API_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    callback_url = models.CharField(db_column='Callback_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    active_provider_ind = models.IntegerField(db_column='Active_provider_ind', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'communication_provider'


class CompanyContactDetails(models.Model):
    company_contact_detail_id = models.AutoField(db_column='Company_contact_detail_id', primary_key=True)  # Field name made lowercase.
    branch_name = models.CharField(db_column='Branch_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.BigIntegerField(db_column='Phone_number', blank=True, null=True)  # Field name made lowercase.
    mobile_number = models.BigIntegerField(db_column='Mobile_number', blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_contact_details'


class Conntest(models.Model):
    a = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conntest'


class ContactUs(models.Model):
    contact_us_id = models.AutoField(db_column='Contact_us_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile_number = models.CharField(db_column='Mobile_number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enquired_about = models.CharField(db_column='Enquired_about', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    request_source = models.CharField(db_column='Request_source', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact_us'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ForgotPassword(models.Model):
    forgot_password_id = models.IntegerField(db_column='Forgot_password_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    email_sent_to = models.CharField(db_column='Email_sent_to', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password_updated_date = models.DateTimeField(db_column='Password_Updated_Date', blank=True, null=True)  # Field name made lowercase.
    auth_code = models.CharField(db_column='Auth_code', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forgot_password'


class GroupSessions(models.Model):
    group_session_id = models.AutoField(db_column='Group_session_id', primary_key=True)  # Field name made lowercase.
    group_session_name = models.CharField(db_column='Group_session_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grooup_session_about = models.CharField(db_column='Grooup_session_about', max_length=500, blank=True, null=True)  # Field name made lowercase.
    group_session_duration = models.IntegerField(db_column='Group_Session_Duration', blank=True, null=True)  # Field name made lowercase.
    group_session_start_date = models.DateField(db_column='Group_Session_start_date', blank=True, null=True)  # Field name made lowercase.
    group_session_start_time = models.TimeField(db_column='Group_Session_start_time', blank=True, null=True)  # Field name made lowercase.
    group_session_end_time = models.TimeField(db_column='Group_Session_end_time', blank=True, null=True)  # Field name made lowercase.
    group_session_created_by = models.IntegerField(db_column='Group_Session_created_by')  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group_sessions'


class Offers(models.Model):
    offer_id = models.AutoField(db_column='Offer_id', primary_key=True)  # Field name made lowercase.
    offer_subject = models.CharField(db_column='Offer_Subject', max_length=50, blank=True, null=True)  # Field name made lowercase.
    offer_detail = models.CharField(db_column='Offer_detail', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    coupon_code = models.CharField(db_column='Coupon_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'offers'


class SubscriptionPlan(models.Model):
    subscription_plan_id = models.AutoField(db_column='Subscription_plan_id', primary_key=True)  # Field name made lowercase.
    plan_name = models.CharField(db_column='Plan_name', max_length=45)  # Field name made lowercase.
    allow_audio_consultation = models.CharField(db_column='Allow_Audio_Consultation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_audio_consultation_with_dietician = models.IntegerField(db_column='Total_audio_consultation_with_dietician', blank=True, null=True)  # Field name made lowercase.
    total_audio_consultation_with_fitnesscoach = models.IntegerField(db_column='Total_audio_consultation_with_fitnessCoach', blank=True, null=True)  # Field name made lowercase.
    allow_video_consultation = models.CharField(db_column='Allow_Video_Consultation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_video_consultation_with_dietician = models.IntegerField(db_column='Total_video_consultation_with_dietician', blank=True, null=True)  # Field name made lowercase.
    total_video_consultation_with_fitnesscoach = models.IntegerField(db_column='Total_video_consultation_with_fitnessCoach', blank=True, null=True)  # Field name made lowercase.
    total_workout_group_sessions = models.IntegerField(db_column='Total_Workout_Group_Sessions', blank=True, null=True)  # Field name made lowercase.
    number_of_diet_plans = models.IntegerField(db_column='Number_Of_Diet_Plans', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_plan'


class SubscriptionPlanFeatureDetails(models.Model):
    subscription_plan_feature_detail_id = models.AutoField(primary_key=True)
    subscription_plan_id = models.IntegerField(blank=True, null=True)
    subscription_plan_feature_id = models.IntegerField(blank=True, null=True)
    numeric_value = models.IntegerField(db_column='Numeric_value', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_plan_feature_details'


class SubscriptionPlanFeatures(models.Model):
    subscription_plan_feature_id = models.AutoField(primary_key=True)
    feature_name = models.CharField(db_column='Feature_name', max_length=200)  # Field name made lowercase.
    feature_description = models.CharField(db_column='Feature_description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isnumeric = models.CharField(db_column='isNumeric', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subs_plan_first_numeric_value = models.IntegerField(db_column='Subs_plan_first_numeric_value', blank=True, null=True)  # Field name made lowercase.
    sub_plan_second_numeric_value = models.IntegerField(db_column='Sub_plan_second_numeric_value', blank=True, null=True)  # Field name made lowercase.
    subs_plan_third_numeric_value = models.IntegerField(db_column='Subs_plan_third_numeric_value', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_plan_features'


class SubscriptionPlanPricing(models.Model):
    subscription_plan_pricing = models.AutoField(primary_key=True)
    plan_duration = models.CharField(db_column='Plan_duration', max_length=45)  # Field name made lowercase.
    mrp = models.IntegerField(db_column='MRP')  # Field name made lowercase.
    discounted_price = models.IntegerField(db_column='Discounted_price')  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    subscription_plan = models.ForeignKey(SubscriptionPlan, models.DO_NOTHING, db_column='Subscription_plan_id')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_plan_pricing'


class SubscriptionPlanSubFeature(models.Model):
    subscription_plan_sub_feature_id = models.AutoField(primary_key=True)
    sub_feature_name = models.CharField(db_column='Sub_feature_name', max_length=150)  # Field name made lowercase.
    sub_feature_description = models.CharField(db_column='Sub_feature_description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    isnumeric = models.CharField(db_column='isNumeric', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subs_plan_third_numeric_value = models.IntegerField(db_column='Subs_plan_third_numeric_value', blank=True, null=True)  # Field name made lowercase.
    subs_plan_second_numeric_value = models.IntegerField(db_column='Subs_plan_second_numeric_value', blank=True, null=True)  # Field name made lowercase.
    subs_plan_first_numeric_value = models.IntegerField(db_column='Subs_plan_first_numeric_value', blank=True, null=True)  # Field name made lowercase.
    is_online_session = models.CharField(db_column='Is_online_session', max_length=5, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subscription_plan_feature = models.ForeignKey(SubscriptionPlanFeatures, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subscription_plan_sub_feature'


class SubscriptionPlanSubFeatureDetails(models.Model):
    subscription_plan_sub_feature_detail_id = models.AutoField(primary_key=True)
    subscription_plan_id = models.IntegerField(blank=True, null=True)
    subscription_plan_sub_feature_id = models.IntegerField(blank=True, null=True)
    numeric_value = models.IntegerField(db_column='Numeric_value', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscription_plan_sub_feature_details'


class CustomUserManager(BaseUserManager):
    def create_user(self,email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        # if username is None:
        #     username = email.split('@')[0]
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.is_active = True 
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    user_id = models.AutoField(db_column='User_id', primary_key=True)
    username=None
    firstname = models.CharField(db_column='Firstname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mobile_number = models.CharField(db_column='Mobile_number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True,unique=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_date', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_date', blank=True, null=True)  # Field name made lowercase.
    unique_id = models.CharField(db_column='Unique_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_type = models.ForeignKey('UserType', models.DO_NOTHING, db_column='User_type_id')  # Field name made lowercase.
    login_via = models.CharField(db_column='Login_via', max_length=45, blank=True, null=True)  # Field name made lowercase.
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
   
    class Meta:
        managed = False
        db_table = 'user'


class UserAccessibleFeatures(models.Model):
    user_accessible_feature_id = models.AutoField(db_column='User_Accessible_Feature_id', primary_key=True)  # Field name made lowercase.
    feature_name = models.CharField(db_column='Feature_name', max_length=45)  # Field name made lowercase.
    feature_desc = models.CharField(db_column='Feature_desc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on', blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_accessible_features'


class UserBodyCompositionAnalysis(models.Model):
    user_body_composition_analysis_id = models.AutoField(db_column='User_Body_Composition_Analysis_id', primary_key=True)  # Field name made lowercase.
    body_fat_percentage = models.CharField(db_column='Body_Fat_percentage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    body_type = models.CharField(db_column='Body_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    basal_metabolic_rate_bmr_field = models.CharField(db_column='Basal_Metabolic_Rate(BMR)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_daily_energy_expenditure = models.CharField(db_column='Total_daily_energy_expenditure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visceral_fat = models.CharField(db_column='Visceral_Fat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fat_mass = models.CharField(db_column='Fat_Mass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=50, blank=True, null=True)  # Field name made lowercase.
    body_mass_index_bmi_field = models.CharField(db_column='Body_Mass_Index(BMI)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    uploaded_medical_report = models.CharField(db_column='Uploaded_Medical_Report', max_length=50, blank=True, null=True)  # Field name made lowercase.
    biological_age = models.CharField(db_column='Biological_Age', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_body_composition_analysis'


class UserBodyMeasurement(models.Model):
    user_body_measurement_id = models.AutoField(db_column='User_Body_Measurement_id', primary_key=True)  # Field name made lowercase.
    neck_size = models.IntegerField(db_column='Neck_size')  # Field name made lowercase.
    chest_size = models.IntegerField(db_column='Chest_size')  # Field name made lowercase.
    shoulder_size = models.IntegerField(db_column='Shoulder_size')  # Field name made lowercase.
    arms_size = models.IntegerField(db_column='Arms_size')  # Field name made lowercase.
    abs_size = models.IntegerField(db_column='Abs_size')  # Field name made lowercase.
    waist_size = models.IntegerField(db_column='Waist_size')  # Field name made lowercase.
    hips_size = models.IntegerField(db_column='Hips_size')  # Field name made lowercase.
    thighs_size = models.IntegerField(db_column='Thighs_size')  # Field name made lowercase.
    calves_size = models.IntegerField(db_column='Calves_size')  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_body_measurement'


class UserDietPlans(models.Model):
    user_diet_plan_id = models.AutoField(db_column='User_diet_plan_id', primary_key=True)  # Field name made lowercase.
    diet_name = models.CharField(db_column='Diet_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    diet_detail = models.CharField(db_column='Diet_detail', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    diet_start_date = models.DateTimeField(db_column='Diet_start_date', blank=True, null=True)  # Field name made lowercase.
    diet_end_date = models.DateTimeField(db_column='Diet_end_date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    diet_validity = models.IntegerField(db_column='Diet_validity', blank=True, null=True)  # Field name made lowercase.
    diet_suggested_by = models.ForeignKey(User, models.DO_NOTHING, db_column='Diet_suggested_by', related_name='userdietplans_diet_suggested_by_set')  # Field name made lowercase.
    early_morning_meal = models.CharField(db_column='Early_morning_meal', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pre_workout_meal = models.CharField(db_column='Pre-workout_meal', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    post_workout_meal = models.CharField(db_column='Post-workout_meal', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    breakfast_meal = models.CharField(max_length=500, blank=True, null=True)
    before_lunch_meal = models.CharField(max_length=500, blank=True, null=True)
    lunch_meal = models.CharField(max_length=500, blank=True, null=True)
    evening_snacks_meal = models.CharField(max_length=500, blank=True, null=True)
    dinner_meal = models.CharField(max_length=500, blank=True, null=True)
    before_bed_meal = models.CharField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_diet_plans'


class UserFitnessDetails(models.Model):
    user_fitness_detail_id = models.AutoField(db_column='User_fitness_detail_id', primary_key=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fitness_goal = models.CharField(db_column='Fitness_goal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    muscle_focus_area = models.CharField(db_column='Muscle_Focus_Area', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.CharField(db_column='Birth_date', max_length=50, blank=True, null=True)  # Field name made lowercase.
    current_weight = models.IntegerField(db_column='Current_weight')  # Field name made lowercase.
    weight_goal = models.IntegerField(db_column='Weight_goal')  # Field name made lowercase.
    current_bmi = models.IntegerField(db_column='Current_BMI')  # Field name made lowercase.
    height_in_cm_field = models.IntegerField(db_column='Height (In cm)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    workout_frequency_per_week = models.IntegerField(db_column='Workout_frequency_per_week')  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_fitness_details'


class UserGroupSessions(models.Model):
    user_group_session_id = models.AutoField(primary_key=True)
    session_about = models.CharField(db_column='Session_about', max_length=50, blank=True, null=True)  # Field name made lowercase.
    session_join_status = models.CharField(db_column='Session_join_status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    session_end_status = models.CharField(db_column='Session_end_status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    group_session = models.ForeignKey(GroupSessions, models.DO_NOTHING, db_column='Group_session_id')  # Field name made lowercase.
    is_rescheduled = models.CharField(db_column='Is_rescheduled', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_session_parent_id = models.IntegerField(db_column='User_session_parent_id', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_group_sessions'


class UserHealthAndLifestyleTracker(models.Model):
    user_health_and_lifestyle_tracker_id = models.AutoField(db_column='User_health_and_lifestyle_tracker_id', primary_key=True)  # Field name made lowercase.
    water_intake_litre_field = models.CharField(db_column='Water_intake(litre)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    daily_sleep_hrs_field = models.CharField(db_column='Daily_sleep(Hrs)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    blood_suagr_reading = models.CharField(db_column='Blood_suagr_reading', max_length=50, blank=True, null=True)  # Field name made lowercase.
    blood_pressure_reading = models.CharField(db_column='Blood_pressure_reading', max_length=50, blank=True, null=True)  # Field name made lowercase.
    total_cholesterol = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_health_and_lifestyle_tracker'


class UserNotification(models.Model):
    user_notification_id = models.AutoField(db_column='User_Notification_id', primary_key=True)  # Field name made lowercase.
    notification_subject = models.CharField(db_column='Notification_Subject', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notification_detail = models.CharField(db_column='Notification_detail', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_notification'


class UserRating(models.Model):
    user_rating_id = models.AutoField(db_column='User_rating_id', primary_key=True)  # Field name made lowercase.
    dietician_or_fitness_coach = models.ForeignKey(User, models.DO_NOTHING, db_column='Dietician_or_Fitness_coach_id')  # Field name made lowercase.
    rating_given_by = models.ForeignKey(User, models.DO_NOTHING, db_column='Rating_given_by', related_name='userrating_rating_given_by_set')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_rating'


class UserRecipes(models.Model):
    user_recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(db_column='Recipe_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipe_ingredients = models.CharField(db_column='Recipe_Ingredients', max_length=45, blank=True, null=True)  # Field name made lowercase.
    recipe_description = models.CharField(db_column='Recipe_description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    recipe_procedure = models.CharField(db_column='Recipe_procedure', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_recipes'


class UserSessions(models.Model):
    user_session_id = models.AutoField(primary_key=True)
    session_about = models.CharField(db_column='Session_about', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    session_date = models.DateField(db_column='Session_date', blank=True, null=True)  # Field name made lowercase.
    session_end_time = models.TimeField(db_column='Session_end_time', blank=True, null=True)  # Field name made lowercase.
    session_start_time = models.TimeField(db_column='Session_start_time', blank=True, null=True)  # Field name made lowercase.
    session_join_status = models.CharField(db_column='Session_join_status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    session_end_status = models.CharField(db_column='Session_end_status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    session_created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='Session_created_by')  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id', related_name='usersessions_user_set')  # Field name made lowercase.
    is_rescheduled = models.CharField(db_column='Is_rescheduled', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_session_parent_id = models.IntegerField(db_column='User_session_parent_id', blank=True, null=True)  # Field name made lowercase.
    session_type = models.CharField(db_column='Session_type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_sessions'


class UserSocialMediaAccounts(models.Model):
    user_social_media_account_id = models.AutoField(db_column='User_social_media_account_id', primary_key=True)  # Field name made lowercase.
    social_media_platform_name = models.CharField(db_column='Social_media_platform_name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_social_media_accounts'


class UserSubscriptions(models.Model):
    user_subscription = models.OneToOneField(SubscriptionPlan, models.DO_NOTHING, db_column='User_subscription_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    subscription_plan_id = models.IntegerField(db_column='Subscription_plan_id')  # Field name made lowercase.
    subscription_plan_start_date = models.DateTimeField(db_column='Subscription_Plan_Start_date', blank=True, null=True)  # Field name made lowercase.
    subscription_plan_end_date = models.DateTimeField(db_column='Subscription_Plan_End_Date', blank=True, null=True)  # Field name made lowercase.
    service_type = models.CharField(db_column='Service_type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parent_user_subscription_id = models.IntegerField(db_column='Parent_user_subscription_id', blank=True, null=True)  # Field name made lowercase.
    plan_cost = models.IntegerField(db_column='Plan_cost', blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    purchased_price = models.IntegerField(db_column='Purchased_price', blank=True, null=True)  # Field name made lowercase.
    tax_amount = models.IntegerField(db_column='Tax_amount', blank=True, null=True)  # Field name made lowercase.
    upgrade_service_deduction_amount = models.IntegerField(db_column='Upgrade_service_deduction_amount', blank=True, null=True)  # Field name made lowercase.
    upgrade_service_charges = models.IntegerField(db_column='Upgrade_service_charges', blank=True, null=True)  # Field name made lowercase.
    payment_via = models.CharField(db_column='Payment_via', max_length=45, blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment_status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    payment_status_remark = models.CharField(db_column='Payment_status_remark', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.
    alloted_audio_consultation_with_dietician = models.IntegerField(db_column='Alloted_audio_consultation_with_dietician', blank=True, null=True)  # Field name made lowercase.
    alloted_video_consultation_with_dietician = models.IntegerField(db_column='Alloted_video_consultation_with_dietician', blank=True, null=True)  # Field name made lowercase.
    alloted_audio_consultation_with_fitness_coach = models.IntegerField(db_column='Alloted_audio_consultation_with_fitness_coach', blank=True, null=True)  # Field name made lowercase.
    alloted_video_consultation_with_fitness_coach = models.IntegerField(db_column='Alloted_video_consultation_with_fitness_coach', blank=True, null=True)  # Field name made lowercase.
    updated_on = models.DateTimeField(db_column='Updated_on', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_subscriptions'


class UserType(models.Model):
    user_type_id = models.AutoField(db_column='User_type_id', primary_key=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_type'


class UserWorkoutPlans(models.Model):
    user_workout_plan_id = models.AutoField(db_column='User_workout_plan_id', primary_key=True)  # Field name made lowercase.
    workout_ids = models.CharField(db_column='Workout_ids', max_length=500)  # Field name made lowercase.
    workout_days = models.CharField(db_column='Workout_days', max_length=500)  # Field name made lowercase.
    suggested_workouts_period = models.CharField(db_column='Suggested_Workouts_Period', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fitness_coach = models.ForeignKey(User, models.DO_NOTHING, db_column='Fitness_coach')  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='userworkoutplans_user_set')
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_workout_plans'


class Workout(models.Model):
    workout_id = models.AutoField(db_column='Workout_id', primary_key=True)  # Field name made lowercase.
    workout_name = models.CharField(max_length=45, blank=True, null=True)
    workout_description = models.CharField(max_length=500, blank=True, null=True)
    workout_type = models.ForeignKey('WorkoutType', models.DO_NOTHING)
    workout_category = models.ForeignKey('WorkoutCategory', models.DO_NOTHING)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workout'


class WorkoutCategory(models.Model):
    workout_category_id = models.AutoField(db_column='Workout_category_id', primary_key=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    workout_category_name = models.CharField(max_length=45, blank=True, null=True)
    workout_category_description = models.CharField(max_length=45, blank=True, null=True)
    workout_type = models.ForeignKey('WorkoutType', models.DO_NOTHING)
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workout_category'


class WorkoutType(models.Model):
    workout_type_id = models.AutoField(primary_key=True)
    workout_type = models.CharField(max_length=45, blank=True, null=True)
    workout_type_desc = models.CharField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(db_column='Created_on')  # Field name made lowercase.
    delete_ind = models.CharField(db_column='Delete_ind', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workout_type'
