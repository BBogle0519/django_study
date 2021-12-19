# Generated by Django 4.0 on 2021-12-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(blank=True, db_column='USER_ID', max_length=20, null=True, unique=True)),
                ('user_pw', models.CharField(blank=True, db_column='USER_PW', max_length=255, null=True)),
                ('user_nm', models.CharField(blank=True, db_column='USER_NM', max_length=20, null=True)),
                ('user_ph', models.IntegerField(blank=True, db_column='USER_PH', null=True)),
                ('user_email', models.CharField(blank=True, db_column='USER_EMAIL', max_length=50, null=True)),
                ('user_reg_ymd', models.DateTimeField(auto_now_add=True, db_column='USER_REG_YMD')),
                ('user_st', models.IntegerField(blank=True, db_column='USER_ST', default=1, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user_tb',
            },
        ),
    ]