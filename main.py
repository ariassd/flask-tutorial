import os
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename  # Import secure_filename for safe filenames

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__, template_folder=str(BASE_DIR / 'templates'))

UPLOAD_FOLDER = BASE_DIR / 'uploads'
if not UPLOAD_FOLDER.exists():
    UPLOAD_FOLDER.mkdir()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # user = request.form["username"]
        return redirect(url_for('index'))
        # return redirect(url_for('/', username = user))
        # return render_template('index.html', username=user)
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/author')
def author():
    return 'author page'


@app.route('/copyright')
def copyright():
    return 'Copy right page'


@app.route('/post/<string:name>')
def post(name):
    return f'Post {name}'


@app.route('/hello/<string:name>/<string:last_name>')
def hello2(name, last_name):
    shopping_list = ['bananas', 'apples', 'oranges']
    context = {  # use a dictionary to pass several variables like an object
        'user': {'name': name, 'last_name': last_name},
        'shopping_list': shopping_list,
    }
    return render_template('hello.html', **context)


@app.route('/goodby/<string:name>/<string:last_name>')
def good_bye(name, last_name):
    return f'Goodbye mr/ms {name} {last_name}'


@app.route('/bmi-calc', methods=['POST', 'GET'])
def bim_calc():
    if request.method == 'POST':
        height = request.form['height']
        height = float(height)
        mass = request.form['mass']
        mass = float(mass)
        bmi = mass / (height * height)
        # return redirect(url_for('success', bmi=bmi))
        return render_template('bmi.html', bmi=bmi)
    else:
        return render_template('bmi.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('success', filename=filename))
    else:
        return render_template('upload.html')


@app.route('/success')
def success():
    filename = request.args.get('filename')
    return f'File {filename} uploaded successfully!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
