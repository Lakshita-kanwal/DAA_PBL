# Generated by Django 5.1.6 on 2025-02-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stugrp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('students', models.ManyToManyField(to='stugrp.student')),
            ],
        ),
    ]
