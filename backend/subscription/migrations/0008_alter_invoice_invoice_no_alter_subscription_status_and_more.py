# Generated by Django 4.2.2 on 2023-07-18 11:29

from django.db import migrations, models
import subscription.models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_alter_invoice_invoice_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_no',
            field=models.IntegerField(default=subscription.models.get_initial_invoice_number, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('Pending Payment', 'Pending Payment'), ('Active', 'Active'), ('Suspended', 'Suspended'), ('Cancelled', 'Cancelled')], default='Pending Payment', max_length=100),
        ),
        migrations.AlterField(
            model_name='subscriptionpackage',
            name='duration',
            field=models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('Year', 'Year'), ('One-Time', 'One Time')], max_length=100),
        ),
    ]
