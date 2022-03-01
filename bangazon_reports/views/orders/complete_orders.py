from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all

class CompleteOrdersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                select o.id, u.first_name || ' ' || u.last_name as full_name, o.created_on, SUM(p.price) as total_price
                from bangazon_api_order o
                join auth_user u on o.user_id = u.id
                join bangazon_api_orderproduct op on o.id = op.order_id
                join bangazon_api_product p on op.product_id = p.id
                where o.completed_on is not null
                group by op.order_id                     
            """)
            
            dataset = dict_fetch_all(db_cursor)
            
            complete_orders = []
            
            for row in dataset: 
                order = {
                    'id': row['id'],
                    'full_name': row['full_name'],
                    'created_on': row['created_on'],
                    'total_price': row['total_price']
                }
                
            
                complete_orders.append(order)
            
                
        template = 'orders/complete_orders.html'
        
        context = {
            "completeorders_list": complete_orders
        }
        
        return render(request, template, context)