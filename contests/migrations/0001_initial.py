# Generated by Django 2.2.3 on 2019-08-31 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('problems', models.CharField(max_length=500)),
                ('final_ranking_onsite', models.CharField(max_length=500)),
                ('final_ranking_online', models.CharField(max_length=550)),
            ],
            options={
                'verbose_name': 'ACM',
                'verbose_name_plural': 'ACM CONTEST',
            },
        ),
    ]
