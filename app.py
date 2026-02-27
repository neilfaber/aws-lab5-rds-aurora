from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host='lab5-mysql-db.cwdk48qc01mg.us-east-1.rds.amazonaws.com',
    user='admin',
    password='YOUR_PASSWORD',
    database='lab5db'
)

@app.route("/")
def home():
    return "RDS CRUD Application Running"

# CREATE
@app.route("/create", methods=["POST"])
def create_user():
    data = request.json
    cursor = connection.cursor()
    sql = "INSERT INTO users (name,email,is_active,salary) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (data['name'], data['email'], data['is_active'], data['salary']))
    connection.commit()
    return jsonify({"message": "User created"})

# READ
@app.route("/users", methods=["GET"])
def get_users():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return jsonify(result)

# UPDATE
@app.route("/update/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET salary=%s WHERE id=%s", (data['salary'], id))
    connection.commit()
    return jsonify({"message": "User updated"})

# DELETE
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id))
    connection.commit()
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
