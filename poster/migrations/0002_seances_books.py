# Generated by Django 5.0.6 on 2024-06-03 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название фильма')),
                ('date_time', models.CharField(max_length=20, verbose_name='Дата время')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=3, verbose_name='Место')),
                ('mail', models.CharField(max_length=100, verbose_name='Почта')),
                ('seanse_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='poster.seances')),
            ],
        ),
    ]