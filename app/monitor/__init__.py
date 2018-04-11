from flask import Blueprint

bp = Blueprint('monitor', __name__)

from app.monitor import routes_memory
from app.monitor import routes_cpu
