from marshmallow import Schema, fields


class ProblemDetailsSchema(Schema):
    status = fields.Int()
    title = fields.Str()
    type = fields.Str()
    details = fields.Str()

