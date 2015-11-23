# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventid', models.AutoField(serialize=False, primary_key=True)),
                ('eventName', models.CharField(max_length=50)),
                ('eventDescription', models.CharField(max_length=200)),
                ('eventDate', models.DateTimeField(verbose_name=b'Event Date/Time')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=10)),
                ('stream', models.CharField(default=b'CSE', max_length=3, choices=[(b'ECE', b'Electronics'), (b'CSE', b'Computer Science')])),
                ('batch', models.CharField(max_length=4)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='userWhoPosted',
            field=models.ForeignKey(to='CollegeEventsApp.UserProfile'),
        ),
    ]
