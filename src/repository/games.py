from src.infra.postgres import PostgresDatabase
from uuid import uuid4, UUID

"""
    The GamesRepository class is responsible for handling the database operations.
"""


class GamesRepository:
    def __init__(self):
        self.db = PostgresDatabase()

    def get_games(self) -> list:
        result = self.db.get(
            """
                SELECT id, name, description, price, created_at FROM games WHERE available = True
            """
        )

        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "name": item[1],
                    "description": item[2],
                    "price": item[3],
                    "created_at": item[4],
                },
                result,
            )
        )

    def get_game(self, id: UUID) -> list:
        result = self.db.get(
            """
                SELECT id, name, description, price, created_at FROM games WHERE available = True AND id = %s
            """,
            (str(id),),
        )

        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "name": item[1],
                    "description": item[2],
                    "price": item[3],
                    "created_at": item[4],
                },
                result,
            )
        )

    def add_game(self, body: dict) -> None:
        self.db.execute(
            """
                INSERT INTO games (id, name, description, price) VALUES (%s, %s, %s, %s)
            """,
            (str(uuid4()), body["name"], body["description"], body["price"]),
        )

    def update_game(self, id: UUID, body: dict) -> None:
        self.db.execute(
            """
                UPDATE games SET name = %s, description = %s, price = %s WHERE id = %s
            """,
            (body["name"], body["description"], body["price"], str(id)),
        )

    def delete_game(self, id: UUID) -> None:
        self.db.execute(
            """
                UPDATE games SET available = False, deleted_at = NOW() WHERE id = %s
            """,
            (str(id),),
        )
