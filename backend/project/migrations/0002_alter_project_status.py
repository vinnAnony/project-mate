# Generated by Django 4.2.2 on 2023-06-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Initiated', 'Initiated'), ('Planning', 'Planning'), ('In-Progress', 'Inprogress'), ('On-Hold', 'Onhold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Initiated', max_length=55),
        ),
    ]
