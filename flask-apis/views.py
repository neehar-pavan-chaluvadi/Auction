from flask_restful import Resource
from flask import request
from flask_cors import cross_origin
from models import User, Product, ProductBuyer
from http import HTTPStatus
from utils import hash_password, check_password
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    unset_jwt_cookies,
)
from datetime import datetime

class RegisterUser(Resource):
    @cross_origin()
    def post(self):
        """
        To register new user
        Method: POST
        """
        json_data = request.get_json()
        username = json_data.get('username')
        profile_name = json_data.get('profile_name')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')
        if User.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST
        if User.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST
        password = hash_password(non_hash_password)
        user = User(username=username, profile_name=profile_name, email=email, password=password)
        user.save()
        data = user.json()
        return data, HTTPStatus.CREATED

class UserLogin(Resource):
    @cross_origin()
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.get_by_email(email=email)
        if not user or not check_password(password, user.password):
            return ({
                        'message': 'email or password is incorrect'
                    }, HTTPStatus.UNAUTHORIZED
            )
        access_token = create_access_token(identity=user.id, fresh=True)
        return (
            {
                'access_token': access_token,
                'username': user.username,
                'profile_name': user.profile_name
            },
            HTTPStatus.OK
        )

class Person(Resource):
    @jwt_required(optional=True)
    def get(self, user_id=""):
        """
        To get more details about users
        Method: GET
        """
        if user_id:
            user = User.get_by_id(user_id=user_id)
            if user is None:
                return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
            return user.json(), HTTPStatus.OK
        data = []
        for user in User.query.all():
            data.append(user.json())
        return data, HTTPStatus.OK
    
    @jwt_required(optional=True)
    def put(self):
        """
        TO update/modify profile name of a user
        method: PUT
        """
        json_data = request.get_json()
        username = json_data.get('username')
        new_profile_name = json_data.get('profile_name')
        user = User.get_by_username(username=username)
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
        user.profile_name = new_profile_name
        user.save()
        return {"success": True, "message":"Updated profile_name"}, HTTPStatus.OK

    @cross_origin()
    @jwt_required(optional=True)
    def delete(self, user_id=""):
        """
        Delete User
        :method: DELETE
        """
        if user_id:
            user = User.get_by_id(user_id=user_id)
            if user is None:
                return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
            user.delete_from_db()
            return {'message': 'User deleted successfully'}, HTTPStatus.OK
        return {"message":'missing user_id'}, HTTPStatus.BAD_REQUEST
            

class ProductCatalogue(Resource):
    @cross_origin()
    @jwt_required(optional=True)
    def get(self):
        """
        List all the action products
        """
        args = request.args
        type = args.get('type','live')
        today_datetime = datetime.now()
        if type == "past":
            items_list = Product.query.filter(Product.auction_end_date < today_datetime).all()
            return {
                'items': [item.json(type=type) for item in items_list]
            }
        elif type == 'live':
            items_list = Product.query.filter(
                Product.auction_start_date < today_datetime, Product.auction_end_date > today_datetime).all()
        elif type == "future":
            items_list = Product.query.filter(Product.auction_start_date > today_datetime).all()
        return {
            'items': [item.json(type=type) for item in items_list]
        }
    
class UpdateBidAmount(Resource):
    @cross_origin()
    @jwt_required(optional=True)
    def put(self):
        """
        Update bid amount while action is in progress
        request body should contain username, product_id and amount
        """
        json_data = request.get_json()
        username = json_data.get('username')
        product_id = json_data.get('product_id')
        amount = json_data.get('amount')
        user = User.get_by_username(username=username)
        product = Product.get_product_from_id(pid=product_id)
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
        if product is None:
            return {'message': 'product not found'}, HTTPStatus.NOT_FOUND
        prod_obj = ProductBuyer.get_details_from_product(product.id)
        if prod_obj:
            prod_obj.highest_bid = amount
            prod_obj.user_id = user.id
            prod_obj.save()
        else:
            new_obj = ProductBuyer(user_id=user.id, product_id=product.id, highest_bid=amount)
            new_obj.save()
        return {"success": True, "message":"product bid amount updated"}, HTTPStatus.OK