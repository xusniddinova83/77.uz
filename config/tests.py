from rest_framework.test import APITestCase

class AddressTests(APITestCase):
    def test_create_address(self):
        data = {
            "street": "123 Main St",
            "city": "Tashkent",
            "state": "Tashkent Region",
            "zip_code": "100100"
        }
        response = self.client.post('/api/address/', data)
        self.assertEqual(response.status_code, 201)
