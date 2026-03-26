import os
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from auth.routes import auth_bp
from calculator.routes import calculator_bp
from user.routes import user_bp

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__, template_folder=str(BASE_DIR / 'templates'))

UPLOAD_FOLDER = BASE_DIR / 'uploads'
if not UPLOAD_FOLDER.exists():
    UPLOAD_FOLDER.mkdir()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(calculator_bp, url_prefix='/calculator')
app.register_blueprint(user_bp, url_prefix='/user')


@app.route('/')
def index():
    username = request.cookies.get('username')
    return render_template('index.html', username=username)


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
