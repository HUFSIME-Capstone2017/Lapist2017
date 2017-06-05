# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_eurail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractive',
            fields=[
                ('attract_id', models.TextField(blank=True, db_column='ATTRACT_ID', primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, db_column='CITY_NAME', max_length=20, null=True)),
                ('a_name', models.CharField(blank=True, db_column='A_NAME', max_length=20, null=True)),
                ('a_info', models.TextField(blank=True, db_column='A_INFO', null=True)),
                ('country_name', models.TextField(blank=True, db_column='COUNTRY_NAME', null=True)),
            ],
            options={
                'db_table': 'ATTRACTIVE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_name', models.TextField(blank=True, db_column='COUNTRY_NAME', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'COUNTRY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cus_id', models.TextField(blank=True, db_column='CUS_ID', primary_key=True, serialize=False)),
                ('cus_pass', models.CharField(blank=True, db_column='CUS_PASS', max_length=50, null=True)),
                ('cus_email', models.CharField(blank=True, db_column='CUS_EMAIL', max_length=50, null=True)),
                ('cus_name', models.CharField(blank=True, db_column='CUS_NAME', max_length=20, null=True)),
                ('sns_login', models.CharField(blank=True, db_column='SNS_LOGIN', max_length=20, null=True)),
            ],
            options={
                'db_table': 'CUSTOMER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoPerson',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'demo_person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoScrapy1',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sch_cost', models.PositiveSmallIntegerField(db_column='SCH_COST')),
                ('air_info', models.TextField(db_column='AIR_INFO')),
                ('r_origin', models.TextField(db_column='R_ORIGIN')),
                ('dep_date', models.DateField(db_column='DEP_DATE')),
                ('r_dest', models.TextField(db_column='R_DEST')),
                ('arr_t', models.TextField(db_column='ARR_T')),
                ('l_lo', models.TextField(db_column='L_LO')),
                ('dep_t', models.TextField(db_column='DEP_T')),
            ],
            options={
                'db_table': 'demo_scrapy1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.TextField(blank=True, db_column='FOOD_ID', primary_key=True, serialize=False)),
                ('f_name', models.TextField(blank=True, db_column='F_NAME', null=True)),
                ('f_info', models.TextField(blank=True, db_column='F_INFO', null=True)),
                ('country_name', models.TextField(blank=True, db_column='COUNTRY_NAME', null=True)),
            ],
            options={
                'db_table': 'FOOD',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mylist',
            fields=[
                ('list_id', models.TextField(blank=True, db_column='LIST_ID', primary_key=True, serialize=False)),
                ('total_cost', models.IntegerField(blank=True, db_column='TOTAL_COST', null=True)),
                ('dep_date', models.DateField(blank=True, db_column='DEP_DATE', null=True)),
                ('arr_date', models.DateField(blank=True, db_column='ARR_DATE', null=True)),
                ('dep_time', models.CharField(blank=True, db_column='DEP_TIME', max_length=20, null=True)),
                ('arr_time', models.CharField(blank=True, db_column='ARR_TIME', max_length=20, null=True)),
                ('save_date', models.DateField(blank=True, db_column='SAVE_DATE', null=True)),
                ('city_1', models.CharField(blank=True, db_column='CITY_1', max_length=20, null=True)),
                ('city_2', models.CharField(blank=True, db_column='CITY_2', max_length=20, null=True)),
                ('city_3', models.CharField(blank=True, db_column='CITY_3', max_length=20, null=True)),
                ('city_4', models.CharField(blank=True, db_column='CITY_4', max_length=20, null=True)),
                ('city_5', models.CharField(blank=True, db_column='CITY_5', max_length=20, null=True)),
                ('city_6', models.CharField(blank=True, db_column='CITY_6', max_length=20, null=True)),
                ('city_7', models.CharField(blank=True, db_column='CITY_7', max_length=20, null=True)),
                ('city_8', models.CharField(blank=True, db_column='CITY_8', max_length=20, null=True)),
                ('stay_1', models.CharField(blank=True, db_column='STAY_1', max_length=20, null=True)),
                ('stay_2', models.CharField(blank=True, db_column='STAY_2', max_length=20, null=True)),
                ('stay_3', models.CharField(blank=True, db_column='STAY_3', max_length=20, null=True)),
                ('stay_4', models.CharField(blank=True, db_column='STAY_4', max_length=20, null=True)),
                ('stay_5', models.CharField(blank=True, db_column='STAY_5', max_length=20, null=True)),
                ('stay_6', models.CharField(blank=True, db_column='STAY_6', max_length=20, null=True)),
                ('stay_7', models.CharField(blank=True, db_column='STAY_7', max_length=20, null=True)),
                ('stay_8', models.CharField(blank=True, db_column='STAY_8', max_length=20, null=True)),
                ('cus_id', models.TextField(blank=True, db_column='CUS_ID', null=True)),
            ],
            options={
                'db_table': 'MYLIST',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.TextField(blank=True, db_column='ROUTE_ID', primary_key=True, serialize=False)),
                ('r_origin', models.TextField(blank=True, db_column='R_ORIGIN', null=True)),
                ('r_dest', models.TextField(blank=True, db_column='R_DEST', null=True)),
            ],
            options={
                'db_table': 'ROUTE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('route_id', models.TextField(blank=True, db_column='ROUTE_ID', primary_key=True, serialize=False)),
                ('daysleft', models.IntegerField(blank=True, db_column='DAYSLEFT', null=True)),
                ('cost', models.TextField(blank=True, db_column='COST', null=True)),
            ],
            options={
                'db_table': 'TREND',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Sign_Up_Data',
        ),
        migrations.AlterModelTable(
            name='eurail',
            table='EURAIL',
        ),
    ]