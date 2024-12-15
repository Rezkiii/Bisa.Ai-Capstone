from flask import Flask, render_template, session, redirect, url_for, request
from functions.auth import auth, init_app
from functions.databases import Database
from functions.cryptograph import validate_cryptography1, validate_number, validate_superbasic,validate_Fusion,validate_Morse,validate_Repetition,validate_cat,validate_pesan,validate_hiu,validate_esp,validate_flag,validate_XOR,validate_ehe

app = Flask(__name__)
app.secret_key = 'ini_password_g_sih'  

db = Database(host='localhost', user='rezki', password='1', database='capstone')
db.connect()


init_app(db)

app.register_blueprint(auth)

def login_required(f):
    """Decorator untuk memeriksa apakah pengguna telah login."""
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth.login'))  
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', endpoint='index') 
@login_required
def index():
    return render_template('index.html')

@app.route('/cryptography1', methods=['POST'], endpoint='cryptography1')  
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

@app.route('/fusion', methods=['POST'], endpoint='fusion')
@login_required
def fusion():
    user_flag = request.form.get('flag')
    validate_Fusion(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/morse', methods=['POST'], endpoint='morse')
@login_required
def morse():
    user_flag = request.form.get('flag')
    validate_Morse(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))


@app.route('/repetition', methods=['POST'], endpoint='repetition')
@login_required
def repetition():
    user_flag = request.form.get('flag')
    validate_Repetition(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/cat', methods=['POST'], endpoint='cat')
@login_required
def cat():
    user_flag = request.form.get('flag')
    validate_cat(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/pesan', methods=['POST'], endpoint='pesan')
@login_required
def pesan():
    user_flag = request.form.get('flag')
    validate_pesan(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/hiu', methods=['POST'], endpoint='hiu')
@login_required
def hiu():
    user_flag = request.form.get('flag')
    validate_hiu(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/esp', methods=['POST'], endpoint='esp')
@login_required
def esp():
    user_flag = request.form.get('flag')
    validate_esp(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/flag', methods=['POST'], endpoint='flag')
@login_required
def flag():
    user_flag = request.form.get('flag')
    validate_flag(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/XOR', methods=['POST'], endpoint='XOR')
@login_required
def flag():
    user_flag = request.form.get('flag')
    validate_XOR(user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))

@app.route('/ehe', methods=['POST'], endpoint='ehe')
@login_required
def flag():
    user_flag = request.form.get('flag')
    validate_ehe (user_flag)  # Validasi flag menggunakan fungsi dari cryptograph.py
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5030, debug=True)
