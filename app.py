from flask import Flask, render_template, request, Response, redirect, url_for, flash
from database.data_psql import get_connection
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config

#Models
from models.ModelUser import ModelUser

#Entities

from models.entities.User import User

def crear_app():
    app = Flask(__name__)

    csrf = CSRFProtect()
    login_manager_app = LoginManager(app)

    @login_manager_app.user_loader
    def load_user(id):
        return ModelUser.get_by_id(id)

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login', methods = ['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User(0, request.form['username'],request.form['password'])
            logged_user = ModelUser.login(user)
            if logged_user != None:
                if logged_user.password:
                    login_user(logged_user)
                    return redirect(url_for('home'))
                else:
                    flash("Invalid password!:...")
                    return render_template('auth/login.html') 
            else:
                flash ("User no found!....")
                return render_template('auth/login.html')
        else:
            return render_template('auth/login.html')

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect (url_for('login'))

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/protected')
    @login_required
    def protected():
        return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


    def status_401(error):
        return redirect(url_for('login'))


    def status_404(error):
        return "<h1>Página no encontrada</h1>", 404

    app.config.from_object(config['development'])
    app.secret_key = 'supersecretkey'
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()

    return app

if __name__ == '__main__':
    app=crear_app()
    app.run()
