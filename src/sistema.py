import models.Empleador as Empleador
from services.firebase_client import buscar_usuario, initialize_firebase, add_user, update_user, delete_user, get_all_users


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

    def Registro(self):
        print(f"\nRegistro")
        registrar = Empleador.Administrador()
        persona = registrar.realizar_registro_persona()
        add_user(persona)  


    def personas_registradas(self):
        print("\nPersonas registradas (desde Firebase):")
        usuarios = get_all_users()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
        else:
            for id, datos in usuarios.items():
                print(f"- Cedula: {id}")
                print(f"  Nombre: {datos.get('nombre')}")
                print(f"  Apellido: {datos.get('apellido')}")
                print(f"  Edad: {datos.get('edad')}")
                print(f"  Correo: {datos.get('correo')}")
                print(f"  Teléfono: {datos.get('telefono')}")
                print(f"  Cédula: {datos.get('cedula')}")
                print("---------------------------")


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

    def menu(self):
        menu = -1
        while menu != 0:
            self.mostrar_menu()

            menu = int(input("¿Qué opción seleccionas? ----> "))
            
            if menu == 1:
                self.Registro()
            
            elif menu == 2:
                self.personas_registradas()

            elif menu == 3:
                self.editar_usuario()
            
            elif menu == 4:
                self.eliminar_usuario()

            elif menu == 0:
                print("Saliendo del sistema")

            else:
                print("Opción no válida, intenta de nuevo.")
