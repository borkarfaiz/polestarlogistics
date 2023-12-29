# Generated by Django 3.2.23 on 2023-12-29 07:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imo_number', models.CharField(max_length=7, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ship_analysis.ship')),
            ],
        ),
    ]
