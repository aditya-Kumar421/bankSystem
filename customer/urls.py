from django.urls import path
from .views import CustomerListCreateView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customers'),
]
