# Generated by Django 4.2.2 on 2023-06-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default='711236', max_length=6, unique=True),
        ),
    ]
