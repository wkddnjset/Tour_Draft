# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11 on 2018-02-19 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 1.11 on 2018-02-19 12:40
from __future__ import unicode_literals

from django.db import migrations, models
>>>>>>> 206a777a6d2c7dacce5d156d933cc8fbe5bfc195


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=45)),
                ('address', models.TextField()),
                ('latitude', models.CharField(max_length=45)),
                ('longitude', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_Plan.Item')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='_Plan.User')),
                ('plan_name', models.CharField(max_length=45)),
                ('share_flag', models.BooleanField()),
                ('start_datetime', models.DateField(auto_now_add=True)),
                ('end_datetime', models.DateField(auto_now_add=True)),
                ('end_address_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='end_time', to='_Plan.Address')),
                ('start_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_time', to='_Plan.Address')),
            ],
        ),
        migrations.AddField(
            model_name='plan_item',
            name='itemslot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_Plan.TimeSlot'),
        ),
=======
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
>>>>>>> 206a777a6d2c7dacce5d156d933cc8fbe5bfc195
    ]
