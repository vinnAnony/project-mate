# Generated by Django 4.2.2 on 2023-07-19 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0008_alter_invoice_invoice_no_alter_subscription_status_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payments', to='subscription.invoice'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Mpesa', 'Mpesa'), ('Paybill', 'Paybill'), ('Bank', 'Bank')], max_length=100),
        ),
    ]
