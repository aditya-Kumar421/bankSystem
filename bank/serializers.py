from rest_framework import serializers
from .models import Loan, Transaction



class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class LoanDetailSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'principal', 'rate_of_interest', 'period', 'total_amount', 'emi', 'emi_left', 'amount_paid', 'transactions']
