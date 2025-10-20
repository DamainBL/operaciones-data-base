from firebase_admin import credentials, db
import firebase_admin

def initialize_firebase():

    cred = credentials.Certificate(".................................")
    firebase_admin.initialize_app(cred, {'databaseURL': '................'})

def add_user(user_data):
    ref = db.reference('users')
    ref.child(user_data["cedula"]).set(user_data)

def update_user(user_id, user_data):
    ref = db.reference(f'users/{user_id}')
    ref.update(user_data)

def delete_user(user_id):
    ref = db.reference(f'users/{user_id}')
    ref.delete()

def get_all_users():
    ref = db.reference('users')
    return ref.get()

def buscar_usuario(user_id):
    ref = db.reference(f'users/{user_id}')
    return ref.get()
