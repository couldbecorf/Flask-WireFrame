# The almighty flask import
from flask import Flask

# route/setting imports
from extensions import db, bcrypt
from routes.indexRoute import indexRoute

# Flask configuration
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hauntAdmin.db'

# Register all blueprints
routes = [indexRoute]
for x in routes:
    app.register_blueprint(x)

# initialize databse
db.init_app(app)
bcrypt.init_app(app)

# run the webserver
if __name__ == "__main__":
    app.run()

