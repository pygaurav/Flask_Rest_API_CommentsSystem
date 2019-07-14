from flask import Flask,make_response
from flask_restful import Api,Resource,reqparse,request
# from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
# CORS(app)

from app.conn import ConnectToDB
from app.func.func import Comment
from app.component import component