from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Subscription)
admin.site.register(SubscriptionPackage)
admin.site.register(Invoice)
