from flask_restx import Namespace, Api
from flask import Flask, request, jsonify

class CustomNamespace(Namespace):
    def route(self, *args, **kwargs):
        # Check if the route requires authorization
        authorize = kwargs.pop("authorize", True)
        original_route = super().route(*args, **kwargs)

        def wrapper(func):
            if authorize:
                def protected_func(*func_args, **func_kwargs):
                    # Perform authorization check
                    if not self.is_authorized():
                        return jsonify({"message": "Unauthorized"}), 401
                    return func(*func_args, **func_kwargs)

                return original_route(protected_func)
            else:
                return original_route(func)

        return wrapper

    def is_authorized(self):
        # A simple authorization check (e.g., checking for an API key)
        api_key = request.headers.get("Authorization")
        return api_key == "my-secret-api-key"

# Define a Protected Route

app = Flask(__name__)
api = Api(app)

# Create an instance of SyntacticNamespace
protected_ns = CustomNamespace("protected", description="Protected API endpoints")

# Define a protected route
@protected_ns.route("/secure-data", authorize=True)
def secure_data():
    return {"message": "This is secured data"}

# Define an unprotected route
@protected_ns.route("/public-data", authorize=False)
def public_data():
    return {"message": "This is public data"}

api.add_namespace(protected_ns)

if __name__ == "__main__":
    app.run(debug=True)
