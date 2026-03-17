from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'Hello from flask'

@app.route('/products/<string:name>')
def product(name):
    return f'Product {name}'

app.run(host='0.0.0.0', port=5000)