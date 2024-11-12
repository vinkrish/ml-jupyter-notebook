from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Endpoint to make a GET request
@app.route('/external-get', methods=['GET'])
def external_get():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    headers = {
        "Authorization": "Bearer your_token",
        "Content-Type": "application/json"
    }
    params = {"q": "python", "sort": "stars"}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return jsonify(data), response.status_code

# Endpoint to make a POST request
@app.route('/external-post', methods=['POST'])
def external_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return jsonify(data), response.status_code

# Endpoint to make a PUT request
@app.route('/external-put/<int:id>', methods=['PUT'])
def external_put(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    payload = {
        "id": id,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, json=payload, headers=headers)
    data = response.json()
    return jsonify(data), response.status_code

# Endpoint to make a DELETE request
@app.route('/external-delete/<int:id>', methods=['DELETE'])
def external_delete(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.delete(url)
    return jsonify({"message": "Deleted"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)


# Handling Errors and Timeout

try:
    response = requests.get('url', timeout=5)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
except requests.exceptions.Timeout:
    # return jsonify({"error": "Request timed out"}), 504
    pass
except requests.exceptions.RequestException as e:
    # return jsonify({"error": str(e)}), 500
    pass