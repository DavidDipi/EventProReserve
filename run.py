"""from flask import Flask
from blueprints.admin import admin_blueprint
from blueprints.client import client_blueprint
from blueprints.ini import ini_blueprint
from blueprints.events.typeevents import admin_blueprint
# from flask_mysqldb import MySQL,MySQLdb
from flaskext.mysql import MySQL
from config import MYSQL_DATABASE_HOST, MYSQL_DATABASE_USER, MYSQL_DATABASE_PORT, MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_DB

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = MYSQL_DATABASE_HOST
app.config['MYSQL_DATABASE_USER'] = MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PORT'] = MYSQL_DATABASE_PORT
app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = MYSQL_DATABASE_DB
mysql = MySQL()
mysql.init_app(app)


app.register_blueprint(admin_blueprint)
app.register_blueprint(client_blueprint)
app.register_blueprint(ini_blueprint)"""

from app import app


if __name__ == '__main__':
    app.run(debug=True)
