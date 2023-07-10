from datetime import datetime, timedelta
from celery import shared_task
from django.forms.models import model_to_dict

from subscription.models import *
from mail.email import send_email

@shared_task(name='one_week_due_invoice_reminder')
def remind_one_week_invoice_due():
    current_date = datetime.now().date()
    seven_days_from_today = current_date + timedelta(days=7)
    # fetch pending invoices where due date - today is 7 days
    invoices = Invoice.objects.filter(due_date__date=seven_days_from_today,status=Invoice.InvoiceStatus.Pending)
    
    for invoice in invoices:
        invoice_project = invoice.subscription_id.subscription_package_id.project_id
        subscription_package = invoice.subscription_id.subscription_package_id
        
        invoice_lines = [
            {
                'description':f'{invoice_project.name} - {subscription_package.name} plan',
                'amount':invoice.total_amount,
            },
            {
                'description':f'VAT {invoice.tax_percentage}',
                'amount':invoice.total_tax_amount,
            }if invoice.total_tax_amount else {},
            {
                'description':f'Total paid',
                'amount':invoice.total_paid,
            }if invoice.total_paid else {},            
        ]
        total_amount_due = decimal.Decimal(invoice.total_amount + invoice.total_tax_amount) - decimal.Decimal(invoice.total_paid)
        
        # send reminder email
        send_email(
            context={
                'customer': invoice.subscription_id.customer_id.name,
                'project': model_to_dict(invoice.subscription_id.subscription_package_id.project_id),
                'subscription': model_to_dict(invoice.subscription_id.subscription_package_id),
                'due_days': '7 days',
                'company':{
                    'name':'BizCore'
                },
                'invoice':{
                    'invoice_no':invoice.invoice_no,
                    'generated_at':current_date.strftime('%d-%m-%Y'),
                    'invoice_lines':invoice_lines,
                    'total_amount_due':total_amount_due,
                    'due_date':invoice.due_date.strftime('%d-%m-%Y'),
                }                
            },
            template='invoice_due_reminder',
            recipients=[invoice.subscription_id.customer_id.email]        
        )