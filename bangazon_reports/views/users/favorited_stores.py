from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all


class FavoritedStoreList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                select u.id, u.first_name || ' ' || u.last_name as full_name, s.name
                from auth_user u
                join bangazon_api_favorite f on u.id = f.customer_id
                join bangazon_api_store s on f.store_id = s.id
            """)
            
            dataset = dict_fetch_all(db_cursor)

            stores_by_user = []

            for row in dataset:
                store = {
                    'name': row['name']
                }
                
                user_dict = next(
                    (
                        user_store for user_store in stores_by_user
                        if user_store['id'] == row['id']
                    ),
                    None
                )
                
                if user_dict:
                    user_dict['stores'].append(store)
                else:
                    stores_by_user.append({
                        "id": row['id'],
                        "full_name": row['full_name'],
                        "stores": [store]
                    })
        
        template = 'users/favorite_sellers.html'
        
        context = {
            "userstore_list": stores_by_user
        }

        return render(request, template, context)
