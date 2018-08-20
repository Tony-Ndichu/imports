"""
#app/api/answers/views.py
This is the module that handles question operations and their methods
"""

from flask import Flask, Blueprint
from flask_restful import reqparse, Api, Resource
from ..common import validator
from ..models.user import UserModel

APP = Flask(__name__)


USER_BLUEPRINT = Blueprint('user', __name__)
API = Api(USER_BLUEPRINT, prefix='/api/v1')


class Registration(Resource):
    """
    this class deals with posting questions and getting all questions
    """

    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        type=str,
                        required=True,
                        help='Please enter your first name.',

                        )

    parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help='Please enter your last_name.',

                        )

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Please enter your username.',

                        )

    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='Please enter your email.',

                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Please enter your last_name.',

                        )

    @classmethod
    def post(cls):
        """Handles posting a user's registration"""
        data = cls.parser.parse_args()

        USER_LIST = UserModel.get_all_users()

        exists = validator.check_if_user_exists(
            USER_LIST, data['username'], data['email'])

        if exists:
            return {"message": exists}, 409

        verify_user_details = validator.user_detail_verification(
            data['first_name'], data['last_name'], data['username'])

        if verify_user_details:
            return {"message": verify_user_details}, 409

        create_user = UserModel.create_user(data['first_name'], data['last_name'], data[
                                            'username'], data['email'], data['password'])

        return {'message': 'Success!! User account has been created successfully'}, 201


class Login(Resource):
    """this class handles fetching a specific question and deleting it"""
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Please enter your username.',

                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Please enter your email.',

                        )

    @classmethod
    def post(cls):
        """this handles a user's login"""
        data = cls.parser.parse_args()

        user_check = UserModel.find_by_username(
            data['username'], data['password'])

        if user_check:
            return {"message": user_check}, 200
        return {"message": "Sorry, wrong credentials" }, 200


API.add_resource(Registration, "/auth/signup")
API.add_resource(Login, "/auth/login")


if __name__ == '__main__':
    APP.run()
