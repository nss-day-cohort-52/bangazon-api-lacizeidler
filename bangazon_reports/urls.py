from .views import TopProductList
from django.urls import path

urlpatterns = [
    path('20products', TopProductList.as_view())
]
