# Generated by Django 4.0.6 on 2022-08-04 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigiResume', '0002_alter_institution_mobile_alter_organisation_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='aadhar',
            field=models.IntegerField(),
        ),
    ]