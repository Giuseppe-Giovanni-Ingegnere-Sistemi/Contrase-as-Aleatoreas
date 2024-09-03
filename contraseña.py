import string
import random

longitud = int(input("Ingrese el tamaño de la contraseña: "))

# Corregir el error tipográfico
caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es: " + contraseña)
