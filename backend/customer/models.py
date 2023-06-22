import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False)
    name = models.CharField(max_length=150,blank=False,null=False)
    phone_number = PhoneNumberField(blank=True, null=True , unique= True, help_text='Phone number')
    email = models.EmailField(max_length=254, blank=True, null=True , unique= True)
    contact_name = models.CharField(max_length=250,blank=False, null=False)
    address = models.CharField( max_length=255,blank=False, null=False)
    special_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False)

    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer-detail", kwargs={"pk": self.pk})
