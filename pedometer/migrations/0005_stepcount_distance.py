# Generated by Django 4.0 on 2022-01-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedometer', '0004_rename_user_id_stepcount_user_id_pk'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepcount',
            name='distance',
            field=models.FloatField(default=0, null=True),
        ),
    ]
