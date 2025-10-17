
import Empleador


class Sistema:
    def __init__(self):
        self.empleados_registradas = []
        self.admin = Empleador.Administrador()

        demo = Empleador.Empleado("Carlos", "Ramirez", "28", "3001234567", "123456789", "Desarrollador")
        self.empleados_registradas.append(demo)

    def mostrar_menu(self):
        print("\n--- Bienvenido a la Biblioteca ---")
        print("1. Registrar un usuario")
        print("2. Mostrar personas registradas")
        print("3. Editar un usuario")
        print("4. Eliminar un usuario")
        print("0. Salir")

    def buscar_persona_por_cedula(self, cedula):
        for persona in self.empleados_registradas:
            if persona.cedula == cedula:
                return persona
        return None

    def editar_usuario(self):
        cedula_buscar = input("Ingresa la cédula del usuario que deseas editar: ")
        persona = self.buscar_persona_por_cedula(cedula_buscar)
        if persona is None:
            print("No se encontró ese usuario.")
            return

        print(f"Editando usuario: {persona.nombre} {persona.apellido} (Cédula: {persona.cedula})")
        nuevo_nombre = input(f"Nuevo nombre ({persona.nombre}): ") or persona.nombre
        nuevo_apellido = input(f"Nuevo apellido ({persona.apellido}): ") or persona.apellido
        nueva_edad = input(f"Nueva edad ({persona.edad}): ") or persona.edad
        nuevo_telefono = input(f"Nuevo teléfono ({persona.telefono}): ") or persona.telefono
        nueva_cedula = input(f"Nueva cédula ({persona.cedula}): ") or persona.cedula

        persona.nombre = nuevo_nombre
        persona.apellido = nuevo_apellido
        persona.edad = nueva_edad
        persona.telefono = nuevo_telefono
        persona.cedula = nueva_cedula

        print("Usuario actualizado exitosamente.")

    def eliminar_usuario(self):
        if not self.empleados_registradas:
            print("No hay personas registradas para eliminar.")
            return
        cedula_buscar = input("Ingresa la cédula del usuario que deseas eliminar: ").strip()
        persona = self.buscar_persona_por_cedula(cedula_buscar)
        if persona is None:
            print(f"No se encontró un usuario con cédula {cedula_buscar}.")
            return
        self.empleados_registradas.remove(persona)
        print(f"Usuario {persona.nombre} {persona.apellido} eliminado exitosamente.")

    def menu(self):
        menu = -1
        while menu != 0:
            self.mostrar_menu()
            try:
                menu = int(input("¿Qué opción seleccionas? ----> "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if menu == 1:
                registrar = Empleador.Administrador()
                persona = registrar.registrar_empleado()
                self.empleados_registradas.append(persona)
            elif menu == 2:
                if not self.empleados_registradas:
                    print("No hay personas registradas.")
                else:
                    print("\nPersonas registradas:")
                    for i in self.empleados_registradas:
                        i.mostrar_info()
            elif menu == 3:
                self.editar_usuario()
            elif menu == 4:
                self.eliminar_usuario()
            elif menu == 0:
                print("Saliendo del sistema...")
            else:
                print("Opción no válida, intenta de nuevo.")


