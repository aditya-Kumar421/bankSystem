from django.contrib import admin
from .models import Loan, Transaction


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'principal', 'rate_of_interest', 'period', 'total_amount', 'emi', 'emi_left', 'amount_paid')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan', 'amount', 'type', 'date')