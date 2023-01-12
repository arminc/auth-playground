from flask import Flask, request, make_response
from functools import wraps
import jwt
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.model import Principal, Resource, ResourceAction, ResourceList


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
            token = request.headers["Authorization"].replace("Bearer ", "")
            print(token)
            data = jwt.decode(token, "your-256-bit-secret", algorithms=["HS256"])
            print(data)
            return f(
                User(data["org"], data["group"].split(), data["sub"]), *args, **kwargs
            )

        return make_response("Could not verify, Authorization token is missing", 401)

    return decorator


def authorize(user, resource_name, action, res_attr):
    principal = Principal(user.id, user.roles, attr={"org": user.org})
    resource = Resource("a", resource_name, res_attr)
    with CerbosClient(host="http://localhost:3592") as cerbos:
        if cerbos.is_allowed(action, principal, resource):
            return None

    return make_response("Wrong role", 403)


@app.route("/role_needed")
@token_required
def role_needed(user):
    resp = authorize(user, "management", "read", {})
    if resp != None:
        return resp

    return "You have the role"


@app.route("/personal_data/<id>")
@token_required
def personal_data(user, id):
    resp = authorize(user, "personal", "read", {"id": id})
    if resp != None:
        return resp

    return "You are the same user"


@app.route("/org/<id>/data")
@token_required
def org_data(user, id):
    resp = authorize(user, "org", "read", {"id": id})
    if resp != None:
        return resp

    return "You are in the same org"


status_owner = "1234"


@app.route("/cant_change_status_self", methods=["POST"])
@token_required
def cant_change_status_self(user):
    request_data = request.get_json()
    print(user.id)
    print(status_owner)

    resp = authorize(user, "auth", "change", {"id": status_owner})
    if resp != None:
        return resp

    return request_data


if __name__ == "__main__":
    app.run()
