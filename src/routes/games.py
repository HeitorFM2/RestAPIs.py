from flask import Blueprint, request
from src.service.games import GamesService

games = Blueprint("games", __name__)
games_service = GamesService()

"""
    The GamesController class is responsible for handling the requests and returning the responses.
"""


@games.route("/games", methods=["GET"])
def get_games():
    return games_service.get_games()


@games.route("/game/<uuid:id>", methods=["GET"])
def get_game(id):
    return games_service.get_game(id)


@games.route("/game", methods=["POST"])
def add_game():
    return games_service.add_game(request.get_json())


@games.route("/game/<uuid:id>", methods=["PUT"])
def update_game(id):
    return games_service.update_game(id, request.get_json())


@games.route("/game/<uuid:id>", methods=["DELETE"])
def delete_game(id):
    return games_service.delete_game(id)
