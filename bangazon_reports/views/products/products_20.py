from django.shortcuts import render
from django.db import connection
from django.views import View

class TopProductList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                select 
                                      
            """)