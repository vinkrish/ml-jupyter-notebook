user = {"username": "jose", "access_level": "admin"}


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())

# -- keeping function name and docstring --
import functools


user = {"username": "jose", "access_level": "guest"}


def make_secure2(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure2
def get_admin_password2():
    return "1234"

print(get_admin_password())
