# Generated by Django 5.0.3 on 2024-03-27 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('lName', models.CharField(max_length=50)),
                ('fName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('passW', models.CharField(max_length=20)),
                ('isAdmin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('accType', models.CharField(max_length=20)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('lastChangeDate', models.DateField()),
                ('isActive', models.BooleanField(default=True)),
                ('custID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='bankApp.customer')),
            ],
        ),
    ]
