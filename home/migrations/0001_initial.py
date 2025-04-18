# Generated by Django 5.0.6 on 2024-06-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyContactDetails',
            fields=[
                ('company_contact_detail_id', models.AutoField(db_column='Company_contact_detail_id', primary_key=True, serialize=False)),
                ('branch_name', models.CharField(blank=True, db_column='branch_name', max_length=45, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=45, null=True)),
                ('phone_number', models.IntegerField(blank=True, db_column='Phone_number', null=True)),
                ('mobile_number', models.IntegerField(blank=True, db_column='Mobile_number', null=True)),
                ('website', models.CharField(blank=True, db_column='Website', max_length=45, null=True)),
                ('created_on', models.DateTimeField(blank=True, db_column='Created_on', null=True)),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=5, null=True)),
            ],
            options={
                'db_table': 'company_contact_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conntest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'conntest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('contact_us_id', models.AutoField(db_column='Contact_us_id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100, null=True)),
                ('surname', models.CharField(blank=True, db_column='Surname', max_length=45, null=True)),
                ('mobile_number', models.CharField(blank=True, db_column='Mobile_number', max_length=100, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=100, null=True)),
                ('enquired_about', models.CharField(blank=True, db_column='Enquired_about', max_length=500, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=45, null=True)),
                ('request_source', models.CharField(blank=True, db_column='Request_source', max_length=45, null=True)),
                ('created_date', models.DateTimeField(blank=True, db_column='Created_date', null=True)),
            ],
            options={
                'db_table': 'contact_us',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForgotPassword',
            fields=[
                ('forgot_password_id', models.IntegerField(db_column='Forgot_password_id', primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, db_column='User_id', null=True)),
                ('email_sent_to', models.CharField(blank=True, db_column='Email_sent_to', max_length=100, null=True)),
                ('created_date', models.DateTimeField(blank=True, db_column='Created_date', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=45, null=True)),
                ('password_updated_date', models.DateTimeField(blank=True, db_column='Password_Updated_Date', null=True)),
                ('auth_code', models.CharField(blank=True, db_column='Auth_code', max_length=100, null=True)),
            ],
            options={
                'db_table': 'forgot_password',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('subscription_plan_id', models.AutoField(db_column='Subscription_plan_id', primary_key=True, serialize=False)),
                ('plan_name', models.CharField(db_column='Plan_name', max_length=45)),
                ('created_on', models.DateTimeField(db_column='Created_on')),
                ('delete_ind', models.CharField(db_column='Delete_ind', max_length=5)),
            ],
            options={
                'db_table': 'subscription_plan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlanFeatures',
            fields=[
                ('subscription_plan_feature_id', models.AutoField(primary_key=True, serialize=False)),
                ('feature_name', models.CharField(db_column='Feature_name', max_length=45)),
                ('feature_description', models.CharField(blank=True, db_column='Feature_description', max_length=45, null=True)),
                ('created_on', models.DateTimeField(db_column='Created_on')),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=5, null=True)),
                ('subscription_plan_id', models.IntegerField()),
            ],
            options={
                'db_table': 'subscription_plan_features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlanPricing',
            fields=[
                ('subscription_plan_pricing', models.AutoField(primary_key=True, serialize=False)),
                ('plan_duration', models.CharField(db_column='Plan_duration', max_length=45)),
                ('mrp', models.IntegerField(db_column='MRP')),
                ('discounted_price', models.IntegerField(db_column='Discounted_price')),
                ('created_on', models.DateTimeField(db_column='Created_on')),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=5, null=True)),
            ],
            options={
                'db_table': 'subscription_plan_pricing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlanSubFeature',
            fields=[
                ('subscription_plan_sub_feature_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_feature_name', models.CharField(db_column='Sub_feature_name', max_length=45)),
                ('sub_feature_description', models.CharField(blank=True, db_column='Sub_feature_description', max_length=45, null=True)),
                ('created_on', models.DateTimeField(db_column='Created_on')),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=45, null=True)),
            ],
            options={
                'db_table': 'subscription_plan_sub_feature',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(db_column='User_id', db_comment='\t\t\t\t', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='Firstname', max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, db_column='Lastname', max_length=100, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=1000, null=True)),
                ('mobile_number', models.CharField(blank=True, db_column='Mobile_number', max_length=100, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=100, null=True)),
                ('created_date', models.DateTimeField(blank=True, db_column='Created_date', null=True)),
                ('modified_date', models.DateTimeField(blank=True, db_column='Modified_date', null=True)),
                ('unique_id', models.CharField(blank=True, db_column='Unique_ID', max_length=100, null=True)),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=45, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAccessibleFeatures',
            fields=[
                ('user_accessible_feature_id', models.AutoField(db_column='User_Accessible_Feature_id', primary_key=True, serialize=False)),
                ('feature_name', models.CharField(db_column='Feature_name', max_length=45)),
                ('feature_desc', models.CharField(blank=True, db_column='Feature_desc', max_length=45, null=True)),
                ('created_on', models.DateTimeField(blank=True, db_column='Created_on', null=True)),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=5, null=True)),
            ],
            options={
                'db_table': 'user_accessible_features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserSubscriptions',
            fields=[
                ('user_subscription_id', models.AutoField(db_column='User_subscription_id', primary_key=True, serialize=False)),
                ('subscription_plan_id', models.IntegerField(db_column='Subscription_plan_id')),
                ('created_on', models.DateTimeField(db_column='Created_on')),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=5, null=True)),
                ('start_date', models.DateTimeField(blank=True, db_column='Start_date', null=True)),
                ('end_date', models.DateTimeField(blank=True, db_column='End_Date', null=True)),
            ],
            options={
                'db_table': 'user_subscriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('user_type_id', models.AutoField(db_column='User_type_id', primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, db_column='Role', max_length=45, null=True)),
                ('delete_ind', models.CharField(blank=True, db_column='Delete_ind', max_length=45, null=True)),
            ],
            options={
                'db_table': 'user_type',
                'managed': False,
            },
        ),
    ]
