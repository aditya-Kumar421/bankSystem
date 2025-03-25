from django.urls import path
from .views import  LoanCreateView, PaymentView, LoanLedgerView, CustomerLoansView

urlpatterns = [
    path('lend/', LoanCreateView.as_view(), name='lend'),
    path('payment/<int:loan_id>/', PaymentView.as_view(), name='payment'),
    path('ledger/<int:loan_id>/', LoanLedgerView.as_view(), name='ledger'),
    path('overview/<int:customer_id>/', CustomerLoansView.as_view(), name='overview'),
]
