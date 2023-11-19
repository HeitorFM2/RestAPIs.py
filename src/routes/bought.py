from flask import Blueprint, request
from src.service.bought import BoughtService

bought = Blueprint("bought", __name__)

bought_service = BoughtService()

"""
    The BoughtController class is responsible for handling the requests and returning the responses.
"""


@bought.route("/boughts", methods=["GET"])
def get_boughts():
    return bought_service.get_boughts()


@bought.route("/boughts/<uuid:user_id>", methods=["GET"])
def get_bought_by_user(user_id):
    return bought_service.get_bought_by_user(user_id)


@bought.route("/bought", methods=["POST"])
def purchase():
    return bought_service.purchase(request.get_json())
