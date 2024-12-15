from flask import Flask, render_template, session, redirect, url_for, request
from functions.auth import auth, init_app
from functions.databases import Database
from functions.cryptograph import validate_cryptography1, validate_number, validate_superbasic

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia Anda

# Inisialisasi database
db = Database(host='localhost', user='rezki', password='1', database='capstone')
db.connect()

# Inisialisasi aplikasi auth dengan objek db
init_app(db)

app.register_blueprint(auth)

def login_required(f):
    """Decorator untuk memeriksa apakah pengguna telah login."""
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login'))  # Mengarah ke login
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', endpoint='index')  # Endpoint eksplisit
@login_required
def index():
    return render_template('index.html')

@app.route('/cryptography1', methods=['POST'], endpoint='cryptography1')  # Tambahkan endpoint eksplisit
@login_required
def cryptography1():
    user_flag = request.form.get('flag')
    validate_cryptography1(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/number', methods=['POST'], endpoint='number')
@login_required
def number():
    user_flag = request.form.get('flag')
    validate_number(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/superbasic', methods=['POST'], endpoint='superbasic')
@login_required
def superbasic():
    user_flag = request.form.get('flag')
    validate_superbasic(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
