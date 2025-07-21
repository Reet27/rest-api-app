from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = {}
user_id_counter = 1

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Add a new user
@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.json
    user = {
        "id": user_id_counter,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users[user_id_counter] = user
    user_id_counter += 1
    return jsonify(user), 201

# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify(users[user_id]), 200

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify(deleted_user), 200

if __name__ == '__main__':
    app.run(debug=True)
