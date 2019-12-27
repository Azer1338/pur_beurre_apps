# Generated by Django 3.0 on 2019-12-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=501)),
                ('category', models.CharField(max_length=502)),
                ('energy', models.FloatField(max_length=503)),
                ('fat', models.FloatField(max_length=504)),
                ('fat_saturated', models.FloatField(max_length=505)),
                ('sugar', models.FloatField(max_length=506)),
                ('salt', models.FloatField(max_length=507)),
                ('nutrition_score', models.CharField(max_length=508)),
                ('url_link', models.CharField(max_length=509)),
                ('picture_link', models.CharField(max_length=510)),
            ],
        ),
        migrations.CreateModel(
            name='UserLinkToAlimentsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('aliment_id', models.CharField(max_length=20)),
            ],
        ),
    ]
