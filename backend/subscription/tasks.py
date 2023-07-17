from datetime import datetime, timedelta
from celery import shared_task
from django.forms.models import model_to_dict
from django.template.loader import get_template
from django.conf import settings
import os
import pdfkit

from subscription.models import *
from mail.email import send_email,send_email_with_attachment

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
                    'name':'ProjectMate'
                },
                'invoice':{
                    'invoice_no':invoice.invoice_no,
                    'generated_at':current_date.strftime('%d-%m-%Y'),
                    'currency':'Ksh',
                    'invoice_lines':invoice_lines,
                    'total_amount_due':total_amount_due,
                    'due_date':invoice.due_date.strftime('%d-%m-%Y'),
                }                
            },
            template='invoice_due_reminder',
            recipients=[invoice.subscription_id.customer_id.email]        
        )
        
@shared_task
def generate_and_email_invoice_pdf(pk):
    current_date = datetime.now().date()
    #fetch that invoice
    invoice = Invoice.objects.get(pk=pk)
    
    if invoice:
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
        
        context = {}
        context['customer'] = invoice.subscription_id.customer_id
        context['project'] = model_to_dict(invoice.subscription_id.subscription_package_id.project_id)
        context['subscription_package'] = model_to_dict(invoice.subscription_id.subscription_package_id)
        context['company'] = {
                'name':'ProjectMate',
                'logo':'https://vinnjeru.com/images/vinn-logo.png'
            }
        context['invoice'] = {
                'invoice_no':invoice.invoice_no,
                'generated_at':invoice.generated_at.strftime('%d-%m-%Y'),
                'currency':'Ksh',
                'invoice_lines':invoice_lines,
                'total_amount_due':total_amount_due,
                'due_date':invoice.due_date.strftime('%d-%m-%Y'),
            }

        #The name of your PDF file
        filename = '{}.pdf'.format(f"{invoice.invoice_no}-{current_date.strftime('%d-%m-%Y')}")

        #HTML FIle to be converted to PDF - inside your Django directory
        template = get_template('invoice/pdf-template.html')

        #Render the HTML
        html = template.render(context)

        options = {
            'encoding': 'UTF-8',
            'javascript-delay':'1000', #Optional
            'enable-local-file-access': None, #To be able to access CSS
            'page-size': 'A4',
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ],
        }

        #location to wkhtmltopdf
        config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_LOCATION)

        #Saving the File
        filepath = os.path.join(settings.PDF_FILES_FOLDER, 'customer_invoices')
        os.makedirs(filepath, exist_ok=True)
        pdf_save_path = f"{filepath}/{filename}"
                  
        # Replace file if it exists
        if(os.path.isfile(pdf_save_path) ):
            os.remove(pdf_save_path)
            
        #Save the PDF file   
        pdfkit.from_string(html, pdf_save_path, configuration=config, options=options)
        
        send_email_with_attachment(
            subject='Customer Invoice',
            context={
                'customer': invoice.subscription_id.customer_id.name,
                'project': model_to_dict(invoice.subscription_id.subscription_package_id.project_id),
                'subscription': model_to_dict(invoice.subscription_id.subscription_package_id),
                'company':{
                    'name':'ProjectMate'
                },
                'invoice':{
                    'invoice_no':invoice.invoice_no,
                    'generated_at':current_date.strftime('%d-%m-%Y'),
                    'currency':'Ksh',
                    'invoice_lines':invoice_lines,
                    'total_amount_due':total_amount_due,
                    'due_date':invoice.due_date.strftime('%d-%m-%Y'),
                }                
            },
            template='email/customer_invoice.html',
            recipients=[invoice.subscription_id.customer_id.email],
            attachment_file_path = pdf_save_path
        )