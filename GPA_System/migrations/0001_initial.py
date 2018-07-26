# Generated by Django 2.0.6 on 2018-07-24 21:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('First_Name', models.CharField(max_length=20, null=True, unique=True)),
                ('Last_Name', models.CharField(max_length=20, null=True, unique=True)),
                ('Middle_Name', models.CharField(max_length=20, null=True, unique=True)),
                ('CSU_ID', models.IntegerField(null=True, unique=True, validators=[django.core.validators.MaxValueValidator(1999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('CSU_Class', models.CharField(choices=[('GHSM', 'Gospel Holiday School Of Ministry'), ('TE', 'Truth Exposition'), ('DC', 'Discipleship Class')], default='GHSM', max_length=4)),
                ('CSU_Position', models.CharField(choices=[('None', 'None'), ('CCL', 'Cell Component Leader'), ('CL', 'Cell Leader'), ('TL', 'Tissue Leader')], default='None', max_length=4)),
                ('CSU_Ministry', models.CharField(choices=[('None', 'None'), ('MCAA', 'Ministry Of Creativity And Arts'), ('MOSAF', 'Ministry Of Sports And Fitness'), ('MASA', 'Ministry Of Seed Sowing And Admnistration'), ('MSO', 'Ministry Of Security And Order'), ('ME', 'Ministry Of Evangelism'), ('MI', 'Ministry Of Information'), ('MIAW', 'Ministry Of Interior And Welfare'), ('MOM', 'Ministry Of Music'), ('MOH', 'Ministry Of Helps'), ('MOTA', 'Ministry Of Trade And Investment'), ('MEA', 'Ministry Of Exterior Affairs'), ('MOE', 'Ministry Of Events'), ('MOPAM', 'Ministry Of Property And Management')], default='None', max_length=5)),
                ('Cell_Component_Leader_Name', models.CharField(max_length=30, null=True)),
                ('Cell_Leader_Name', models.CharField(max_length=30, null=True)),
                ('Tissue_Leader_Name', models.CharField(max_length=30, null=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
