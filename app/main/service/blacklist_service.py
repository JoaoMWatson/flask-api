from app.main import db
from app.main.model.blacklist_model import BlacklistToken

def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        respose_object = {
            'status':'success',
            'message':'Successfully logged out'
        }
        
        return respose_object, 200
    except Exception as e:
        respose_object = {
            'status':'error',
            'message':e
        }
        
        return respose_object, 200