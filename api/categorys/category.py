from flask import Flask, Blueprint
from api.categorys.CategoryAPI import CategoryAPI

category = Blueprint('category', __name__)
Category = CategoryAPI()

