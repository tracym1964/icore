from marshmallow import Schema, fields, ValidationError, validates


class TestApi(Schema):
    test = fields.String(required=True)
