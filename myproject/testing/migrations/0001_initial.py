# Generated by Django 4.1.3 on 2022-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bdquestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100)),
                ('questions', models.TextField()),
                ('answer1', models.TextField()),
                ('answer2', models.TextField()),
                ('trueanswer', models.CharField(max_length=1)),
            ],
        ),
    ]