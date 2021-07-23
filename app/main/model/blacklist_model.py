from .. import db
import datetime

class BlacklistToken(db.Model):
    """Token model for storing jwt tokens."""
    
    __tablename__ = 'blacklist_token'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()
        
    def __repr__(self):
        return f'<id: token: {self.token}>'
    
    @staticmethod
    def check_blacklist(auth_token):
        """check whether auth token fas been blacklisted"""
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False