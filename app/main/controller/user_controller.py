from flask import request
from flask_restplus import Resource

from ..utils.dto import UserDTO
from ..service.user_service import save_new_user, get_a_user, get_all_users

api = UserDTO.user_namespace
_user = UserDTO.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_od_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all users"""
        return get_all_users()
    
    @api.response(201, 'User successfully created')
    @api.doc('create a ner user')
    @api.expected(_user, validate=True)
    def post(self):
        """Create a new user"""
        data =request.json
        return save_new_user(data=data)
    

@api.route('/<public_id>')
@api.param('public_id', 'The user identifiers')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user