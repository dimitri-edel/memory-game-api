# Generated by Django 5.1.2 on 2024-11-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='complementary_color',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='style',
            name='primary_color',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='style',
            name='secondary_color',
            field=models.CharField(max_length=9),
        ),
    ]
