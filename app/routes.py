from flask import Flask
from admin import admin_blueprint
from client import client_blueprint

app = Flask(__name__)

# Registrar los Blueprints
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(client_blueprint, url_prefix='/client')

if __name__ == '__main__':
    app.run(debug=True)
