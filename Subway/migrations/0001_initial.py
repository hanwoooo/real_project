# Generated by Django 3.2.13 on 2023-02-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('X_location', models.TextField()),
                ('Y_location', models.TextField()),
            ],
        ),
    ]
