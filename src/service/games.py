from src.repository.games import GamesRepository

from uuid import UUID
from src.utils.responses import Response
from marshmallow import ValidationError

from src.schemas.games import AddGamesSchema, UpdateGamesSchema

"""
    The GamesService class is responsible for handling the business logic of the application.
    It is responsible for validating the data and calling the repository to perform the operations.
    The GamesService class is called by the GamesController class.

"""


class GamesService:
    def __init__(self):
        self.games_repository = GamesRepository()

    def get_games(self) -> Response:
        try:
            return Response.Ok(self.games_repository.get_games())

        except Exception as e:
            print(e)
            return Response.Error(e.__str__())

    def get_game(self, id: UUID) -> Response:
        try:
            return Response.Ok(self.games_repository.get_game(id))

        except Exception as e:
            print(e)
            return Response.Error(e.__str__())

    def add_game(self, body: dict) -> Response:
        try:
            AddGamesSchema().load(body)
            self.games_repository.add_game(body)
            return Response.Created(body)

        except ValidationError as e:
            return Response.Error(e.__str__())
        except Exception as e:
            return Response.Error(e.__str__())

    def update_game(self, id: UUID, body: dict) -> Response:
        try:
            UpdateGamesSchema().load(body)
            self.games_repository.update_game(id, body)
            return Response.Ok(None)

        except ValidationError as e:
            return Response.Error(e.__str__())
        except Exception as e:
            return Response.Error(e.__str__())

    def delete_game(self, id: UUID) -> Response:
        try:
            self.games_repository.delete_game(id)
            return Response.Ok(None)

        except ValidationError as e:
            return Response.Error(e.__str__())
        except Exception as e:
            return Response.Error(e.__str__())
