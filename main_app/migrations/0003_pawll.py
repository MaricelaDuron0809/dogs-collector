# Generated by Django 3.2.8 on 2021-10-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_treat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pawll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dogs', models.ManyToManyField(to='main_app.Dog')),
            ],
        ),
    ]
