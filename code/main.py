from flask import Flask, request, make_response
from functools import wraps
import jwt


app = Flask(__name__)


class User:
    def __init__(self, org, roles, id):
        self.org = org
        self.roles = roles
        self.id = id


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].replace('Bearer ', '')
            print(token)
            data = jwt.decode(token, "your-256-bit-secret", algorithms=["HS256"])
            print(data)
            return f(
                User(data["org"], data["group"].split(), data["sub"]), *args, **kwargs
            )

        return make_response("Could not verify, Authorization token is missing", 401)

    return decorator


@app.route("/role_needed")
@token_required
def role_needed(user):
    if "ADMIN_X" in user.roles:
        return "You have the role"
    return make_response("Wrong role", 403)


# Not checking any roles here
@app.route("/personal_data/<id>")
@token_required
def personal_data(user, id):
    if user.id == id:
        return "You are the same user"
    return make_response("You don't own this data", 403)


# Not checking any roles here
@app.route("/org/<id>/data")
@token_required
def org_data(user, id):
    if user.org == id:
        return "You are in the same org"
    return make_response("You are not part of this org", 403)


status_owner = "1234"


@app.route("/cant_change_status_self", methods=["POST"])
@token_required
def cant_change_status_self(user):
    request_data = request.get_json()
    print(user.id)
    print(status_owner)
    if user.id != status_owner:
        return request_data

    return make_response("You can not change your own state", 403)


if __name__ == "__main__":
    app.run()
