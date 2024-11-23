from flask import Flask,render_template

def create_app():
    app = Flask(__name__) #initialize app
    app.config['SECRET_Key'] = 'RANDOMWORDASAHDALSFAS'
    
    from  .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    return app