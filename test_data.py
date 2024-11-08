# test_data.py
from models import db, Loan
from app import create_app

app = create_app()

with app.app_context():
    sample_loans = [
        Loan(loan_amount=50000, interest_rate=15.0, loan_duration=3),
        Loan(loan_amount=20000, interest_rate=10.0, loan_duration=5),
        Loan(loan_amount=75000, interest_rate=12.5, loan_duration=2),
    ]
    db.session.bulk_save_objects(sample_loans)
    db.session.commit()
    print("Sample data added.")
