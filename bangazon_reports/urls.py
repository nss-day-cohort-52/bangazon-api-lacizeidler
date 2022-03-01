from .views import TopProductList, InexpensiveProductList, ExpensiveProductList, IncompleteOrdersList, CompleteOrdersList
from django.urls import path

urlpatterns = [
    path('20products', TopProductList.as_view()),
    path('inexpensiveProducts', InexpensiveProductList.as_view()),
    path('expensiveProducts', ExpensiveProductList.as_view()),
    path('incompleteOrders', IncompleteOrdersList.as_view()),
    path('completeOrders', CompleteOrdersList.as_view())
]
