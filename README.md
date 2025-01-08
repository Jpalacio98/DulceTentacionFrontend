# DulceTentacionFrontend
# Pasos para configurar el entorno de desarrollo

A continuación, se detallan los pasos para configurar el entorno de desarrollo para este proyecto utilizando un entorno virtual de Python:

### 1. Crear el entorno virtual
Ejecuta el siguiente comando para crear un entorno virtual:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` en el directorio del proyecto que contendrá el entorno virtual.

---

### 2. Activar el entorno virtual

- **En Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

- **En macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

Cuando el entorno virtual esté activado, verás el nombre del entorno (por ejemplo, `venv`) al inicio de la línea de comandos.

---

### 3. Instalar las dependencias

Con el entorno virtual activado, instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Esto instalará todos los paquetes listados en el archivo `requirements.txt`.

---

### Notas adicionales
- Asegúrate de tener instalada una versión de Python compatible con el proyecto.
- Para salir del entorno virtual, simplemente usa el comando:
```
deactivate
```
