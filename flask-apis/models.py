from extensions import db
from markupsafe import Markup

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    profile_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    is_active = db.Column(db.Boolean(), default=True)
    products = db.relationship('Product', backref='user', lazy=True)

    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self, is_current_user=False):
        info = {
            'id':self.id,
            'username': self.username,
            'is_active': self.is_active,
            'profile_name': self.profile_name
        }
        if is_current_user:
            info['email'] = self.email
        return info
    def __str__(self):
        return self.username

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    image_link = db.Column(db.String(300), nullable=False)
    base_price = db.Column(db.Integer, nullable=False)
    auction_start_date = db.Column(db.DateTime(), nullable=False)
    auction_end_date = db.Column(db.DateTime(), nullable=False)
    highest_bid = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_product_from_id(cls, pid):
        return cls.query.filter_by(id=pid).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self, get_user=False):
        info = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'base_price': self.base_price,
            'img': self.image_link,
        }
        if get_user:
            info['buyer'] = self.user_id.name
        return info
