# Generated by Django 3.2.10 on 2021-12-26 12:15

import datetime

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensors",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="IOC",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("type", models.CharField(max_length=32)),
                ("first_seen", models.DateTimeField(default=datetime.datetime.utcnow)),
                ("last_seen", models.DateTimeField(default=datetime.datetime.utcnow)),
                (
                    "days_seen",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.DateField(), blank=True, size=None
                    ),
                ),
                ("number_of_days_seen", models.IntegerField(default=1)),
                ("times_seen", models.IntegerField(default=1)),
                ("log4j", models.BooleanField(default=False)),
                ("scanner", models.BooleanField(default=False)),
                ("payload_request", models.BooleanField(default=False)),
                (
                    "related_urls",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=900),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "related_ioc",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_greedybear_ioc_related_ioc_+",
                        to="greedybear.IOC",
                    ),
                ),
            ],
        ),
    ]
