import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, session, url_for
)
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr import db, login_manager
from .models import User
from .forms import LoginForm, RegisterForm

bp = Blueprint('auth', __name__, url_prefix='/auth')


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.filter_by(id=user_id).first()
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to see this page')
    return redirect(url_for('auth.login'))


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember_me.data
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            login_user(user, remember=remember)
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    for fieldName, errorMessages in form.errors.items():
        for err in errorMessages:
            print(err)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password2 = form.confirm.data
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif password != password2:
            error = 'Passwords must match.'
        elif User.query.filter_by(username=username).first() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            user = User(username, generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html', form=form)
