# Generated by Django 2.2.13 on 2020-06-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherloginsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=500)),
                ('answer1', models.CharField(max_length=500)),
                ('options1', models.CharField(max_length=500)),
            ],
        ),
    ]
