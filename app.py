"""
Aplicacion Principal
"""
from flask import Flask
from routes.sort import sort_route
from routes.balance import balance_route
from routes.users import users_route
from routes.easteregg import easteregg_route

app = Flask(__name__)

URL_PREFIX_API = '/api/v1'
app.register_blueprint(sort_route, url_prefix=URL_PREFIX_API)
app.register_blueprint(balance_route, url_prefix=URL_PREFIX_API)
app.register_blueprint(users_route, url_prefix=URL_PREFIX_API)
app.register_blueprint(easteregg_route, url_prefix=URL_PREFIX_API)

if __name__ == '__main__':
    app.run()
