from .views import TopProductList, InexpensiveProductList
from django.urls import path

urlpatterns = [
    path('20products', TopProductList.as_view()),
    path('inexpensiveProducts', InexpensiveProductList.as_view())
]
