from flask import Flask, render_template, request, redirect, session, flash# flask-> helps to create web app , render_template-> shows html page,request-> gets data from form
import pymysql  #redirect -> move to another page ,session->rember users(login),flash-> show message(success/error),pymsql-> used to connect fask to mysql database
from werkzeug.security import generate_password_hash, check_password_hash#generate_password_hash-> used to encrypt password,heck_password_hash->verify password

#App setup
app = Flask(__name__)# create app
app.config['SECRET_KEY'] = "super_secure_key_change_this"# used for : session security and flash message

# ================= DATABASE =================
def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="flask_auth",
        cursorclass=pymysql.cursors.DictCursor
    )

# ================= HOME =================
@app.route('/')
def home():
    return render_template('login.html')

# ================= REGISTER =================
@app.route('/register', methods=['GET', 'POST'])#get is used for show form and post is used for process data
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = generate_password_hash(request.form.get('password'))

        db = get_db()
        cur = db.cursor()

        cur.execute("SELECT id FROM users WHERE email=%s", (email,))#prevent duplicate users
        if cur.fetchone():
            flash("⚠️ Email already registered", "error")
            return redirect('/register')

        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        db.commit()

        cur.close()
        db.close()

        flash("✅ Registration successful! Please login.", "success")
        return redirect('/')

    return render_template('register.html')

# ================= LOGIN =================
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cur.fetchone()

    cur.close()
    db.close()

    if user and check_password_hash(user['password'], password):
        session['user'] = user['name']
        flash(f"Welcome back, {user['name']} 👋", "success")
        return redirect('/dashboard')

    flash("❌ Invalid credentials", "error")
    return redirect('/')

# ================= DASHBOARD =================
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html', user=session['user'])

# ================= LOGOUT =================
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully", "info")
    return redirect('/')

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
