# Generated by Django 3.2.8 on 2021-10-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irum', models.CharField(max_length=10)),
                ('juso', models.CharField(max_length=20)),
                ('nai', models.IntegerField()),
            ],
        ),
    ]