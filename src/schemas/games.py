from marshmallow import Schema, fields, validate


class AddGamesSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(required=True, validate=validate.Length(min=5, max=255))
    price = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="The price value must be greater than 0."),
    )


class UpdateGamesSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(required=True, validate=validate.Length(min=5, max=255))
    price = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="The price value must be greater than 0."),
    )
