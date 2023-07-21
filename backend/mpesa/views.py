# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os
from mpesa.daraja import utils

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from mpesa.daraja.core import MpesaClient
from decouple import config
from datetime import datetime
from django.conf import settings
from mpesa.daraja_v2 import statusQueryHandler,reversalHandler,c2bHandler

cl = MpesaClient()
stk_push_callback_url = settings.MPESA_EXPRESS_CALLBACK_URL
b2c_callback_url = settings.MPESA_B2C_CALLBACK_URL

def index(request):

	return HttpResponse('Welcome to the home of daraja APIs')

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)

def stk_push_success(request):
	phone_number = os.environ.get('MPESA_TEST_PHONENUMBER')
	amount = 1
	account_reference = 'ABC001'
	transaction_desc = 'STK Push Description'
	callback_url = stk_push_callback_url
	r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
	return JsonResponse(r.response_description, safe=False)

def business_payment_success(request):
	phone_number = os.environ.get('MPESA_TEST_PHONENUMBER')
	amount = 1
	transaction_desc = 'Business Payment Description'
	occassion = 'Test business payment occassion'
	callback_url = b2c_callback_url
	r = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)

def salary_payment_success(request):
	phone_number = os.environ.get('MPESA_TEST_PHONENUMBER')
	amount = 1
	transaction_desc = 'Salary Payment Description'
	occassion = 'Test salary payment occassion'
	callback_url = b2c_callback_url
	r = cl.salary_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)

def promotion_payment_success(request):
	phone_number = os.environ.get('MPESA_TEST_PHONENUMBER')
	amount = 1
	transaction_desc = 'Promotion Payment Description'
	occassion = 'Test promotion payment occassion'
	callback_url = b2c_callback_url
	r = cl.promotion_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)

def transaction_status_query_success(request):
	class StatusQueryInitiator:
		MSISDN = 1
		TILL_NUMBER = 2
		ORGANISATION_SHORT_CODE = 4

	mpesa_transaction_id = 'RGK11RZPTT'
	initiator = StatusQueryInitiator.ORGANISATION_SHORT_CODE
	
	r = statusQueryHandler().handle(mpesaTransactionID=mpesa_transaction_id,initiator=initiator)
	return JsonResponse(json.loads(r), safe=False)

def transaction_reversal_success(request):	
	mpesa_transaction_id = 'RGL9297DVR'
	amount = 1
	remarks = 'Reversal for mistaken payment'	
	
	r = reversalHandler().handle(mpesaTransactionID=mpesa_transaction_id,amount=amount,remarks=remarks)
	return JsonResponse(json.loads(r), safe=False)

def register_c2b_urls_success(request):	
	confirmation_url = 'https://example.com/payme/projectmate-django-c2b-confirm.php'
	validation_url = 'https://example.com/payme/projectmate-django-c2b-validate.php'
	
	r = c2bHandler().handle(confirmation_url=confirmation_url,validation_url=validation_url)
	return JsonResponse(json.loads(r), safe=False)
