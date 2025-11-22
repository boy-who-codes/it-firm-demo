import hashlib
import requests
import os
from urllib.parse import urljoin

class PayU:
    def __init__(self):
        self.merchant_key = os.environ.get('PAYU_MERCHANT_KEY', 'YOUR_MERCHANT_KEY')
        self.merchant_salt = os.environ.get('PAYU_MERCHANT_SALT', 'YOUR_MERCHANT_SALT')
        self.base_url = os.environ.get('PAYU_BASE_URL', 'https://sandboxsecure.payu.in/_payment')
        self.domain = os.environ.get('DOMAIN', 'http://localhost:5000')
        
    def generate_hash(self, data):
        """
        Generate PayU hash for payment request
        """
        # Create hash sequence as per PayU documentation
        hash_sequence = f"{self.merchant_key}|{data['txnid']}|{data['amount']}|{data['productinfo']}|{data['firstname']}|{data['email']}|||||||||||{self.merchant_salt}"
        return hashlib.md5(hash_sequence.encode('utf-8')).hexdigest()
    
    def create_payment_request(self, booking_id, amount, productinfo, firstname, email, phone):
        """
        Create a payment request for PayU
        """
        # Generate unique transaction ID
        txnid = f"TXN{booking_id}{int(amount)}"
        
        # Prepare data for hash generation
        data = {
            'txnid': txnid,
            'amount': str(int(amount)),
            'productinfo': productinfo,
            'firstname': firstname,
            'email': email
        }
        
        # Generate hash
        hash_value = self.generate_hash(data)
        
        # Prepare payment data
        payment_data = {
            'key': self.merchant_key,
            'txnid': txnid,
            'amount': str(int(amount)),
            'productinfo': productinfo,
            'firstname': firstname,
            'email': email,
            'phone': phone,
            'surl': urljoin(self.domain, '/payment/success'),
            'furl': urljoin(self.domain, '/payment/failed'),
            'service_provider': 'payu_paisa',
            'hash': hash_value
        }
        
        return payment_data
    
    def verify_payment_response(self, response_data):
        """
        Verify payment response from PayU
        """
        # Verify hash from PayU response
        if 'hash' not in response_data or 'status' not in response_data:
            return False
            
        # Generate expected hash
        hash_sequence = f"{self.merchant_salt}|{response_data['status']}|||||||||||{response_data.get('email', '')}|{response_data.get('firstname', '')}|{response_data.get('productinfo', '')}|{response_data.get('amount', '')}|{response_data.get('txnid', '')}|{self.merchant_key}"
        expected_hash = hashlib.md5(hash_sequence.encode('utf-8')).hexdigest()
        
        # Compare hashes
        return expected_hash == response_data['hash']

# Create a global instance
payu = PayU()