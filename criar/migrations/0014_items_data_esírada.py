# Generated by Django 4.1.5 on 2023-02-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criar', '0013_alter_items_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='data_esírada',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
