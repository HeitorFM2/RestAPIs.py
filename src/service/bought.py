from src.repository.bought import BoughtRepository
from src.repository.games import GamesRepository

from uuid import UUID
from src.utils.responses import Response
from marshmallow import ValidationError

from src.schemas.bought import AddBoughtSchema

"""
    The BoughtService class is responsible for handling the business logic of the application.
    It is responsible for validating the data and calling the repository to perform the operations.
    The BoughtService class is called by the UsersController class.
"""


class BoughtService:
    def __init__(self):
        self.bought_repository = BoughtRepository()
        self.games_repository = GamesRepository()

    def get_boughts(self) -> Response:
        try:
            return Response.Ok(self.bought_repository.get_boughts())

        except Exception as e:
            print(e)
            return Response.Error(e.__str__())

    def get_bought_by_user(self, user_id: UUID) -> Response:
        try:
            return Response.Ok(self.bought_repository.get_bought_by_user(user_id))

        except Exception as e:
            print(e)
            return Response.Error(e.__str__())

    def purchase(self, body: dict) -> Response:
        try:
            AddBoughtSchema().load(body)

            if not self.games_repository.get_game(body["game_id"]):
                raise Exception("Game not found or already purchased!")

            self.bought_repository.purchase(body)
            return Response.Ok(message="Successful purchase!", data=None)

        except ValidationError as e:
            return Response.Error(e.__str__())
        except Exception as e:
            return Response.Error(e.__str__())
