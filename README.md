# Assignment 2 - RDS CRUD Application

Architecture:
EC2 (Ubuntu) running Flask application connected to AWS RDS MySQL.

Database:
Table: users
Datatypes used:
- INT
- VARCHAR
- TEXT
- BOOLEAN
- DECIMAL
- TIMESTAMP

CRUD Operations:
- Create: POST /create
- Read: GET /users
- Update: PUT /update/<id>
- Delete: DELETE /delete/<id>

Security:
- RDS inbound allowed only from EC2 Security Group
