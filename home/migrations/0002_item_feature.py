# Generated by Django 4.0.3 on 2022-03-31 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='feature',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
