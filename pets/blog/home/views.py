from flask import Flask,Blueprint,url_for,redirect,render_template,request,flash
from blog.home.models import db
from blog.home.models import User

pet = Blueprint('pet',__name__)


@pet.route("/")
def index():
    return "<h2>Welcome to the PETSWORLD</h2>"

@pet.route("/home",methods=['POST','GET'])
def home():
    if request.method=='POST':
        fname = request.form['first name']
        lname = request.form['last name']
        email = request.form['Email']
        rbutton = request.form['view']
        reason = request.form['like']
        new_record_values= User(FirstName=fname,LastName=lname,Email=email,Doyouownpets=rbutton,reason=reason)
        db.session.add(new_record_values)
        db.session.commit()
        flash("Sucessfully registerd")
        return redirect(url_for('pet.home'))

    else:
        return render_template('home/index.html')

@pet.route("/create")
def create():
    db.create_all()
    return "Database created sucessfully"
@pet.route("/delete")
def delete():
    db.drop_all()
    return "Database deleted properly"
