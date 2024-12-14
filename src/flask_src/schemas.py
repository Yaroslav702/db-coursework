from marshmallow import Schema, fields, ValidationError, validates_schema


class UserReadSchema(Schema):
    class Meta:
        fields = ['id', 'first_name', 'last_name']


class UserCreateSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True, validate=lambda s: len(s) >= 8)


class UpdateUserSchema(Schema):
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    password = fields.Str(required=False, validate=lambda s: len(s) >= 8)

    @validates_schema
    def validate(self, data, **kwargs):
        if not data:
            raise ValidationError("At least one field must be provided for update.")


user_read_schema = UserReadSchema()
users_read_schema = UserReadSchema(many=True)

user_create_schema = UserCreateSchema()

user_update_schema = UpdateUserSchema()
