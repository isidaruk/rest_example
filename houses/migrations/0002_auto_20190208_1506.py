# Generated by Django 2.1.5 on 2019-02-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
