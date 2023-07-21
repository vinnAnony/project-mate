from  decouple import  config
import base64,datetime
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from decouple import config
from .common import  RequestHandler
from mpesa.daraja.utils import encrypt_security_credential
class statusQueryHandler:
	@staticmethod
	def handle(mpesaTransactionID:str, initiator:int):
		"""
		Check the status of a transaction.

		Args:
			mpesaTransactionID (str): -- Unique identifier to identify a transaction on Mpesa.
   
			initiator (int) -- The name of the initiator initiating the request.

		Returns:
			str: Transaction Status Request response body
		"""
		try:
			requestbody={}
			requestbody['Initiator']=config('MPESA_INITIATOR_USERNAME') 
			requestbody['SecurityCredential']=encrypt_security_credential(config('MPESA_INITIATOR_SECURITY_CREDENTIAL'))
			requestbody['CommandID']='TransactionStatusQuery'
			requestbody['TransactionID']=mpesaTransactionID
			requestbody['PartyA'] = config('MPESA_SHORTCODE')						
			requestbody['IdentifierType']=initiator
			requestbody['ResultURL']=config('MPESA_STATUS_QUERY_RESULT_URL')
			requestbody['QueueTimeOutURL']=config('MPESA_STATUS_QUERY_TIMEOUT_URL')
			requestbody['Remarks']='Status query'
			requestbody['Occasion']=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
			return RequestHandler().makeRequest(
				url='mpesa/transactionstatus/v1/query',
				data=requestbody
			)
		except Exception as e:
			raise e

