
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import os


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

cred = credentials.Certificate("btc.json")
firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def loginUser(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Login successful")
        return user
    except:
        print("Invalid email or password")
    return None



db = firestore.client()

def addResult(email, testDate, result):
    data = {
            "testDate": testDate,
            "result": result
        }
    doc_ref = db.collection('patients').document(email)
    doc_ref.update(data)

    print("success...")




