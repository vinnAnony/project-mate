# Generated by Django 4.2.2 on 2023-06-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_project_commence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='commence_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
