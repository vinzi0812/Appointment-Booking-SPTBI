# Generated by Django 4.1.6 on 2023-06-21 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0015_remove_incubatee_bookings_booking_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Incubatee',
        ),
    ]
