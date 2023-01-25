from flask import Flask
from flask import render_template,session,redirect,url_for
from flask import request
import mysql.connector
import os

from block import write_block, check_intergrity
from search import search

connection= mysql.connector.connect(host='localhost', port='3306', 
                                    database='records',
                                    user= 'root',
                                    password='')

cursor = connection.cursor()
app = Flask(__name__)
app.secret_key="super secret key"

picFolder = os.path.join('static', 'pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/home")
def home():
    return render_template('index.html', username=session['username'])


@app.route('/home', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        dob = request.form.get('dob')
        nic = request.form.get('nic')
        address = request.form.get('address')
        bio = request.form.get('bio')
        cad = request.form.get('cad')
        pd = request.form.get('pd')
        fd = request.form.get('fd')
        ed = request.form.get('ed')
        rd = request.form.get('rd')

        write_block(id=id, name=name, dob=dob, nic=nic, address=address, bio=bio, cad=cad, pd=pd, fd=fd, ed=ed, rd=rd)

    return render_template("index.html", username=session['username'])  


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the user's input
        username = request.form['username']
        password = request.form['password']

        # Connect to the database and check if the user exists
        # cur = mysql.connection.cursor()
        cursor.execute("SELECT * FROM admin1 WHERE aid = %s AND pass = %s", (username, password))
        user = cursor.fetchone()
   

        # If the user exists, log them in
        if user:
            session['logged_in'] = True
            session['username'] = user[1]
            return redirect(url_for('home'))
        else:
            # If the user doesn't exist or the password is incorrect, show an error message
            error = "Invalid username or password"
            return render_template('login.html', error=error)
    return render_template('login.html')




@app.route('/release_prisoner')
def release_prisoner():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'icon2.png')
    return render_template('release_prisoner.html', user_image=pic1)

@app.route('/prisoners_data')
def prisoners_data():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'icon2.png')
    return render_template('prisoners_data.html', user_image=pic1)

@app.route('/dashboard_add_admin')
def dashboard_add_admin():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'icon2.png')
    return render_template('dashboard_add_admin.html', user_image=pic1)

@app.route('/dashboard')
def dashboard():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'icon2.png')
    return render_template('dashboard.html', user_image=pic1)  


@app.route('/checking')
def check():
    results = check_intergrity()
    return render_template('index.html', checking_results=results)

@app.route('/searching', methods=['POST', 'GET'])
def searching():
    results = search()
    return render_template('search.html', searching_results=results)

if __name__ == '__main__':
    app.run(debug=True)
