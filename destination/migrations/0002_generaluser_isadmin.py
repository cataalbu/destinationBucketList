# Generated by Django 4.2.1 on 2023-05-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaluser',
            name='isAdmin',
            field=models.BooleanField(null=True),
        ),
    ]
