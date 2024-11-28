from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia Anda

# Simulasi database menggunakan dictionary
users_db = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users_db.get(email)
        if user and check_password_hash(user['password'], password):
            session['user'] = email
            flash('Login berhasil!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Email atau password salah!', 'danger')
    
    return render_template('Login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if email in users_db:
            flash('Email sudah terdaftar!', 'danger')
        elif password != confirm_password:
            flash('Password tidak cocok!', 'danger')
        else:
            hashed_password = generate_password_hash(password)
            users_db[email] = {'fullname': fullname, 'password': hashed_password}
            flash('Registrasi berhasil! Silakan login.', 'success')
            return redirect(url_for('login'))

    return render_template('Register.html')

@app.route('/profile')
def profile():
    if 'user' in session:
        user_email = session['user']
        user = users_db[user_email]
        return f'Welcome, {user["fullname"]}!'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Anda telah logout.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)