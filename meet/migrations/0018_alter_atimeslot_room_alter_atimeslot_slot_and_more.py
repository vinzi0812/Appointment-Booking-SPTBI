# Generated by Django 4.1.6 on 2023-06-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0017_remove_booking_user_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atimeslot',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atimeslot',
            name='slot',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
