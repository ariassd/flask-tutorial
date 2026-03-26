from flask import Blueprint, render_template, request

calculator_bp = Blueprint('calculator', __name__, template_folder='templates')


@calculator_bp.route('/bmicalc', methods=['POST', 'GET'])
def bmicalc():
    if request.method == 'POST':
        height = request.form['height']
        height = float(height)
        mass = request.form['mass']
        mass = float(mass)
        bmi = mass / (height * height)
        return render_template('calculator/bmi.html', bmi=bmi)
    else:
        return render_template('calculator/bmi.html')
