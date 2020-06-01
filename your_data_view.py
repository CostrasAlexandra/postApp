from flask import Blueprint

example_blueprint = Blueprint('your_data_view', __name__)

@example_blueprint.route('/your_data')
def index():
    return "This is an example app"