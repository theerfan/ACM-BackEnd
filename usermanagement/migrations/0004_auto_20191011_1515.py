# Generated by Django 2.2.5 on 2019-10-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0003_auto_20191010_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='team',
            name='institution',
            field=models.CharField(max_length=50),
        ),
    ]