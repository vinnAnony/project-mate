import random
import time
import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Generate six digit random code
def generate_verification_code(size=6): 
    return ''.join(str(random.randint(0,9)) for i in range(size))
    
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=50)
    # phone_number = PhoneNumberField(blank=True, help_text='Contact phone number', null=True , unique= True)
    verification_code = models.CharField(max_length=6, unique=True,default=generate_verification_code())
    code_generated_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False) # to be set up later in views to change if user verified
    # USERNAME_FIELD = 'email' #set email to be used for authentication
    
    # add requirements for signup
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'email']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    # resets the verification code after every 1hr
    def get_verification_code(self):
        now = time.time()
        elapsed = now - self.code_generated_at.timestamp()
        if elapsed > 3600: 
            self.verification_code = generate_verification_code()
            self.code_generated_at = now
            self.save
        return self.verification_code