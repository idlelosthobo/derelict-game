# Generated by Django 3.0.4 on 2020-04-16 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0008_auto_20200415_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]