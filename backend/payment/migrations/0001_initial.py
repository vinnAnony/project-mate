# Generated by Django 4.2.2 on 2023-07-18 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0008_alter_invoice_invoice_no_alter_subscription_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('payment_type', models.CharField(choices=[('in', 'In'), ('out', 'Out')], help_text='Whether receiving(in) or sending(out)', max_length=100)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Mpesa', 'Mpesa'), ('PayBill', 'Paybill'), ('Bank', 'Bank')], max_length=100)),
                ('reference', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payments', to='subscription.invoice')),
                ('processed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
