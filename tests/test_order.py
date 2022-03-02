from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.core.management import call_command
from django.contrib.auth.models import User

from bangazon_api.models import Order, Product
from bangazon_api.models.order_product import OrderProduct
from bangazon_api.models.payment_type import PaymentType


class OrderTests(APITestCase):
    def setUp(self):
        """
        Seed the database
        """
        call_command('seed_db', user_count=3)
        self.user1 = User.objects.filter(store=None).first()
        self.token = Token.objects.get(user=self.user1)

        self.user2 = User.objects.filter(store=None).last()
        product = Product.objects.get(pk=1)

        self.order1 = Order.objects.create(
            user=self.user1
        )

        self.order1.products.add(product)

        self.order2 = Order.objects.create(
            user=self.user2
        )

        self.order2.products.add(product)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        self.payment_type = PaymentType()
        self.payment_type.merchant_name = "Discover"
        self.payment_type.acct_number = "6482548268882451"
        self.payment_type.customer_id = self.user1.id
        self.payment_type.save()

    def test_list_orders(self):
        """The orders list should return a list of orders for the logged in user"""
        response = self.client.get('/api/orders')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_delete_order(self):
        response = self.client.delete(f'/api/orders/{self.order1.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_complete_order(self):
        url = f'/api/orders/{self.order1.id}/complete'
        orderObj = {
            "paymentTypeId": self.payment_type.id
        }
        response = self.client.put(url, orderObj, format='json')
        order = Order.objects.get(pk=self.order1.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(order.payment_type_id, self.payment_type.id)
        self.assertIsNotNone(order.completed_on)

    def test_add_product(self):
        """
        Ensure we can create a new orderproduct object.
        """
        product = Product.objects.first()
        
        response = self.client.post(f'/api/products/{product.id}/add_to_order', format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # order_product = OrderProduct.objects.get(order_id=data['orderId'], product_id=data['productId'])

        # self.assertIsNotNone(order_product)
        