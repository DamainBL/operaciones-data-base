from models.persona import Persona

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
        return persona

    def mostrar_info_persona(self):
        print("\nAquí están tu información:\n")
        for respuesta in self.respuestas:
            print(f"Respuesta: {respuesta}\n")