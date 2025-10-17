

from firebase_config import db


class Empleado:
    def __init__(self, nombre, apellido, edad, telefono, cedula, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.cedula = cedula
        self.cargo = cargo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Teléfono: {self.telefono}")
        print(f"Cédula: {self.cedula}")
        print(f"Cargo: {self.cargo}")
        print("-" * 40)


class Administrador:
    def __init__(self):
        self.preguntas_empleado = [
            "¿Cuál es el nombre del empleado? ",
            "¿Cuál es el apellido del empleado? ",
            "¿Cuántos años tiene? ",
            "¿Cuál es su número de teléfono? ",
            "¿Cuál es su número de cédula? ",
            "¿Cuál es su cargo? ",
        ]

    def registrar_empleado(self):
        print("=== Registro de Empleado ===")
        self.respuestas_empleado.clear()
        for pregunta in self.preguntas_empleado:
            respuesta = input(pregunta)
            self.respuestas_empleado.append(respuesta)

        empleado = Empleado(
            nombre=self.respuestas_empleado[0],
            apellido=self.respuestas_empleado[1],
            edad=self.respuestas_empleado[2],
            telefono=self.respuestas_empleado[3],
            cedula=self.respuestas_empleado[4],
            cargo=self.respuestas_empleado[5],
        )

        db.collection("empleados").document(empleado.cedula).set({
            "nombre": empleado.nombre,
            "apellido": empleado.apellido,
            "edad": empleado.edad,
            "telefono": empleado.telefono,
            "cedula": empleado.cedula,
            "cargo": empleado.cargo
        })

        print("Empleado registrado y guardado en Firebase correctamente.\n")
        return empleado

    def listar_empleados_firebase():
        empleados_ref = db.collection("empleados").get()
        for doc in empleados_ref:
            data = doc.to_dict()
            print(f"{data['nombre']} {data['apellido']} - {data['cargo']} (Cédula: {data['cedula']})")