# Generated by Django 4.0 on 2021-12-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_tb_is_active'),
        ('pedometer', '0002_alter_stepcount_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepcount',
            name='user_id',
            field=models.ForeignKey(db_column='user_id_pk', on_delete=django.db.models.deletion.CASCADE, to='account.user_tb'),
        ),
    ]
