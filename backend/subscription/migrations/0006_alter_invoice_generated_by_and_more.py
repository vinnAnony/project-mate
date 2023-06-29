# Generated by Django 4.2.2 on 2023-06-29 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_alter_project_commence_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0003_alter_customer_created_by'),
        ('subscription', '0005_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='generated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subscription_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subscriptions', to='subscription.subscription'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, help_text='Amount excluding tax', max_digits=11),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_tax_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.project'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subscription.subscriptionpackage'),
        ),
        migrations.AlterField(
            model_name='subscriptionpackage',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.project'),
        ),
    ]
