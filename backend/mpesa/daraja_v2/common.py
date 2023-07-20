import json
import requests
from requests.auth import HTTPBasicAuth
from decouple import config
from mpesa.daraja.utils import mpesa_access_token
class RequestHandler:
	def __init__(self):
		mpesa_environment = config('MPESA_ENVIRONMENT')
		if mpesa_environment == 'sandbox':
			self.base_url = 'https://sandbox.safaricom.co.ke/'
		else:
			self.base_url = 'https://api.safaricom.co.ke/'

	def makeRequest(self,**kwargs):
		try:
			data=kwargs.pop('data')
			print(data)			
			headers={}
			headers['Content-Type']='application/json'
			headers['Authorization']='Bearer'+' '+mpesa_access_token()
			response = lambda headers:requests.post(self.base_url+kwargs.pop('url'), json=data, headers=headers).text
			return response(headers)
		except Exception as e:
			raise  e