# Generated by Django 4.0.4 on 2022-05-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='documento',
            field=models.IntegerField(),
        ),
    ]
