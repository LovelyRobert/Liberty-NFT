# Generated by Django 4.1.5 on 2023-01-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criar', '0007_alter_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
