from django.urls import re_path as url, include
from . import views

test_patterns = [
	url(r'^$', views.index, name='mpesa_index'),
	url(r'^oauth/success', views.oauth_success, name='test_oauth_success'),
	url(r'^stk-push/success', views.stk_push_success, name='test_stk_push_success'),
	url(r'^business-payment/success', views.business_payment_success, name='test_business_payment_success'),
	url(r'^salary-payment/success', views.salary_payment_success, name='test_salary_payment_success'),
	url(r'^promotion-payment/success', views.promotion_payment_success, name='test_promotion_payment_success'),
	url(r'^transaction-status/success', views.transaction_status_query_success, name='test_transaction_status_success'),
	url(r'^reversal/success', views.transaction_reversal_success, name='test_reversal_success'),
	url(r'^register-c2b-urls/success', views.register_c2b_urls_success, name='test_register_c2b_urls_success'),
]

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tests/', include(test_patterns)),
]

