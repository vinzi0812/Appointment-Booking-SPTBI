# Generated by Django 4.1.6 on 2023-06-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0022_booking_no_of_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='month',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
