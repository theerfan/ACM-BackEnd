# Generated by Django 2.2.3 on 2019-09-02 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
        ('contests', '0005_contest_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='photologue.Photo')),
            ],
            options={
                'abstract': False,
            },
            bases=('photologue.photo',),
        ),
    ]
