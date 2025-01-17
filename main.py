from flask import Flask, request, jsonify, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():

    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    message = data.get('message')


    print(f"Form submitted: {name}, {email}, {phone}, {message}")

    return jsonify({'message': 'Thank you for your message! We will get back to you soon.'}), 200


if __name__ == '__main__':
    app.run(debug=True)