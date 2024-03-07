import os
import datetime
import smtplib
from flask import Flask, render_template, request, redirect, url_for, session
from firebase import addResult

from inference import get_prediction
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase


app = Flask(__name__)
app.secret_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkI'

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '609fb14259f1d1'
app.config['MAIL_PASSWORD'] = '70ea376cf013c3'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

config = {
    "apiKey": "AIzaSyDBpTlredH1Zq35LGZuiztCJ9z12JdQSAU",
    "authDomain": "bctc-rawlinz-jeffproject.firebaseapp.com",
    "projectId": "bctc-rawlinz-jeffproject",
    "storageBucket": "bctc-rawlinz-jeffproject.appspot.com",
    "messagingSenderId": "1053088381150",
    "appId": "1:1053088381150:web:1cbc40e99566fe93a7ea4f",
    "measurementId": "G-X6WLDDBQG5",
    "databaseURL": ""
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firestore.client()



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('upload_file'))
        except Exception as e:
            print("error: ", e)
            return "Invalid Email or Password"
    return render_template('index.html')


@app.route('/predictions', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        user = session.get('user')
        if not user:
           return  redirect(url_for('login')) 
        
        email = user['email']
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        email = user['email']

        doc_ref = db.collection('patients').document(email)
        doc = doc_ref.get()
        userData = doc.to_dict()


        if not file:
            return
        img_bytes = file.read()
        prediction = get_prediction(image_bytes=img_bytes)
        addResult(email, datetime.datetime.now(), prediction) 
        
        return redirect(url_for('result'))
        # return render_template('result.html',
        #                        class_name=prediction, name = userData['name'], email = email)
    if request.method == 'GET':
        user = session.get('user')
        email = user['email']
        if not user:
           return  redirect(url_for('login')) 
        doc_ref = db.collection('patients').document(email)
        doc = doc_ref.get()
        userData = doc.to_dict()
        print("userdata: ", userData)
        
        if user:
            return render_template('predictions.html',
                                   name = userData['name'],
                                    email = email
                                   )
        else:
            return redirect(url_for('login'))


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        user = session.get('user')
        if not user:
           return  redirect(url_for('login')) 
        
        email = user['email']

        doc_ref = db.collection('patients').document(email)
        doc = doc_ref.get()
        userData = doc.to_dict()
        print("userdatahere: ", userData)

        return render_template('result.html', class_name=userData['result'][0], name = userData['name'], email = email)
    if request.method == 'POST':
        pass

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

