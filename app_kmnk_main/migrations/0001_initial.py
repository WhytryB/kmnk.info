# Generated by Django 2.1 on 2019-01-13 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_place', '0002_auto_20181103_1914'),
        ('person', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klass', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], max_length=2)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название курса')),
            ],
            options={
                'verbose_name': 'Название курса',
                'verbose_name_plural': 'Названия курсов',
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='function', to='person.Person')),
                ('app_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='function', to='app_place.PlaceAddress')),
            ],
            options={
                'verbose_name': 'Функция',
                'verbose_name_plural': 'Функции',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название позиции')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
        migrations.AddField(
            model_name='function',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='function', to='app_kmnk_main.Position'),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='app_kmnk_main.CourseName'),
        ),
    ]
