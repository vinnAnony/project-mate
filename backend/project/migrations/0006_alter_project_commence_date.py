# Generated by Django 4.2.2 on 2023-06-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_project_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='commence_date',
            field=models.DateField(null=True),
        ),
    ]
