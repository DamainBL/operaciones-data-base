from firebase_admin import credentials, initialize_app, db
from pathlib import Path

class RealtimeDB:
    def __init__(self, config_path=None):
        # recibir ruta opcional; si no se pasa, buscar en src/config
        self.config_path = config_path
        self.initialize_firebase()

    def initialize_firebase(self):
        filename = 'prueba-61c40-firebase-adminsdk-fbsvc-996e98f8c5.json'
        if self.config_path:
            cred_file = Path(self.config_path)
        else:
            # __file__ está en .../src/services, parents[1] -> src
            cred_file = Path(__file__).parents[1] / 'config' / filename

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

    def add_user(self, user_data):
        ref = db.reference('users')
        ref.push(user_data)

    def update_user(self, user_id):
        ref = db.reference('users')
        ref.child(str(user_id)).delete()

    def delete_user(self, user_id):
        ref = db.reference(f'users/{user_id}')
        ref.delete()

    def get_user(self, user_id):
        ref = db.reference(f'users/{user_id}')
        return ref.get()

    def get_all_users(self):
        ref = db.reference('users')
        return ref.get()

# ...existing code...
# Wrappers de módulo (creación perezosa de la instancia) para mantener la API simple
_db_instance = None

def _get_db_instance(config_path=None):
    global _db_instance
    if _db_instance is None:
        _db_instance = RealtimeDB(config_path=config_path)
    return _db_instance

def add_user(user_data):
    return _get_db_instance().add_user(user_data)

def update_user(user_id, user_data):
    return _get_db_instance().update_user(user_id, user_data)

def delete_user(user_id):
    return _get_db_instance().delete_user(user_id)

def get_user(user_id):
    return _get_db_instance().get_user(user_id)

def get_all_users():
    return _get_db_instance().get_all_users()
def _to_dict(obj):
    if obj is None:
        return None
    # si tiene método mostrar_info (tu clase Persona), úsalo
    if hasattr(obj, "mostrar_info") and callable(getattr(obj, "mostrar_info")):
        return obj.mostrar_info()
    # si ya es dict, devolver tal cual
    if isinstance(obj, dict):
        return obj
    # fallback: intentar usar __dict__
    if hasattr(obj, "__dict__"):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}
    # si no se puede convertir, devolver el objeto tal cual (probablemente falle)
    return obj
# ...existing code...
def add_user(user_data):
        # aceptar dict o instancia; obtener cedula si existe
        cedula = None
        if isinstance(user_data, dict):
            cedula = user_data.get("cedula") or user_data.get("Cedula")
            data = user_data
        else:
            cedula = getattr(user_data, "cedula", None)
            # convertir objeto a dict (evitar atributos privados)
            data = {k: v for k, v in user_data.__dict__.items() if not k.startswith("_")}

        ref = db.reference('users')

        if cedula:
            # update() crea el nodo si no existe y actualiza solo los campos dados si ya existe
            ref.child(str(cedula)).update(data)
        else:
            # sin cédula, usar push() como antes
            ref.push(data)

def update_user(user_id, user_data):
    ref = db.reference('users')
        # actualizar campos (usa update para mezclar; set para sobrescribir)
    ref.child(str(user_id)).update(user_data)
