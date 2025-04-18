# Generated by Django 5.0.6 on 2024-08-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_signin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDietPlan',
            fields=[
                ('User_diet_plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('Diet_name', models.CharField(max_length=100)),
                ('Diet_suggested_by', models.CharField(max_length=100)),
                ('Diet_start_date', models.DateField()),
                ('Diet_end_date', models.DateField()),
                ('status', models.CharField(default='Active', max_length=50)),
            ],
            options={
                'db_table': 'user_diet_plans',
                'managed': False,
            },
        ),
    ]
