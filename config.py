import pyrebase



db_link = "https://doutor-vazamentos-default-rtdb.firebaseio.com"

firebase_config = {
    "apiKey": "AIzaSyBYN5FqwF3g3GHUGamNYJOmMmYXu5BEpNk",
    "authDomain": "doutor-vazamentos.firebaseapp.com",
    "databaseURL": "https://doutor-vazamentos-default-rtdb.firebaseio.com",
    "projectId": "doutor-vazamentos",
    "storageBucket": "doutor-vazamentos.firebasestorage.app",
    "messagingSenderId": "100259767518",
    "appId": "1:100259767518:web:3fe2770abe96324d0f8e4f",
    "measurementId": "G-1R65BYTFLV"
}

firebase = pyrebase.initialize_app(firebase_config)
storage = firebase.storage()
auth = firebase.auth()
db = firebase.database()