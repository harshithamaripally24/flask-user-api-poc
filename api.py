from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data 
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "password": "password123", "age": 25},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "password": "pass456", "age": 30}
]

# GET all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Check if required fields are present
    if "name" not in data or "email" not in data or "password" not in data or "age" not in data:
        return jsonify({"message": "Missing required fields"}), 400

    # Create a new user
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
        "age": data["age"]
    }

    users.append(new_user)
    return jsonify(new_user), 201

# DELETE user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted successfully"})

# PUT Method
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((user for user in users if user["id"] == user_id), None)

    if user:
        user.update(data)
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

#PATCH Method
@app.route('/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    data = request.get_json()
    user = next((user for user in users if user["id"] == user_id), None)

    if user:
        user.update(data)
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

        
if __name__ == '_main_':
    app.run(debug=True)