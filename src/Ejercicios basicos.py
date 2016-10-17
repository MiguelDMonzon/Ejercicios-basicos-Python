# Ejercicios sencillos de aprendizaje de python
from math import pi


# Funcion que retorne el mayor de dos numeros o 0 si son iguales
def max_numeros(num1, num2):
    """
    Devuelve el mayor de dos numeros x e y
    :param num1: float
    :param num2: float
    :return: float
    """

    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return 0


# Funcion que determine si una persona es mayor de edad o no
def es_mayor_edad(edad):
    """
    Determina si una persona es mayor de edad a partir de su edad
    :param edad: int
    :return: bool
    """
    return edad >= 18


# Programar una funcion que determine si una empresa es microempresa o no (retorno booleano True o False).
# Se dice que es microempresa si tiene menos de 50 empleados, factura menos de 30
# millones de euros y tiene un balance igual o inferior a los 5 millones de euros.
def es_microempresa(num_empleados, facturacion, balance):
    """
    Determina si una empresa es microempresa o no
    :param num_empleados: int
    :param facturacion: int
    :param balance: int
    :return: bool
    """
    return num_empleados < 50 and facturacion < 30 and balance <= 5


# Calcular el impuesto que debe pagar un contribuyente a partir de sus ingresos anuales
# y el numero de hijos. El impuesto a pagar es un tercio del ingreso imponible,
# siendo este ultimo igual a los ingresos totales menos una deduccion personal de 600 euros
# y otra deduccion de 60 euros por hijo.
def calcular_impuesto():
    """
    Calcula el impuesto que debe pagar un contribuyente en funcion se sus ingresos anuales y el
    numero de hijos.
    :return: float
    """
    ingresos_anuales = input("Inserte sus ingresos anuales (en euros): ")
    tiene_hijos = raw_input("Tiene Ud. hijo/as? (S/N): ")
    if tiene_hijos == "S":
        num_hijos = input("Escriba cuantos hijo/as tiene: ")
        ingreso_imponible = ingresos_anuales - 600 - (60 * num_hijos)
    else:
        ingreso_imponible = ingresos_anuales - 600
    return ingreso_imponible / 3.0

# Hacer los calculos que permiten saber si una empresa de 20 empleados, 18 millones de euros de
# facturacion y 5 millones de euros de balance es una micro empresa y almacenar el
# valor en una variable logica (booleana).
# Solucion: llamar a la funcion, y escribir 20, 18 y 5 => True
ejercicio_microempresa = es_microempresa(20, 18, 5)


# La temperatura expresada en grados centigrados TC, se puede convertir a grados
# Fahrenheit (TF) mediante la siguiente formula: TF = 9*TC/5 + 32. Programa una funcion
# para hacer esta transformacion que reciba como argumento la temperatura en grados
# centigrados y retorne su equivalente en Farenheit.
def centigrados_to_fahrenheit(grados_centigrados):
    """
    Transforma grados centigrados a fahrenheit
    :param grados_centigrados: float
    :return: float
    """
    return 9*grados_centigrados/5.0 + 32


# Escribir una funcion Python que a partir de una cierta cantidad en euros y
# del tipo de cambio del dia, retorne el equivalente en libras teniendo en cuenta que
# la casa de cambio retiene una comision del 2% sobre el total de la operacion.
def euros_to_libras(euros, tipo):
    """
    Transforma euros a libras, con una comision del 2%
    :param euros: float
    :param tipo: float
    :return: float
    """
    return (euros*tipo)*0.98


# Procedimiento que pinte una linea de asteriscos en pantalla
def pintar_asteriscos():
    """
    Pinta una linea de asteriscos
    :return: void
    """
    print("********************************")


# Programe un modulo en Python que reutilizando la funcion anterior muestre nuestros datos
# en pantalla con formato banner tal y como se representa abajo:
# **************************************
# Autor: Miguel David Monzon
# Email: miguel.monzon@uah.es
# **************************************
def pintar_banner(autor, email):
    """
    Pinta un banner con autor junto a su e-mail
    :param autor: string
    :param email: string
    :return: void
    """
    pintar_asteriscos()
    print("Autor: "+autor)
    print("Email: "+email)
    pintar_asteriscos()


# Programa modularizado que, utilizando funciones, calcule el perimetro y el area de
# un circulo cuyo radio es proporcionado por el usuario
def calcular_perimetro(radio):
    """
    Calcula el perimetro de una circunferencia dado su radio
    :param radio: float
    :return: float
    """
    return 2.0 * pi * radio


def calcular_area(radio):
    """
    Calcula el area de una circunferencia dado su radio
    :param radio: float
    :return: float
    """
    return pi * (radio ** 2.0)


def programa_calculo():
    """
    Calcula el perimetro y el area de una circunferencia dado su radio
    :return: void
    """
    radio = input("Inserte el radio del circulo: ")
    print("Su perimetro es: " + str(calcular_perimetro(radio)))
    print("Su area es: " + str(calcular_area(radio)))


# Escribir un programa para solicitar al usuario el numero de horas y el precio por hora
# con vistas a calcular su salario bruto. Las horas que sobrepasen 40 se consideraran
# extra y pagadas a 1,5 veces el precio de la hora regular.
def calcular_salario_bruto():
    """
    Calcula salario bruto en funcion del numero de horas y el precio de la hora regular y extra
    :return: float
    """
    num_horas = input("Inserte el numero de horas: ")
    precio_hora = input("Inserte el precio de la hora (regular): ")
    if num_horas > 40:
        horas_extra = num_horas - 40
        precio_extra = horas_extra * 1.5
        return 40 * precio_hora + precio_extra
    else:
        return num_horas * precio_hora


# Programar una funcion que determine si un numero es par o impar. La funcion debe retornar
# verdadero o falso haciendo uso de valores booleanos.
def es_par(num):
    """
    Devuelve si un numero es par o no
    :param num: int
    :return: bool
    """
    return num % 2 == 0


# Programar una funcion que determine si una letra es vocal o no.
def es_vocal(letra):
    """
    Devuelve si una letra es vocal o no
    :param letra: char
    :return: bool
    """
    return letra.upper() in ['A', 'E', 'I', 'O', 'U']


# Programar una funcion en Python que a partir de un numero entero entre 1 y 7 que recibe como
# argumento retorne el dia de la semana que corresponda, y un mensaje de error si
# el numero no esta entre 1 y 7.
def dia_semana(num):
    """
    Devuelve el dia de la semana correspondiente al numero pasado por parametro
    :param num: int
    :return: string
    """
    if num == 1:
        return "Lunes"
    elif num == 2:
        return "Martes"
    elif num == 3:
        return "Miercoles"
    elif num == 4:
        return "Jueves"
    elif num == 5:
        return "Viernes"
    elif num == 6:
        return "Sabado"
    elif num == 7:
        return "Domingo"
    else:
        return "Error, el numero tiene que estar entre 1 y 7."


def dia_semana_switch(num):
    """
    Devuelve el dia de la semana correspondiente al numero pasado por parametro, usando switch
    :param num: int
    :return: string
    """
    switcher = {
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado",
        7: "Domingo",
    }
    return switcher.get(num, "Error, el numero tiene que estar entre 1 y 7.")


# Funcion que recibe un numero y que muestre la tabla de multiplicar de ese numero (hasta 10)
def tabla_multiplicar(num):
    """
    Pinta la tabla de multiplicar de un numero
    :param num: float
    :return: void
    """
    for i in range(0, 11):
        print (str(num) + " * " + str(i) + " = " + str(num*i))


# Funcion que suma todos los elementos del 1 al 200 que sean multiplos de 3 o de 5
def suma_multiplos():
    """
    Calcula la suma de los multiplos de 3 o 5 entre el 1 y el 200 y lo pinta en pantalla
    :return: void
    """
    suma = 0
    for i in range(1, 201):
        if i % 3 == 0 or i % 5 == 0:
            suma += i

    print ("La suma de los multiplos de 3 o de 5 es: " + str(suma))


# Funcion que devuelve la suma de los primeros 50 numeros que cumplen la condicion de ser
# multiplo de 3 o de 5
def suma_multiplos2():
    """
    Calcula la suma de los 50 primeros multiplos de 3 o de 5 y lo pinta en pantalla
    :return: void
    """
    num = 1
    suma = 0
    contador = 0
    while contador < 50:
        if num % 3 == 0 or num % 5 == 0:
            suma += num
            contador += 1
        num += 1
    print ("La suma de los 50 primeros multiplos de 3 o 5 es: " + str(suma))













