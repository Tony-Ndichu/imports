"""

#app/test/test_answers.py
Handles all the tests related to answers
"""
import json
from api import create_app
from flask_testing import TestCase
from api.questions.views import QUESTION_LIST
from api.answers.views import ANSWER_LIST
from import create_tables
from api.database.connect import conn, cur


class Base(TestCase):
    """contains config for testing"""

    def create_app(self):
        """sets config to testing"""
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        create_tables()
        self.signup_details = {
            "first_name" : "John",
            "last_name" : "Doe",
            "username" : "johndoe",
            "email" : "johndoe@gmail.com",
            "password" : "abcd1234"
            }  
                   
        conn

    def tearDown(self):
        """after tests have been executed"""
        del QUESTION_LIST[:]
        del ANSWER_LIST[:]


class TestUsers(Base):
    """contains the test methods"""


    def test_user_can_signup(self):
        """checks that users can add an answer"""

        answer = self.client.post(
            'api/v1/auth/signup',
            data=json.dumps(self.signup_details),
            content_type='application/json')

        self.assertEqual(answer.status_code, 201)

   