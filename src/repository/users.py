from src.infra.postgres import PostgresDatabase
from uuid import uuid4, UUID

"""
    The UsersRepository class is responsible for handling the database operations.
"""


class UsersRepository:
    def __init__(self):
        self.db = PostgresDatabase()

    def get_users(self) -> list:
        result = self.db.get(
            """
                SELECT id, name, mail, created_at FROM users WHERE is_active = True
            """
        )

        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "name": item[1],
                    "mail": item[2],
                    "created_at": item[3],
                },
                result,
            )
        )

    def get_user(self, id: UUID) -> list:
        result = self.db.get(
            """
                SELECT id, name, mail, created_at FROM users WHERE is_active = True AND id = %s
            """,
            (str(id),),
        )

        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "name": item[1],
                    "mail": item[2],
                    "created_at": item[3],
                },
                result,
            )
        )

    def add_user(self, body: dict) -> None:
        self.db.execute(
            """
                INSERT INTO users (id, name, mail) VALUES (%s, %s, %s)
            """,
            (str(uuid4()), body["name"], body["mail"]),
        )

    def update_user(self, id: UUID, body: dict) -> None:
        self.db.execute(
            """
                UPDATE users SET name = %s, mail = %s WHERE id = %s
            """,
            (body["name"], body["mail"], str(id)),
        )

    def delete_user(self, id: UUID) -> None:
        self.db.execute(
            """
                UPDATE users SET is_active = False, deleted_at = NOW() WHERE id = %s
            """,
            (str(id),),
        )
