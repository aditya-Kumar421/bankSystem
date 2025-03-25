from django.db import models
from customer.models import Customer
from decimal import Decimal

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="loans")
    principal = models.DecimalField(max_digits=12, decimal_places=2)  
    rate_of_interest = models.DecimalField(max_digits=5, decimal_places=2)  
    period = models.IntegerField()  
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    emi = models.DecimalField(max_digits=12, decimal_places=2, default=0) 
    emi_left = models.IntegerField(default=0)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0) 

    def save(self, *args, **kwargs):
        """Calculate Interest, Total Amount, and EMI"""
        interest = (self.principal * self.period * self.rate_of_interest) / 100
        self.total_amount = self.principal + interest
        self.emi = self.total_amount / (self.period * 12) 
        self.emi_left = self.period * 12
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Loan {self.id} - {self.customer.name}"

class Transaction(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=[('EMI', 'EMI'), ('LUMP_SUM', 'LUMP_SUM')])

    def save(self, *args, **kwargs):
        """Update Loan Balance"""
        self.amount = Decimal(self.amount)
        self.loan.amount_paid += self.amount
        if self.type == 'EMI':
            self.loan.emi_left -= 1
        else:  
            remaining = self.loan.total_amount - self.loan.amount_paid
            self.loan.emi_left = max(0, round(remaining / self.loan.emi))

        self.loan.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} - {self.amount} for Loan {self.loan.id}"
