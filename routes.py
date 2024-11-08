from flask import Blueprint, request, jsonify
from models import db, Loan

api = Blueprint('api', __name__)

@api.route('/loans', methods=['POST'])
def create_loan():
    data = request.get_json()
    loan = Loan(
        loan_amount=data['loan_amount'],
        interest_rate=data['interest_rate'],
        loan_duration=data['loan_duration']
    )
    db.session.add(loan)
    db.session.commit()
    return jsonify({'message': 'Loan created', 'loan': loan.id}), 201

@api.route('/loans', methods=['GET'])
def get_loans():
    loans = Loan.query.all()
    return jsonify([{'id': loan.id, 'loan_amount': loan.loan_amount, 'interest_rate': loan.interest_rate, 'loan_duration': loan.loan_duration} for loan in loans])

@api.route('/loans/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    data = request.get_json()
    loan = Loan.query.get_or_404(loan_id)
    loan.loan_amount = data['loan_amount']
    loan.interest_rate = data['interest_rate']
    loan.loan_duration = data['loan_duration']
    db.session.commit()
    return jsonify({'message': 'Loan updated'})

@api.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    db.session.delete(loan)
    db.session.commit()
    return jsonify({'message': 'Loan deleted'})