from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.core.management import call_command
from django.contrib.auth.models import User

from bangazon_api.models.payment_type import PaymentType


class PaymentTests(APITestCase):
    def setUp(self):
        """
        Seed the database
        """
        call_command('seed_db', user_count=5)
        self.user1 = User.objects.filter(store=None).first()
        self.token = Token.objects.get(user=self.user1)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.faker = Faker()


    def test_create_payment_type(self):
        """
        Ensure we can add a payment type for a customer.
        """
        # Add product to order
        data = {
            "merchant": self.faker.credit_card_provider(),
            "acctNumber": self.faker.credit_card_number()
        }

        response = self.client.post('/api/payment-types', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['id'])
        self.assertEqual(response.data["merchant_name"], data['merchant'])
        self.assertEqual(response.data["acct_number"], data['acctNumber'])

    # def test_delete_payment_type(self):
    #     """
    #     Ensure we can delete an existing product.
    #     """

    #     # Create a new instance of product
    #     payment_type = PaymentType()
    #     payment_type.merchant_name = "American Express"
    #     payment_type.acct_number = "7364291236487395"
    #     payment_type.customer_id = 1

    #     # Save the Product to the testing database
    #     payment_type.save()

    #     # Define the URL path for deleting an existing Game
    #     url = f'/paymentType/{payment_type.id}'

    #     # Initiate DELETE request and capture the response
    #     response = self.client.delete(url)

    #     # Assert that the response status code is 204 (NO CONTENT)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #     # Initiate GET request and capture the response
    #     response = self.client.get(url)

    #     # Assert that the response status code is 404 (NOT FOUND)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
