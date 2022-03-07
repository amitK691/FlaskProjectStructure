from models.base import BaseModel, db
from models.accounts import User





class Land(BaseModel):
    city = db.Column(db.String(120), nullable=False)
    district = db.Column(db.String(120), nullable=False)
    district = db.Column(db.String(120), nullable=False)
    number_street = db.Column(db.Integer(10), nullable=False)
    block_number = db.Column(db.Integer(10), nullable=False)
    direction = db.Column(db.String(120), nullable=False)
    street_angle = db.Column(db.String(120), nullable=False)
    services = db.Column(db.String(120), nullable=False)
    building_number = db.Column(db.Integer(10), nullable=False)
    construction_age = db.Column(db.Integer(10), nullable=False)
    open_to_bid = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))


