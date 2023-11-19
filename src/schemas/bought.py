from marshmallow import Schema, fields, validate


class AddBoughtSchema(Schema):
    game_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
