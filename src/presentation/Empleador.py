from models.persona import Persona
from services.firebase_client import buscar_usuario, add_user, update_user, delete_user, get_all_users

class Administrador:
    def __init__(self):
        self.preguntas = [
            "¿Cuál es o son tus nombres?",
            "¿Cuál es o son tus apellidos?",
            "¿Cuántos años tienes?",
            "¿Cuál es tu correo electrónico?",
            "¿Cuál es tu número de contacto?",
            "¿Cuál es tu número de cédula?"
        ]
        self.respuestas = []

    def realizar_registro_persona(self):
        print("Bienvenido al registro. Por favor, responde las siguientes preguntas:")
        for pregunta in self.preguntas:
            respuesta = input(f"{pregunta} ")
            self.respuestas.append(respuesta)
        persona = Persona(
            nombre=self.respuestas[0],
            apellido=self.respuestas[1],
            edad=self.respuestas[2],
            correo=self.respuestas[3],
            telefono=self.respuestas[4],
            cedula=self.respuestas[5]
        )
        persona_dict = persona.__dict__
        return persona_dict

    
    def Registro(self):
        print(f"\nRegistro")
        registrar = Administrador()
        persona = registrar.realizar_registro_persona()
        add_user(persona)  


    def _personas_registradas(self):
        print("\nPersonas registradas (desde Firebase):")
        usuarios = get_all_users()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
        else:
            for id,  datos in usuarios.items():
                print(f"  Nombre: {datos.get('nombre')}")
                print(f"  Apellido: {datos.get('apellido')}")
                print(f"  Edad: {datos.get('edad')}")
                print(f"  Correo: {datos.get('correo')}")
                print(f"  Teléfono: {datos.get('telefono')}")
                print(f"  Cédula: {datos.get('cedula')}")
                print("---------------------------")
    
    @property
    def personas_registradas(self):
        self._personas_registradas()


    def editar_usuario(self):
        cedula_buscar = input("Ingresa la cédula del usuario que deseas editar: ")
        usuarios = get_all_users()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
            return

        datos = buscar_usuario(cedula_buscar)
        if not datos:
            print(f"No se encontró un usuario con cédula {cedula_buscar}.")
            return

        nombre_actual = datos.get("nombre","")
        apellido_actual = datos.get("apellido","") 
        edad_actual = datos.get("edad","") 
        correo_actual = datos.get("correo","") 
        telefono_actual = datos.get("telefono","") 

        print(f"Editando usuario: {nombre_actual} {apellido_actual} (Cédula: {cedula_buscar})")

        nuevo_nombre = input(f"Nuevo nombre ({nombre_actual}): ")
        nuevo_apellido = input(f"Nuevo apellido ({apellido_actual}): ")
        nueva_edad = input(f"Nueva edad ({edad_actual}): ")
        nuevo_correo = input(f"Nuevo correo ({correo_actual}): ")
        nuevo_telefono = input(f"Nuevo teléfono ({telefono_actual}): ")

        actualizado = dict(datos) 
        if nuevo_nombre:
            actualizado["nombre"] = nuevo_nombre
        if nuevo_apellido:
            actualizado["apellido"] = nuevo_apellido
        if nueva_edad:
            actualizado["edad"] = nueva_edad
        if nuevo_correo:
            actualizado["correo"] = nuevo_correo
        if nuevo_telefono:
            actualizado["telefono"] = nuevo_telefono


        update_user(cedula_buscar, actualizado)

        print("Usuario actualizado exitosamente.")
        
    def eliminar_usuario(self):

        cedula_buscar = input("Ingresa la cédula del usuario que deseas eliminar: ")
        usuarios = get_all_users()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
            return

        delete_user(cedula_buscar)

        print(f"Usuario con cédula {cedula_buscar} eliminado exitosamente.")
