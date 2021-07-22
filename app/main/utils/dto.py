from flask_restplus import Namespace, fields


class UserDTO:
    user_namespace = Namespace('user', description='user related operations')
    user = user_namespace.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(required=True, description='user public_id')
    })