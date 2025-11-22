import unittest
from app import app
from payu import payu

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_services_page(self):
        result = self.app.get('/services')
        self.assertEqual(result.status_code, 200)

    def test_create_order_endpoint_requires_auth(self):
        result = self.app.post('/api/create-order')
        self.assertEqual(result.status_code, 401)  # Unauthorized

    def test_payu_hash_generation(self):
        # Test PayU hash generation
        data = {
            'txnid': 'TXN123',
            'amount': '100',
            'productinfo': 'Test Product',
            'firstname': 'John',
            'email': 'john@example.com'
        }
        hash_value = payu.generate_hash(data)
        self.assertIsInstance(hash_value, str)
        self.assertEqual(len(hash_value), 32)  # MD5 hash is 32 characters

if __name__ == '__main__':
    unittest.main()