import time
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        12345: {'username': 'Paul', 'email': 'paul@paul.com'},
        54321: {'username': 'Rory', 'email': 'rory@rory.com'}
    }

    user_data = users.get(user_id)

    time.sleep(3)

    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)