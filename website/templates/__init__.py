from flask import Flask

def create_app()
    app = Flask(__name__) #initialize app
    app.config['SECRET_Key'] = 'RANDOMWORDASAHDALSFAS'

    return app