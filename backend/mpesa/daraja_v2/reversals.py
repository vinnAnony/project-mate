from  decouple import  config
import datetime
from decouple import config
from .common import  RequestHandler
from mpesa.daraja.utils import encrypt_security_credential
class reversalHandler:
	@staticmethod
	def handle(mpesaTransactionID:str, amount:int, remarks:str):
		"""
		Reverses a C2B M-Pesa transaction.

		Args:
			
			mpesaTransactionID (str): -- This is the Mpesa Transaction ID of the transaction which you wish to reverse.

			amount (int) -- The amount transacted in the transaction is to be reversed, down to the cent.			

			remarks (str): -- Description for reversal

		Returns:
			str: Reversal Request response body
		"""
		try:
			requestbody={}
			requestbody['Initiator']=config('MPESA_INITIATOR_USERNAME') 
			requestbody['SecurityCredential']=encrypt_security_credential(config('MPESA_INITIATOR_SECURITY_CREDENTIAL'))
			requestbody['CommandID']='TransactionReversal'
			requestbody['TransactionID']=mpesaTransactionID
			requestbody['Amount']=amount
			requestbody['ReceiverParty']=config('MPESA_SHORTCODE')
			requestbody['RecieverIdentifierType']=11
			requestbody['ResultURL']=config('MPESA_REVERSAL_RESULT_URL')
			requestbody['QueueTimeOutURL']=config('MPESA_REVERSAL_TIMEOUT_URL')
			requestbody['Remarks']=remarks
			requestbody['Occasion']=str('{:%y%m%d%H%M%S}'.format(datetime.datetime.now()))
			return RequestHandler().makeRequest(
				url='mpesa/reversal/v1/request',
				data=requestbody
			)
		except Exception as e:
			raise e


