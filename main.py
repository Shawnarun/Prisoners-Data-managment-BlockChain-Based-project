from flask import Flask
from flask import render_template
from flask import request
import os

from block import write_block, check_intergrity
from search import search


app = Flask(__name__)

picFolder = os.path.join('static', 'pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder




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

    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'icon2.png')
    pic11 = os.path.join(app.config['UPLOAD_FOLDER'], 'icon21.png')

    return render_template("index.html", user_image=pic1)  


@app.route('/login')
def login():
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
