from firebase_admin import credentials, initialize_app, db
from pathlib import Path
import os

def initialize_firebase():
    # primero buscar variable de entorno, si no existe usar ruta relativa dentro de src/config
    env = os.environ.get('FIREBASE_CREDENTIAL')
    if env:
        cred_file = Path(env)
    else:
        cred_file = Path(__file__).parent / 'config' / 'prueba-61c40-firebase-adminsdk-fbsvc-996e98f8c5.json'

    cred_file = cred_file.expanduser().resolve()
    if not cred_file.exists():
        raise FileNotFoundError(f"No se encontró el archivo de credenciales: {cred_file}")

    cred = credentials.Certificate(str(cred_file))
    try:
        initialize_app(cred, {
            'databaseURL': 'https://prueba-61c40-default-rtdb.firebaseio.com/'
        })
    except ValueError:
        # ya inicializada
        pass

def add_user_to_db(user_data):
    ref = db.reference('users')
    ref.push(user_data)

def update_user_in_db(user_id, user_data):
    ref = db.reference(f'users/{user_id}')
    ref.update(user_data)

def delete_user_from_db(user_id):
    ref = db.reference(f'users/{user_id}')
    ref.delete()

def get_all_users_from_db():
    ref = db.reference('users')
    return ref.get()
