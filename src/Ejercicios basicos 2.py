# Ejercicios sencillos de aprendizaje de Python (2)
import random

# Modificar una lista de numeros reales que representan las calificaciones de los
# alumnos de una clase, para sustituir los valores numericos por sus
# calificaciones alfanumericas (Suspenso, Aprobado, etc.)
def calificar(lista):
    """
    Califica todas las notas de la lista, devolviendo la misma lista pero con sus calificaciones
    :param lista: list[float]
    :return: list[string]
    """
    calificacion = ""
    for i in range(0, len(lista)):
        nota = lista[i]
        if nota < 0 or nota > 10:
            calificacion = "Error"
        else:
            if nota < 5:
                calificacion = "Suspenso"
            elif nota < 7:
                calificacion = "Aprobado"
            elif nota < 9:
                calificacion = "Notable"
            elif nota <= 10:
                calificacion = "Sobresaliente"
        lista[i] = calificacion
    return lista


# Implementar una funcion que pone en mayusculas todas las primeras letras de las palabras de una frase
def poner_mayuscular(frase):
    """
    Pone en mayusculas las primeras letras de las palabras de una frase
    :param frase: string
    :return: string
    """
    palabras = frase.split(" ")
    frase_nueva = ""
    for palabra in palabras:
        frase_nueva += palabra[0].upper() + palabra[1:] + " "

    return frase_nueva[0:len(frase_nueva)-1]


# Implemente una funcion que indique si una palabra contiene las cinco vocales: por ejemplo, "murcielago".
# Modifique posteriormente la funcion para que detecte solo aquellas palabras que contienen una unica vez
# cada vocal
def tiene_cinco_vocales(palabra):
    """
    Indica si la palabra contiene a las cinco vocales pero una unica vez cada vocal
    :param palabra: string
    :return: bool
    """
    return palabra.upper().find("A") > -1 and palabra.upper().find("E") > -1 and palabra.upper().find("I") > -1 and \
           palabra.upper().find("O") > -1 and palabra.upper().find("U") > -1


def tiene_cinco_vocales_una_unica_vez(palabra):
    """
    Indica si la palabra contiene a las cinco vocales
    :param palabra: string
    :return: bool
    """
    return palabra.upper().find("A") > -1 and palabra.upper().count("A") == 1 and\
           palabra.upper().find("E") > -1 and palabra.upper().count("E") == 1 and\
           palabra.upper().find("I") > -1 and palabra.upper().count("I") == 1 and\
           palabra.upper().find("O") > -1 and palabra.upper().count("O") == 1 and\
           palabra.upper().find("U") > -1 and palabra.upper().count("U") == 1


# Escribir una funcion que sume dos listas de igual longitud y retorne otra lista
# que contenga la suma de las originales elemento a elemento.
def suma_listas(lista1, lista2):
    """
    Devuelve una lista cuyos elementos son la suma de lista1 y lista 2 elemento a elemento
    :param lista1: list[float], len = n
    :param lista2: list[float], len = n
    :return: list[float], len = n
    """
    lista_salida = []
    for i in range(0, len(lista1)):
        lista_salida.append(lista1[i]+lista2[i])
    return lista_salida


# Modifique el ejercicio anterior permitiendo que las listas sean desiguales. En este caso, los
# elementos sobrantes de la lista mas larga se anadiran al final de la lista resultante.
def suma_listas_desiguales(lista1, lista2):
    """
    Devuelve una lista cuyos elementos son la suma de lista1 y lista 2 elemento a elemento
    :param lista1: list[float], len = n
    :param lista2: list[float], len = n
    :return: list[float], len = n
    """
    lista_salida = []
    if len(lista1) <= len(lista2):
        lista_pequena = lista1
        lista_grande = lista2
    else:
        lista_pequena = lista2
        lista_grande = lista1

    for i in range(0, len(lista_pequena)):
        lista_salida.append(lista_pequena[i]+lista_grande[i])

    lista_salida += lista_grande[len(lista_pequena):]

    return lista_salida


# Crear una lista de enteros, inicializarlos segun valores aleatorios en el rango
# 1..20 y computar la media de los valores, el valor mas alto y el mas bajo
# (utilizando listas). Utilizar las funciones para generacion de numeros
# aleatorios de Python
def calculos_lista_aleatoria():
    """
    Crea una lista de enteros aleatorios entre 1 y 20 y devuelve la media,
    el maximo y el minimo
    :return: void
    """
    lista = []
    tamano_lista = input("Escriba el tamano de la lista: ")
    for i in range(0, tamano_lista):
        lista.append(random.randint(1, 20))
    media = sum(lista)/float(len(lista))
    print("La lista es: " + str(lista))
    print("La media de los valores de la lista es: "+str(media))
    print("El maximo de los valores de la lista es: " + str(max(lista)))
    print("El minimo de los valores de la lista es: " + str(min(lista)))


# Implementar una funcion que compruebe si una palabra es un palindromo.
# Palindromo -> se lee igual en los dos sentidos. Ej: Kayak
def es_palindroma(palabra):
    """
    Devuelve si la palabra es palindroma, es decir, que se lee igual en los dos sentidos
    :param palabra: string
    :return: bool
    """
    palabra_al_reves = ""
    for i in range(0, len(palabra)):
        palabra_al_reves += palabra[len(palabra)-1-i]
    return palabra == palabra_al_reves


# Crear una funcion que compruebe si dos cadenas de caracteres son iguales recorriendo con
# un indice ambas cadenas (sin utilizar cad1 == cad2)
def es_cadenas_iguales(cad1, cad2):
    """
    Devuelve si las dos cadenas son iguales
    :param cad1: string
    :param cad2: string
    :return: bool
    """
    respuesta = False
    for i in range(0, len(cad1)):
        if cad1[i] == cad2[i]:
            respuesta = True
    return respuesta


# Distribuir 20 datos enteros leidos por teclado en dos listas de tal manera que se vayan generando
# dos secuencias ordenadas, una creciente y otra decreciente
def insertar_descendente(num, lista):
    """
    Inserta un numero en una lista, de manera descendente
    :param num: int
    :param lista: list[int]
    :return: list[int]
    """
    lista_salida = []
    # Si la lista a esta vacia o el menor de la lista es mayor o igual que el numero a insertar
    if len(lista) == 0:
        lista_salida.append(num)
    elif min(lista) >= num:
        lista_salida = lista + [num]
    # Si tiene mas elementos
    else:
        lista_salida = []
        numero_insertado = False
        for i in range(0, len(lista)):
            # Si el numero es mas grande que el elemento y no ha sido colocado, colocarlo delante
            if num >= lista[i] and numero_insertado is False:
                lista_salida.append(num)
                lista_salida.append(lista[i])
                numero_insertado = True
            # Si no, pasa al siguiente elemento
            else:
                lista_salida.append(lista[i])
    return lista_salida


def insertar_ascendente(num, lista):
    """
    Inserta un numero en una lista, de manera ascendente
    :param num: int
    :param lista: list[int]
    :return: list[int]
    """
    lista_salida = []
    # Si la lista a esta vacia o el menor de la lista es mayor o igual que el numero a insertar
    if len(lista) == 0:
        lista_salida.append(num)
    elif max(lista) <= num:
        lista_salida = lista + [num]
    # Si tiene mas elementos
    else:
        lista_salida = []
        numero_insertado = False
        for i in range(0, len(lista)):
            # Si el numero es mas pequeno que el elemento y no ha sido colocado, colocarlo delante
            if num <= lista[i] and numero_insertado is False:
                lista_salida.append(num)
                lista_salida.append(lista[i])
                numero_insertado = True
            # Si no, pasa al siguiente elemento
            else:
                lista_salida.append(lista[i])
    return lista_salida


def generar_secuencias_ordenadas():
    """
    Devuelve dos listas, la primera ordenada ascendente y la segunda descendente, en funcion de los
    datos que inserte el usuario, y las pinta
    :return: void
    """
    lista_asc = []
    lista_desc = []
    for i in range(0, 20):
        num = input("Inserte un entero: ")
        lista_asc = insertar_ascendente(num, lista_asc)
        lista_desc = insertar_descendente(num, lista_desc)

    print("La lista ascendente es: " + str(lista_asc))
    print("La lista descendente es: " + str(lista_desc))


# Escriba un programa que "codifique" una frase modificando todas las vocales
# segun el siguiente codigo: a por 4, e por 3, i por 1, o por 0 y u por el
# simbolo #. Por ejemplo, la frase: "Un perro del hortelano", debera
# devolverse: "#n p3rr0 d3l h0rt3l4n0".
def codificar_frase(frase):
    """
    Codifica una frase transformando: a->4, e->3, i->1, o->0, u->#
    :param frase: string
    :return: string
    """
    codigo = {
        'A': "4",
        'E': "3",
        'I': "1",
        'O': "0",
        'U': "#"
    }
    frase_codificada = ""
    for i in range(0, len(frase)):
        frase_codificada += codigo.get(frase[i].upper(), frase[i])
    return frase_codificada


# Crear un diccionario en python con parejas numero de tfno, nombre que
# represente una agenda telefonica. Posteriormente simular un manos libres,
# pidiendo al usuario "A quien desea llamar" y mostrando en pantalla el
# mensaje "Llamada al numero XXX en curso" donde XXX seria el numero
# telefonico de la persona elegida
agenda = {
    "ANA": 901234323,
    "JOSE": 902167845,
    "MARIA": 928763857,
    "RAMON": 917654321
}


def simulador_manos_libres(agenda):
    """
    Simula un manos libres, de manera que se le pide al usuario un nombre y llama
    al telefono asociado segun la agenda
    :param agenda: dictionary[string, int]
    :return: void
    """
    nombre = raw_input("A quien desea llamar?: ")
    telefono = agenda.get(nombre.upper(), "")
    if telefono == "":
        print("No existe ese nombre en la agenda.")
    else:
        print("Llamando al numero " + str(telefono) + " en curso")


# Escribir una funcion que reciba un tweet y retorne los hashtags en una lista
def listar_hashtags(tweet):
    """
    Devuelve una lista con los hashtags del tweet
    :param tweet: string
    :return: list[string]
    """
    lista_salida = []
    palabras = tweet.split(" ")
    for palabra in palabras:
        if palabra[0] == "#":
            lista_salida.append(palabra)

    return lista_salida


# Escriba un programa que lea un archivo de texto y lo mete en una lista
# donde cada linea es una sublista
def lector_ficheros(nombre_fichero):
    """
    Lee el fichero de texto pasado por parametro y crea sublistas con cada una de las lineas
    :param nombre_fichero: string
    :return: list[string]
    """
    lista_lineas = []
    sublista_linea = []
    archivo = open(nombre_fichero, 'r')
    for linea in archivo:
        sublista_linea.append(linea)
        lista_lineas.append(sublista_linea)
        sublista_linea = []
    return lista_lineas


# Realizar un programa que lea palabras hasta que se introduzca "fin",
# mostrando una estadistica de las longitudes de las palabras, es decir, el
# numero total de palabras de longitud 1 que se hayan introducido, el total de
# longitud 2, etc. La maxima longitud de las palabras debera ser de 25
# caracteres. Una posible salida de este programa seria:
#   Palabras longitud 1: 0
#   Palabras longitud 2: 10
#   ...
#   Palabras longitud 25: 1
def estadisticas_input():
    """
    Realiza estadisticas de la longitud de las palabras que inserte el usuario.
    :return: void
    """
    palabra_usuario = ""
    lista_palabras = []
    while palabra_usuario != "fin":
        palabra_usuario = raw_input("Inserte una palabra (long maxima de 25 caracteres): ")
        if len(palabra_usuario) <= 25:
            lista_palabras.append(palabra_usuario)

    contador = 0
    for longitud in range(0, 26):
        for palabra in lista_palabras:
            if len(palabra) == longitud:
                contador += 1
        print ("Palabras longitud " + str(longitud) + ": " + str(contador))
        contador = 0






