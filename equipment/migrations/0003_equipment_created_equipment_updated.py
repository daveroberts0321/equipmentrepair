# Generated by Django 4.2.5 on 2023-09-24 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_alter_repairs_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
