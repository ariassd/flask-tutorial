from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, template_folder='templates')


@user_bp.route('/<string:name>/<string:last_name>')
def user(name, last_name):
    shopping_list = ['bananas', 'apples', 'oranges']
    context = {
        'user': {'name': name, 'last_name': last_name},
        'shopping_list': shopping_list,
    }
    return render_template('/user/hello.html', **context)
