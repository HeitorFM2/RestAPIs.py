from src.repository.users import UsersRepository

from uuid import UUID
from src.utils.responses import Response
from marshmallow import ValidationError

from src.schemas.users import AddUserSchema, UpdateUserSchema

"""
    The UsersService class is responsible for handling the business logic of the application.
    It is responsible for validating the data and calling the repository to perform the operations.
    The UsersService class is called by the UsersController class.
"""


class UsersService:
    def __init__(self):
        self.users_repository = UsersRepository()

    def get_users(self) -> Response:
        try:
            return Response.Ok(self.users_repository.get_users())

        except Exception as e:
            print(e)
            return Response.Error(e.__str__())

    def get_user(self, id: UUID) -> Response:
        try:
            return Response.Ok(self.users_repository.get_user(id))

        except Exception as e:
            print(e)
            return Response.Error(e.__str__())

    def add_user(self, body: dict) -> Response:
        try:
            AddUserSchema().load(body)
            self.users_repository.add_user(body)
            return Response.Created(body)

        except ValidationError as e:
            return Response.Error(e.__str__())
        except Exception as e:
            return Response.Error(e.__str__())

    def update_user(self, id: UUID, body: dict) -> Response:
        try:
            UpdateUserSchema().load(body)
            self.users_repository.update_user(id, body)
            return Response.Ok(None)

        except ValidationError as e:
            return Response.Error(e.__str__())
        except Exception as e:
            return Response.Error(e.__str__())

    def delete_user(self, id: UUID) -> Response:
        try:
            self.users_repository.delete_user(id)
            return Response.Ok(None)

        except ValidationError as e:
            return Response.Error(e.__str__())
        except Exception as e:
            return Response.Error(e.__str__())
