from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    #Configurações do banco
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dionis:44718640@localhost/wms_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    #Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Produto
    from .routes import bp as produtos_bp #importa o blueprint das rotas

    app.register_blueprint(produtos_bp) # Registra o blueprint

    return app