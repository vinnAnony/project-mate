# Generated by Django 4.2.2 on 2023-06-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_subscription_created_at_subscription_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='activated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='cancelled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('Pending Payment', 'Pendingpayment'), ('Active', 'Active'), ('Suspended', 'Suspended'), ('Cancelled', 'Cancelled')], default='Pending Payment', max_length=100),
        ),
        migrations.AddField(
            model_name='subscription',
            name='suspended_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]