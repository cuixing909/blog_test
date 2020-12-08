# coding=utf8
from flask_restful import Resource

class Test(Resource):

    def __init__(self):
        pass

    def get(self):
        return 'hello world'