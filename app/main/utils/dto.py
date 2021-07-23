from flask_restplus import Namespace, fields


class UserDTO:
    user_namespace = Namespace('user', description='user related operations')
    user = user_namespace.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(required=False, description='user public_id')
    })
    
    
class AuthDTO:
    auth_namespace = Namespace('auth', description='authentication related operations')
    user_auth = auth_namespace.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })
    
