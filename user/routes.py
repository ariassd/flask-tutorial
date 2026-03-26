from flask import Blueprint, render_template, request, redirect, url_for

user_bp = Blueprint('user', __name__, template_folder='templates')


@user_bp.route('/<string:name>/<string:last_name>')
def user(name, last_name):
    shopping_list = ['bananas', 'apples', 'oranges']
    context = {
        'user': {'name': name, 'last_name': last_name},
        'shopping_list': shopping_list,
    }
    return render_template('/user/hello.html', **context)


@user_bp.route('/edit', methods=['GET'])
def edit():
    # In a real application, you would fetch the user from a database
    # For this example, we'll use a mock user
    user = {'username': 'john_doe', 'email': 'john@example.com'}
    return render_template('user/edit.html', user=user)


@user_bp.route('/update', methods=['POST'])
def update():
    # Handle the form submission here
    # In a real application, you would update the user in a database
    username = request.form['username']
    email = request.form['email']

    # For this example, we'll just redirect back to the home page
    return redirect(url_for('user.index'))
