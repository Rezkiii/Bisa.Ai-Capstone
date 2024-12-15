# functions/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth = Blueprint('auth', __name__)
db = None  # Inisialisasi db sebagai None

def init_app(database):
    global db
    db = database

# Fungsi login_required untuk memeriksa apakah pengguna telah login
def login_required(f):
    """Decorator untuk memeriksa apakah pengguna telah login."""
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login'))  # Mengarah ke login
        return f(*args, **kwargs)
    return decorated_function

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if db.register_user(username, password):
            flash('Registration successful! Please log in.')
            return redirect(url_for('auth.login'))  # Mengarah ke login
        else:
            flash('Username already exists!')
    
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if db.validate_user(username, password):
            session['username'] = username  # Simpan username dalam session
            flash('Login berhasil!', 'success')  # Pesan sukses
            return redirect(url_for('index'))  # Mengarah ke index
        else:
            flash('Username atau password salah!', 'error')  # Pesan error
    
    return render_template('login.html')


@auth.route('/logout')
def logout():
    """Fungsi untuk logout pengguna."""
    session.pop('username', None)  # Menghapus username dari session
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))  # Kembali ke login
