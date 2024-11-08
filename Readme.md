Loan Management System API
This is a RESTful API for a simple Loan Management System built with Flask. The API allows users to create, read, update, and delete (CRUD) loan records.

Table of Contents
Getting Started
API Endpoints
Testing with Postman

Getting Started
Prerequisites
Python 3.8+ installed on your system.
Postman to test API endpoints.
SQLite3 (default for development, but you can configure any RDBMS).

Installation

Clone the Repository:
git clone https://github.com/mekayashwanth/PHP-Backend-Engineer-Take-Home-Assessment-1.git
cd PHP-Backend-Engineer-Take-Home-Assessment-1

Create a Virtual Environment and Activate It:
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt
Set Up the Database: Initialize the database by running:

The API will be running on http://localhost:5000.

API Endpoints
Method Endpoint Description
POST /api/loans Create a new loan
GET /api/loans Retrieve all loans
GET /api/loans/<loan_id> Retrieve a specific loan
PUT /api/loans/<loan_id> Update a specific loan
DELETE /api/loans/<loan_id> Delete a specific loan

Testing with Postman
You can use Postman to test each of the API endpoints. Follow these steps for each operation:

1. Create a Loan
   Request Type: POST
   URL: http://localhost:5000/api/loans
   Headers: Content-Type: application/json
   Body (JSON):
   json
   {
   "loan_amount": 50000,
   "interest_rate": 15.0,
   "loan_duration": 3
   }
   Expected Response: A JSON object confirming loan creation.
2. Retrieve All Loans
   Request Type: GET
   URL: http://localhost:5000/api/loans
   Expected Response: A JSON array containing all loans.
3. Retrieve a Specific Loan
   Request Type: GET
   URL: http://localhost:5000/api/loans/<loan_id>
   Replace <loan_id> with the ID of the loan you wish to retrieve.
   Expected Response: A JSON object with the loan details if found.
4. Update a Loan
   Request Type: PUT
   URL: http://localhost:5000/api/loans/<loan_id>
   Replace <loan_id> with the ID of the loan you wish to update.
   Headers: Content-Type: application/json
   Body (JSON):
   json

   {
   "loan_amount": 60000,
   "interest_rate": 12.0,
   "loan_duration": 5
   }
   Expected Response: A JSON object confirming loan update.

5. Delete a Loan
   Request Type: DELETE
   URL: http://localhost:5000/api/loans/<loan_id>
   Replace <loan_id> with the ID of the loan you wish to delete.
   Expected Response: A JSON message confirming loan deletion.
