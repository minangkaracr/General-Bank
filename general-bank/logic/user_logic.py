from flask import jsonify

def home():
    return jsonify({
        'message':'Selamat Datang di Aplikasi.'
    })