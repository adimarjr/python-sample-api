# Generated by Django 3.0.7 on 2020-06-25 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.TextField(),
        ),
    ]