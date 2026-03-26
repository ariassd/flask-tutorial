from flask import Blueprint, render_template, request, redirect, url_for, make_response

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        response = make_response(redirect(url_for('index')))
        response.set_cookie('username', user)
        return response
    else:
        return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')
