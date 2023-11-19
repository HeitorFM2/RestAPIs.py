from flask import Blueprint, request
from src.service.users import UsersService

users = Blueprint("users", __name__)

users_service = UsersService()

"""
    The UsersController class is responsible for handling the requests and returning the responses.
"""


@users.route("/users", methods=["GET"])
def get_users():
    return users_service.get_users()


@users.route("/user/<uuid:id>", methods=["GET"])
def get_user(id):
    return users_service.get_user(id)


@users.route("/user", methods=["POST"])
def add_user():
    return users_service.add_user(request.get_json())


@users.route("/user/<uuid:id>", methods=["PUT"])
def update_user(id):
    return users_service.update_user(id, request.get_json())


@users.route("/user/<uuid:id>", methods=["DELETE"])
def delete_user(id):
    return users_service.delete_user(id)
