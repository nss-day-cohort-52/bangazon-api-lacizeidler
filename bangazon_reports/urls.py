from .views import TopProductList, InexpensiveProductList, ExpensiveProductList
from django.urls import path

urlpatterns = [
    path('20products', TopProductList.as_view()),
    path('inexpensiveProducts', InexpensiveProductList.as_view()),
    path('expensiveProducts', ExpensiveProductList.as_view())
]
