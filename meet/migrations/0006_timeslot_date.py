# Generated by Django 4.1.6 on 2023-06-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0005_timeslot_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
