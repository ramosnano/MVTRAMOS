# Generated by Django 4.0.4 on 2022-05-25 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0003_alter_familiar_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='documento',
            field=models.DateField(),
        ),
    ]
