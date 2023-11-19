from src.infra.postgres import PostgresDatabase
from uuid import uuid4, UUID

"""
    The BoughtRepository class is responsible for handling the database operations.
"""


class BoughtRepository:
    def __init__(self):
        self.db = PostgresDatabase()

    def get_boughts(self) -> list:
        result = self.db.get(
            """
                SELECT bg.id, g.name AS game_name, g.price, u.name AS people_bought, bg.created_at AS date_bought FROM bought_game bg
                INNER JOIN 
                    games g 
                ON
                    g.id = bg.game_id
                INNER JOIN 
                    users u
                ON
                    u.id = bg.user_id
            """
        )

        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "game_name": item[1],
                    "price": item[2],
                    "people_bought": item[3],
                    "date_bought": item[4],
                },
                result,
            )
        )

    def get_bought_by_user(self, user_id: UUID) -> list:
        result = self.db.get(
            """
                SELECT bg.id, g.name AS game_name, g.price, u.name AS people_bought, bg.created_at AS date_bought FROM bought_game bg
                INNER JOIN 
                    games g 
                ON
                    g.id = bg.game_id
                INNER JOIN 
                    users u
                ON
                    u.id = bg.user_id
                WHERE u.id = %s
            """,
            (str(user_id),),
        )

        return list(
            map(
                lambda item: {
                    "id": item[0],
                    "game_name": item[1],
                    "price": item[2],
                    "people_bought": item[3],
                    "date_bought": item[4],
                },
                result,
            )
        )

    def purchase(self, body: dict) -> None:
        self.db.execute(
            """
                UPDATE games SET available = False WHERE id = %s
            """,
            (body["game_id"],),
        )

        self.db.execute(
            """
                INSERT INTO bought_game (id, user_id, game_id) VALUES (%s, %s, %s)
            """,
            (str(uuid4()), body["user_id"], body["game_id"]),
        )
