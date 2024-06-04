from flask import Blueprint, render_template, request
from checker import strength, leak_check

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/check', methods=['POST'])
def check():
    password = request.form['password']
    use_custom_api = 'use_custom_api' in request.form
    custom_api_key = request.form.get('custom_api_key', '')
    
    strength_result = strength.check_strength(password)
    leak_result = leak_check.check_leak(password, use_custom_api, custom_api_key)
    
    return render_template('index.html', strength=strength_result, leak=leak_result)
