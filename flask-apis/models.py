from extensions import db
from markupsafe import Markup

class User(db.Model):
    __tablename__ = 'users_list'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    profile_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    is_active = db.Column(db.Boolean(), default=True)
    # products = db.relationship('Product', backref='user', lazy=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id':self.id,
            'username': self.username,
            'profile_name': self.profile_name,
            'email': self.email,
            'is_active': self.is_active,
        }
    def __str__(self):
        return self.username

class Product(db.Model):
    __tablename__ = 'auction_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    image_link = db.Column(db.String(300), nullable=False)
    base_price = db.Column(db.Integer, nullable=False)
    auction_start_date = db.Column(db.DateTime(), nullable=False)
    auction_end_date = db.Column(db.DateTime(), nullable=False)
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

    def json(self, type='live'):
        info = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'base_price': self.base_price,
            'img': self.image_link,
            'highest_bid': 0,
        }
        prod_buyer = ProductBuyer.get_details_from_product(self.id)
        if type == 'live':
            info['end_date'] = self.auction_end_date.strftime("%d-%m-%Y, %H:%M:%S")
            if prod_buyer:
                info['highest_bid'] = prod_buyer.highest_bid
        elif type == 'past':
            info['end_date'] = self.auction_end_date.strftime("%d-%m-%Y, %H:%M:%S")
            if prod_buyer:
                info['buyer'] = User.get_by_id(prod_buyer.user_id).username
                info['highest_bid'] = prod_buyer.highest_bid
            else:
                info['buyer'] = ""
        if type == 'future':
            info['start_date'] = self.auction_start_date.strftime("%d-%m-%Y, %H:%M:%S")
            info['is_future'] = True
        return info

class ProductBuyer(db.Model):
    __tablename__ = 'productbuyer'
    
    # id = db.Column(db.Integer, primary_key=True)
    highest_bid = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users_list.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('auction_items.id'), primary_key=True)
    
    def save(self):
        db.session.add(self)
        db.session.commit()\

    @classmethod
    def get_details_from_product(cls, product_id):
        return cls.query.filter_by(product_id=product_id).first()