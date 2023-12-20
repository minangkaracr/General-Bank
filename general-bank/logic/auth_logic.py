from flask import Blueprint, jsonify
from functions.database import cursor, conn
import bcrypt
from datetime import datetime, timezone
import pytz

auth_blueprint = Blueprint('auth', __name__)
now = datetime.now()
tmzone = pytz.timezone('Asia/Jakarta')
date_now = tmzone.localize(now).strftime("%Y-%m-%d %H:%M:%S")

def register(request):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password').encode('utf-8') # mengubah ke byte
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    address = data.get('address')
    dob = data.get('dob')
    cust_type = data.get('cust_type')
    
    cursor.execute("select username, email_address from customer c where username = %s or email_address = %s", (username, email,))
    user = cursor.fetchone()
    
    if user:
        return jsonify({
            'message':'User already exist.'
        })
    
    # hashing password using bcrypt
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    
    try:
        cursor.execute("INSERT INTO public.customer (id, username, password, email_address, first_name, last_name, address, dob, created_at) VALUES(nextval('customer_id_seq'::regclass), %s, %s, %s, %s, %s, %s, %s, %s)",(username, hashed_password.decode('utf-8'),email, first_name, last_name, address, dob, date_now))
        conn.commit()
        
        cursor.execute("INSERT INTO public.customer_type (id, customer_type, last_update) VALUES(nextval('customer_type_id_seq'::regclass), %s, %s)",(cust_type, date_now,))
        conn.commit()
        
        return jsonify({
            'message':'User successfully registered.'
        })
    except Exception as e:
        conn.rollback()  # Mengembalikan transaksi jika ada kesalahan
        return jsonify({'message': 'Failed to register user.', 'error': str(e)})
    