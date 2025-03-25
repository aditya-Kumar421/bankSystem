from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import  Loan, Transaction
from .serializers import LoanSerializer, TransactionSerializer, LoanDetailSerializer
from customer.models import Customer

class LoanCreateView(APIView):
    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentView(APIView):
    def post(self, request, loan_id):
        loan = get_object_or_404(Loan, id=loan_id)
        amount = float(request.data.get("amount"))
        payment_type = request.data.get("type", "EMI").upper()

        if payment_type == "EMI" and amount != float(loan.emi):
            return Response({"error": "EMI payment must be exactly the EMI amount"}, status=status.HTTP_400_BAD_REQUEST)

        transaction = Transaction.objects.create(loan=loan, amount=amount, type=payment_type)
        return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)


class LoanLedgerView(APIView):
    def get(self, request, loan_id):
        loan = get_object_or_404(Loan, id=loan_id)
        data = LoanDetailSerializer(loan).data
        return Response(data, status=status.HTTP_200_OK)


class CustomerLoansView(APIView):
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        loans = Loan.objects.filter(customer=customer)
        return Response(LoanSerializer(loans, many=True).data, status=status.HTTP_200_OK)
