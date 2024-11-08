import unittest
from app import create_app, db
from models import Loan

class LoanAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_create_loan(self):
        response = self.client.post('/api/loans', json={
            'loan_amount': 50000,
            'interest_rate': 15.0,
            'loan_duration': 3
        })
        self.assertEqual(response.status_code, 201)

    def test_get_loans(self):
        response = self.client.get('/api/loans')
        self.assertEqual(response.status_code, 200)

    def test_update_loan(self):
        # Use self.loan.id after it has been committed
        loan_id = self.loan.id
        response = self.client.put(f'/api/loans/{loan_id}', json={
            'loan_amount': 1200,
            'interest_rate': 4.5,
            'loan_duration': 24
        })
        self.assertEqual(response.status_code, 200)
    
    def test_delete_loan(self):
        # Use self.loan.id for the delete test
        loan_id = self.loan.id
        response = self.client.delete(f'/api/loans/{loan_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()