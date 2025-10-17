class Persona:
    def __init__(self, nombre, apellido, edad, correo, telefono, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
        self.cedula = cedula

    def mostrar_info(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "correo": self.correo,
            "telefono": self.telefono,
            "cedula": self.cedula
        }
