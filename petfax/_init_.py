# config
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the database connection object
db = SQLAlchemy()
# Initialize the migration object
migrate = Migrate()

# Application factory function
def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Set configuration parameters
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")  # Database URI from environment variable
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable tracking modifications to save resources

    # Import and initialize database models
    from . import models
    models.db.init_app(app)

    # Initialize migration management with the app and the database
    migrate = Migrate(app, models.db)

    # Define the index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    # Register the pet blueprint
    from . import pet 
    app.register_blueprint(pet.bp)

    # Register the fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    # Return the Flask application instance
    return app
