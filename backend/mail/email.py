import os
from django.conf import settings
from mail.tasks import _async_send_email

base_dir = os.path.abspath(os.path.dirname(__file__))

def send_email(context:dict, template:str, recipients:list[str]) -> str:
    """
    Send templated emails.
    This function acts as a proxy to `_async_send_email`.

    :param context: A dictionary that contains information to be passed to the template.
    :param template: A string that represents the name of the template to be used for the email.
    :param recipient: A string that represents the email address of the recipient.
    :return: A unique ID from a scheduled task.
    """
    
    if not os.path.exists(os.path.join(base_dir,f"templates/templated_email/{template}.email")):

        raise FileNotFoundError(f"Template file {template} not found")
    
    task = _async_send_email.delay(
        context=context,
        template=template,
        from_email=settings.EMAIL_HOST_USER,
        recipients=recipients
    )

    return task.id