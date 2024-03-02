import string
import random
import os

# Verificar la existencia del archivo antes de abrirlo
if not os.path.isfile("Contraseñas.txt"):
    with open("Contraseñas.txt", "w"):
        pass

while True:

    #Defino las variables para los carácteres de la contraseña

    letras_mayusculas=string.ascii_uppercase
    letras_minusculas=string.ascii_lowercase
    numeros=string.digits
    caracteres=string.punctuation

    #Comienzo el programa preguntando por una longitud de contraseña

    longitud=int(input("Escriba cuántos carácteres quiere en su contraseña: "))

    #Preguntamos si vamos a usar letras mayusculas/minusculas/caracteres/numeros y un nombre 

    Nombre_contraseña=input("Escriba un nombre para su contraseña: ").lower()
    usa_mayusculas=input("Seleccione si quiere letras mayúsculas en su contraseña (s/n): ").lower()=='s'
    usa_minusculas=input("Seleccione si quiere letras minusculas en su contraseña (s/n): ").lower()=='s'
    usa_numeros=input("Seleccione si quiere numeros en su contraseña (s/n): ").lower()=='s'
    usa_caracteres=input("Seleccione si quiere caracteres especiales en su contraseña (s/n): ").lower()=='s'

    #Creamos la cadena vacia de caracteres permitidos para guardar las preferencias del ususario

    caracteres_permitidos=""

    if usa_mayusculas==True:
        caracteres_permitidos +=letras_mayusculas

    if usa_minusculas==True:
        caracteres_permitidos +=letras_minusculas

    if usa_numeros==True:
        caracteres_permitidos +=numeros

    if usa_caracteres==True:
        caracteres_permitidos +=caracteres

    while True:
        #Hacemos el bucle que generará la contraseña

        contraseña=''.join(random.choice(caracteres_permitidos) for i in range(longitud))

        #Hacemos las comporbaciones de seguridad

        if (usa_mayusculas and not any(c in letras_mayusculas for c in contraseña)) or (usa_minusculas and not any(c in letras_minusculas for c in contraseña)) or (usa_numeros and not any(c in numeros for c in contraseña)) or (usa_caracteres and not any(c in caracteres for c in contraseña)):
            ##print("La contraseña no cumple con los criterios de seguridad.") Cada vez que hay un error se genera una nueva contraseña, por lo tanto es innecesario
            continue

        #Vamos a imprimir nuestra contraseña y ##a preguntar si queremos generar otra##

        print("Contraseña generada: " + str(contraseña))

        #Guardo contraseña en el bloc de notas
        with open("Contraseñas.txt","a") as archivo:
            archivo.write("Contraseña "+ Nombre_contraseña +": " + contraseña +"\n")

        break

    Reinicio=input("¿Quiere generar otra contraseña? (s/n): ").lower()
    if Reinicio != "s":
        print("¡Gracias por usar el generador de contraseñas!")
        break



