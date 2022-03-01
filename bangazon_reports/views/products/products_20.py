from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all

class TopProductList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                select name, quantity
                from bangazon_api_orderproduct o
                join bangazon_api_product p on o.product_id = p.id
                group by p.name 
                order by quantity desc 
                limit 20                       
            """)
            
            dataset = dict_fetch_all(db_cursor)
            
            products_by_quantity = []
            
            for row in dataset: 
                product = {
                    'name': row['name'],
                    'quantity': row['quantity']
                }
                
            
                products_by_quantity.append(product)
            
                
        template = 'products/list_with_20_products.html'
        
        context = {
            "productquantity_list": products_by_quantity
        }
        
        return render(request, template, context)