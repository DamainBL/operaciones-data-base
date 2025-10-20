# Proyecto en Python con Firebase

Este proyecto es una aplicación desarrollada en Python que utiliza Firebase como base de datos en tiempo real. Permite registrar, mostrar, editar y eliminar usuarios.


## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:


├── README.md # Este archivo

├── requirements.txt # Lista de dependencias del proyecto

├── src/ # Directorio principal del código fuente

│ ├── main.py # Punto de entrada de la aplicación

│ ├── sistema.py # Lógica principal del sistema 

│ ├── models/ # Definiciones de los modelos de datos

│ │ ├── Empleador.py # Clase Administrador para la gestión de usuarios

│ │ └── persona.py # Clase Persona

│ └── services/ # Servicios de conexión a Firebase

│ └── firebase_client.py # Cliente de Firebase


## Dependencias

El proyecto utiliza las siguientes dependencias, que se pueden instalar usando `pip`: pip install -r requirements.txt

Las dependencias son:

-   `firebase-admin`: Para la administración de Firebase.
-   `firebase`: Para interactuar con Firebase.


## Uso

1.  **Inicializar Firebase:**

    *   La función [`initialize_firebase`](src/services/firebase_client.py) en [`firebase_client.py`](src/services/firebase_client.py) inicializa la conexión a Firebase utilizando las credenciales proporcionadas.


2.  **Ejecutar la aplicación:**

    ```bash
    python src/main.py
    ```

    Esto iniciará la aplicación, mostrando un menú con opciones para registrar, mostrar, editar y eliminar usuarios.


## Clases y Funciones Principales

*   [`Sistema`](src/sistema.py): Clase principal que gestiona el sistema 
    *   `__init__`: Inicializa el sistema y la conexión a Firebase.
    *   `mostrar_menu`: Muestra el menú principal.
    *   `Registro`: Permite registrar un nuevo usuario.
    *   `personas_registradas`: Muestra la lista de usuarios registrados.
    *   `editar_usuario`: Permite editar la información de un usuario existente.
    *   `eliminar_usuario`: Permite eliminar un usuario.
    *   `menu`:  Muestra el menú y permite la interacción del usuario.
      
*   [`Administrador`](src/models/Empleador.py): Clase para la gestión de usuarios.
    *   `realizar_registro_persona()`:  Realiza el proceso de registro de una persona, solicitando la información y creando un objeto `Persona`.
      
*   [`Persona`](src/models/persona.py): Clase que representa a una persona.
    *   `__init__`: Inicializa una instancia de la clase `Persona` con nombre, apellido, edad, correo, teléfono y cédula.
      
*   [`firebase_client.py`](src/services/firebase_client.py): Módulo que contiene funciones para interactuar con Firebase.
    *   `initialize_firebase()`: Inicializa la aplicación Firebase.
    *   `add_user(user_data)`: Agrega un usuario a la base de datos.
    *   `update_user(user_id, user_data)`: Actualiza la información de un usuario existente.
    *   `delete_user(user_id)`: Elimina un usuario de la base de datos.
    *   `get_all_users()`: Obtiene todos los usuarios de la base de datos.
    *   `buscar_usuario(user_id)`: Busca un usuario por su ID en la base de datos.

## Modelo

*   [`Persona`](src/models/persona.py): Representa a una persona con atributos como nombre, apellido, edad, correo, teléfono y cédula.

## Consideraciones

*   Asegúrate de tener las credenciales de Firebase configuradas correctamente para que la aplicación pueda acceder a la base de datos.

