from marshmallow import Schema, fields, validate


class AddUserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    mail = fields.Email(required=True, validate=validate.Length(min=5, max=255))


class UpdateUserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    mail = fields.Email(required=True, validate=validate.Length(min=5, max=255))
