# Generated by Django 2.1 on 2018-08-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('dop', models.CharField(max_length=100)),
            ],
        ),
    ]