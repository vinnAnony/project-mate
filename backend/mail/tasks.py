from templated_email import send_templated_mail
from celery import shared_task
from celery.signals import task_failure

import ntpath
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import logging
logger = logging.getLogger(__name__)
 
@shared_task
def _async_send_email(context:dict, template:str, from_email:str, recipients:list[str]) ->None:

    """
    Schedule a task to send an email asynchronously.

    Args:
        context (dict): A dictionary containing information to be passed to the email template.
        template (str): The name of the email template file.
        from_email (str): The email address of the sender.
        recipients (list[str]): A list of email addresses of the recipients.

    Usage:
        _async_send_email.delay(context, template, from_email, recipients)

    Returns:
        None.

    Note:
        The "send_templated_mail" function is used to send the email using the provided information. 
        This function is asynchronous and runs in the background, which allows the application to continue processing 
        without waiting for the email to be sent.
    """

    send_templated_mail(
        from_email=from_email,
        recipient_list=recipients,
        context=context,
        template_name=template,
    )
    
@shared_task
def _async_send_attachment_email(subject:str, context:dict, template:str, from_email:str, recipients:list[str],attachment_file_path:str) ->None:

    # Render the HTML email template
    html_message = render_to_string(template, context)

    # Create the plain text version of the email (optional)
    plain_message = strip_tags(html_message)

    # Create an EmailMultiAlternatives object
    email = EmailMultiAlternatives(
        subject=subject,
        from_email=from_email,
        body=plain_message,
        to=recipients
    )

    # Attach the PDF file to the email
    with open(attachment_file_path, 'rb') as f:
        email.attach(ntpath.basename(attachment_file_path), f.read(), 'application/pdf')

    # Attach the HTML message as an alternative
    email.attach_alternative(html_message, 'text/html')

    # Send the email
    email.send()
    

def _on_mail_error_callback(sender=None, task_id=None, exception=None, **kwargs):
    # TODO: - use a global application logging service to log any errors that occur during email sending. 
    
    logger.warning("error sending email in background task")
    pass


task_failure.connect(_on_mail_error_callback, sender=_async_send_email)