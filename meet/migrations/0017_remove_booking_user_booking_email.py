# Generated by Django 4.1.6 on 2023-06-21 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0016_delete_incubatee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]