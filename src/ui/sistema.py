import presentacion.Empleador as Empleador
from services.firebase_client import initialize_firebase


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


    def menu(self):
        menu = -1
        while menu != 0:
            self.mostrar_menu()

            menu = int(input("¿Qué opción seleccionas? ----> "))
            
            if menu == 1:
                Empleador.Administrador.Registro()
            
            elif menu == 2:
                Empleador.Administrador.personas_registradas()

            elif menu == 3:
                Empleador.Administrador.editar_usuario()
            
            elif menu == 4:
                Empleador.Administrador.eliminar_usuario()

            elif menu == 0:
                print("Saliendo del sistema")

            else:
                print("Opción no válida, intenta de nuevo.")
