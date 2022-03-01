from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all

class InexpensiveProductList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                select name, price
                from bangazon_api_product p
                where price < 1000                     
            """)
            
            dataset = dict_fetch_all(db_cursor)
            
            products_by_price = []
            
            for row in dataset: 
                product = {
                    'name': row['name'],
                    'price': row['price']
                }
                
            
                products_by_price.append(product)
            
                
        template = 'products/list_inexpensive_products.html'
        
        context = {
            "productprice_list": products_by_price
        }
        
        return render(request, template, context)