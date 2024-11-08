# Generated by Django 5.1.2 on 2024-11-08 16:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(max_length=7)),
                ('secondary_color', models.CharField(max_length=7)),
                ('complementary_color', models.CharField(max_length=7)),
                ('background_image', models.ImageField(upload_to='styles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'verbose_name': 'Style',
                'verbose_name_plural': 'Styles',
            },
        ),
    ]