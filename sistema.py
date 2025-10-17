
import Empleador
from firebase_client import initialize_firebase
from services.realtime_db import add_user, update_user, delete_user, get_user, get_all_users

class Sistema:
    def __init__(self):
        self.admin = Empleador.Administrador()
        initialize_firebase()

    def mostrar_menu(self):
        print("\n--- Bienvenido a la Biblioteca ---")
        print("Presiona 1 para registrar un usuario")
        print("Presiona 2 para mostrar personas registradas")
        print("Presiona 3 para editar un usuario")
        print("Presiona 4 para eliminar un usuario")
        print("Presiona 0 para salir")

    def buscar_persona_por_cedula(self, cedula):
        for persona in self.personas_registradas:
            if persona.cedula == cedula:
                return persona
        return None

    def editar_usuario(self):
        cedula_buscar = input("Ingresa la cédula del usuario que deseas editar: ").strip()
        usuarios = get_all_users()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
            return

        # buscar la entrada en Firebase (puede estar guardada bajo la cédula como key o dentro de los datos)
        firebase_key = None
        datos = None
        for key, val in usuarios.items():
            if isinstance(val, dict):
                if str(val.get("cedula") or val.get("Cedula") or key) == cedula_buscar:
                    firebase_key = key
                    datos = val
                    break
            else:
                # caso improbable: valor no dict, considerar key como cédula
                if str(key) == cedula_buscar:
                    firebase_key = key
                    datos = val
                    break

        if firebase_key is None:
            print(f"No se encontró un usuario con cédula {cedula_buscar} en Firebase.")
            return

        # mostrar datos actuales y solicitar cambios
        nombre_actual = datos.get("nombre") or datos.get("Nombre") or ""
        apellido_actual = datos.get("apellido") or datos.get("Apellido") or ""
        edad_actual = datos.get("edad") or datos.get("Edad") or ""
        correo_actual = datos.get("correo") or datos.get("Correo") or ""
        telefono_actual = datos.get("telefono") or datos.get("Telefono") or ""
        cedula_actual = datos.get("cedula") or datos.get("Cedula") or firebase_key

        print(f"Editando usuario: {nombre_actual} {apellido_actual} (Cédula: {cedula_actual})")

        nuevo_nombre = input(f"Nuevo nombre ({nombre_actual}): ").strip()
        nuevo_apellido = input(f"Nuevo apellido ({apellido_actual}): ").strip()
        nueva_edad = input(f"Nueva edad ({edad_actual}): ").strip()
        nuevo_correo = input(f"Nuevo correo ({correo_actual}): ").strip()
        nuevo_telefono = input(f"Nuevo teléfono ({telefono_actual}): ").strip()
        nueva_cedula = input(f"Nueva cédula ({cedula_actual}): ").strip()

        # construir dict actualizado
        actualizado = dict(datos) if isinstance(datos, dict) else {}
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

        # si cambias la cédula y la cédula se usa como key, hay que mover el registro:
        if nueva_cedula and nueva_cedula != str(cedula_actual):
            actualizado["cedula"] = nueva_cedula
            # crear nuevo nodo con la nueva cédula y borrar el antiguo
            update_user(nueva_cedula, actualizado)   # creará/actualizará bajo la nueva cédula
            delete_user(firebase_key)                # eliminar el viejo key
        else:
            # actualizar en la misma key (si guardaste por cédula, key == cedula)
            update_user(firebase_key, actualizado)

        print("Usuario actualizado exitosamente.")

    def eliminar_usuario(self):
        cedula_buscar = input("Ingresa la cédula del usuario que deseas eliminar: ").strip()
        usuarios = get_all_users()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
            return

        # buscar la key en Firebase igual que en editar
        firebase_key = None
        for key, val in usuarios.items():
            if isinstance(val, dict):
                if str(val.get("cedula") or val.get("Cedula") or key) == cedula_buscar:
                    firebase_key = key
                    break
            else:
                if str(key) == cedula_buscar:
                    firebase_key = key
                    break

        if firebase_key is None:
            print(f"No se encontró un usuario con cédula {cedula_buscar} en Firebase.")
            return

        # eliminar en Firebase
        delete_user(firebase_key)

        # si existe en la lista local, eliminarla también
        try:
            persona = self.buscar_persona_por_cedula(cedula_buscar)
            if persona:
                self.personas_registradas.remove(persona)
        except Exception:
            pass

        print(f"Usuario con cédula {cedula_buscar} eliminado exitosamente.")

    def menu(self):
        menu = -1
        while menu != 0:
            self.mostrar_menu()

            menu = int(input("¿Qué opción seleccionas? ----> "))

            if menu == 1:
                print(f"\nRegistro")
                registrar = Empleador.Administrador()
                persona = registrar.realizar_registro_persona()
                add_user(persona)  
            elif menu == 2:
                print("\nPersonas registradas (desde Firebase):")
                usuarios = get_all_users()
                if not usuarios:
                    print("No hay usuarios en la base de datos.")
                else:
                    # usuarios suele ser un dict {firebase_key: {campo:valor, ...}, ...}
                    for key, datos in usuarios.items():
                        if isinstance(datos, dict):
                            # mostrar campos principales
                            nombre = datos.get("nombre") or datos.get("Nombre") or ""
                            apellido = datos.get("apellido") or datos.get("Apellido") or ""
                            cedula = datos.get("cedula") or datos.get("Cedula") or key
                            print(f"- {nombre} {apellido} (cédula/ID: {cedula}) -> {datos}")
                        else:
                            print(f"- {key} -> {datos}")

            elif menu == 3:
                self.editar_usuario()
            
            elif menu == 4:
                self.eliminar_usuario()

            elif menu == 0:
                print("Saliendo del sistema")

            else:
                print("Opción no válida, intenta de nuevo.")