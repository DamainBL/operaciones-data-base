# Mi proyecto Firebase (Python)

Proyecto simple para registrar, ver, editar y eliminar usuarios usando Firebase Realtime Database desde Python.

## Requisitos
- Python 3.8+ (probado con 3.13)
- Paquetes:
  - firebase-admin

Instalar dependencias:
```powershell
python -m pip install firebase-admin
```

## Estructura principal
- src/main.py — entrada del programa (interfaz CLI).
- src/sistema.py — lógica del menú y orquestación.
- src/Empleador.py — recoge datos del usuario y crea instancias de Persona.
- src/models/persona.py — clase Persona.
- src/firebase_client.py — inicializa Firebase (usa la variable de entorno o `src/config/`).
- src/services/realtime_db.py — operaciones sobre Realtime Database (add, update, delete, get).

## Uso

Opciones del menú:
- 1: Registrar usuario (se enviará a Firebase).
- 2: Mostrar usuarios (lista desde Firebase).
- 3: Editar usuario (buscar por cédula y actualizar).
- 4: Eliminar usuario (buscar por cédula y borrar).
- 0: Salir.

## Comportamiento sobre la cédula (recomendado)
- Si los registros contienen campo `cedula`, el código puede usar la cédula como key en la BD (facilita editar/eliminar).
- `add_user` usa `update()` cuando existe cédula (mezcla campos) y `push()` si no existe cédula.
- `update_user(user_id, data)` actualiza los campos del nodo `users/{user_id}`.
- `delete_user(user_id)` borra el nodo `users/{user_id}`.

## Notas
- Los objetos Persona se convierten a diccionario antes de enviarlos a Firebase (método `mostrar_info()`).
- Cambiar la cédula implica mover o crear un nuevo nodo y borrar el antiguo (el flujo de edición ya contempla esto).

