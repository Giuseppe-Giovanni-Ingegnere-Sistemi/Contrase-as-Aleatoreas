# Generador de Contraseñas Aleatorias

-Este script en Python genera una contraseña aleatoria de una longitud especificada por el usuario. Utiliza una combinación de letras, dígitos y caracteres especiales para crear contraseñas seguras.

# Características

- Genera contraseñas aleatorias utilizando letras mayúsculas, letras minúsculas, dígitos y caracteres especiales.
- Permite al usuario especificar la longitud deseada de la contraseña.
- Fácil de usar e implementar en cualquier proyecto que requiera generación de contraseñas seguras.

# Requisitos
Python 3.12.5

# Instrucciones de Uso

Clona el repositorio o copia el script en tu máquina local.
Ejecuta el script en tu terminal o entorno de desarrollo.
Introduce la longitud deseada para la contraseña cuando se te solicite.
Obtén la contraseña generada, que se imprimirá en la consola.

# Ejemplo

```bash
$ python generar_contraseña.py
Ingrese el tamaño de la contraseña: 12
La contraseña generada es: A1b@C2d#E3f$
```

En este ejemplo, se generó una contraseña de 12 caracteres utilizando una combinación de letras mayúsculas, letras minúsculas, números y caracteres especiales.

# Personalización

Puedes personalizar el conjunto de caracteres que se utilizan para generar la contraseña modificando la variable caracteres en el script. Por ejemplo, si solo deseas utilizar letras y números, puedes modificarla así:

```bash
caracteres = string.ascii_letters + string.digits
```

Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias para mejorar el script, no dudes en hacer un fork del proyecto y enviar un pull request.

Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
