from decouple import config
from .common import RequestHandler

class c2bHandler:
	@staticmethod
	def handle(confirmation_url:str|None, validation_url:str|None):
		"""
		Register validation and confirmation URLs on M-Pesa

		Args:
			
			confirmation_url (str): -- This is the URL that receives the confirmation request from API upon payment completion.

			validation_url (str): -- This is the URL that receives the validation request from the API upon payment submission.
   									The validation URL is only called if the external validation on the registered shortcode is enabled.
            						(By default External Validation is disabled).

		Returns:
			str: Transaction Status Request response body
		"""
		try:
			requestbody={}
			requestbody['ShortCode']=config('MPESA_SHORTCODE')
			requestbody['ResponseType']='Completed'
			requestbody['ConfirmationURL']=confirmation_url if(confirmation_url) else config('MPESA_C2B_CONFIRMATION_URL')
			requestbody['ValidationURL']=validation_url if(validation_url) else config('MPESA_C2B_VALIDATION_URL')
			return RequestHandler().makeRequest(
				url='mpesa/c2b/v1/registerurl',
				data=requestbody
			)
		except Exception:
			raise  Exception