# Generated by Django 4.1.6 on 2023-06-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0020_atimeslot_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='atimeslot',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
