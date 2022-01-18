from socket import fromshare
from flask import Blueprint

auth = Blueprint('auth', __name__)

from .import views, froms