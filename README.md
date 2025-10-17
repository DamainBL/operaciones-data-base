📚 Proyecto Sistema de Empleados con Firebase

Un sistema de gestión de empleados desarrollado en Python, que utiliza Firebase Firestore para almacenar la información en la nube.
Basado en Programación Orientada a Objetos (POO), permite registrar, listar, editar y eliminar empleados desde consola.

✨ Características principales

Conexión directa con Firebase Firestore

Estructura modular con clases separadas (Empleado, Administrador, Sistema)

Funciones CRUD básicas (crear, leer, actualizar, eliminar)

Interfaz de texto interactiva por consola

Código limpio y escalable, ideal para proyectos académicos o de aprendizaje

📁 Estructura del proyecto

proyecto_empleados/
│
├── sistema.py             # Control del menú principal
├── Empleador.py           # Clases Empleado y Administrador
├── firebase_config.py     # Conexión con Firebase
├── firebase/
│   └── firebase-key.json  # Clave privada 
└── README.md              # Este archivo 😊


🏷️ Clases principales

👨‍💼 Empleado
Representa a cada empleado con sus datos personales:

nombre, apellido, edad, teléfono, cédula y cargo
Funciones principales:

mostrar_info() → Muestra los datos del empleado

🧾 Administrador
Gestiona el registro de empleados y la conexión con Firebase.
Funciones principales:

registrar_empleado() → Crea un nuevo empleado y lo guarda en Firestore

listar_empleados() → Muestra todos los registros

⚙️ Sistema
Controla el flujo del programa y las opciones del menú.
Opciones principales:

Registrar empleado

Mostrar empleados

Editar empleado

Eliminar empleado

🔥 Configuración de Firebase

Crea un proyecto en Firebase Console

Genera una clave privada en Configuración del proyecto → Cuentas de servicio

Guarda el archivo .json dentro de la carpeta /firebase/

En firebase_config.py, configura la conexión:

cred = credentials.Certificate("firebase/firebase-key.json")
firebase_admin.initialize_app(cred)


⚙️ Ejecución del proyecto

Instala las dependencias:

pip install firebase-admin


Ejecuta el sistema:

python sistema.py


Interactúa con el menú desde consola.

💡 Ejemplo de uso

--- Bienvenido al Sistema de Empleados ---
1. Registrar un usuario
2. Mostrar personas registradas
3. Editar un usuario
4. Eliminar un usuario
0. Salir

¿Qué opción seleccionas? ----> 1
=== Registro de Empleado ===
¿Cuál es el nombre del empleado? Juan
¿Cuál es el apellido del empleado? Pérez
...
✅ Empleado registrado y guardado en Firebase correctamente.
