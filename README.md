# Ejercicios basicos Python
## Ejercicios básicos para interactuar y probar Python: ##

### Ejercicios basicos 1 ###

1.  Función que retorne el mayor de dos números o 0 si son iguales

2. Función que determine si una persona es mayor de edad o no (pista: el retorno debe ser un valor booleano)

3. Programar una función que determine si una empresa es microempresa o no (retorno booleano –True o False–). Se dice que es microempresa si tiene menos de 50 empleados, factura menos de 30 milones de euros y tiene un balance igual o inferior a los 5 millones de euros.

4.  Calcular el impuesto que debe pagar un contribuyente a partir de sus ingresos anuales y el número de hijos. El impuesto a pagar es un tercio del ingreso imponible, siendo este último igual a los ingresos totales menos una deducción personal de 600€ y otra deducción de 60€ por hijo. 

5.  Hacer los cálculos que permiten saber si una empresa de 20 empleados, 18 millones de euros de facturación y 5 millones de euros de balance es una micro empresa y almacenar el valor en una variable lógica (booleana).

6.  La temperatura expresada en grados centígrados TC, se puede convertir a grados Fahrenheit (TF) mediante la siguiente fórmula: TF = 9*TC/5 + 32. Programa una función para hacer esta transformación que reciba como argumento la temperatura en grados centígrados y retorne su equivalente en Farenheit. 

7.  Escribir una función Python que a partir de una cierta cantidad en euros y del tipo de cambio del día, retorne el equivalente en libras teniendo en cuenta que la casa de cambio retiene una comisión del 2% sobre el total de la operación. 

8.  Procedimiento que pinte una línea de asteriscos en pantalla 

9.  Programe un módulo en Python que reutilizando la función anterior muestre nuestros datos en pantalla con formato banner tal y como se representa abajo:
  (Linea de asteriscos)
  Autor: Miguel David Monzón;
  Email: miguel.monzon@uah.es
  (Lista de asteriscos)

10. Programa modularizado que, utilizando funciones, calcule el perímetro y el área de un círculo cuyo radio es proporcionado por el usuario 

11. Escribamos un programa para solicitar al usuario el numero de horas y el precio por hora con vistas a calcular su salario bruto. Las horas que sobrepasen 40 se considerarán extra y pagadas a 1,5 veces el precio de la hora regular.

12. Programar una función que determine si un número es par o impar. La función debe retornar verdadero o falso haciendo uso de valores booleanos.

13. Programar una función que determine si una letra es vocal o no.

14. Programar una función en Python que a partir de un número entero entre 1 y 7 que recibe como argumento retorne el día de la semana que corresponda, y un mensaje de error si el número no está entre 1 y 7.

15. Escribir una función que reciba un número y que muestre su tabla de multiplicar (hasta 10).

16. Programar una función que sume todos los elementos, entre el 1 y el 200, que sean múltiplos de 3 o de 5.

17. Programar una función que sume los 50 primeros elementos que sean múltiplos de 3 o de 5.

### Ejercicios basicos 2 ###

1. Modificar una lista de números reales que representan las calificaciones de los
alumnos de una clase, para sustituir los valores numéricos por sus calificaciones alfanuméricas (Suspenso, Aprobado, etc.)

2. Implementar una función que pone en mayúsculas todas las primeras letras de las palabras de una frase.

3. Implemente una función que indique si una palabra contiene las cinco vocales: por ejemplo “murciélago”. Modifique posteriormente la función para que detecte sólo aquellas palabras que contienen una única vez cada vocal.

4. Escribir una función que sume dos listas de igual longitud y retorne otra lista que contenga la suma de las originales elemento a elemento.

5. Modifique el ejercicio anterior permitiendo que las listas sean desiguales. En este caso, los elementos sobrantes de la lista más larga se añadirán al final de la lista resultante.

6. Crear una lista de enteros, inicializarlos según valores aleatorios en el rango 1..20 y computar la media de los valores, el valor más alto y el más bajo (todo ello utilizando listas). Utilizar las funciones para generación de números aleatorios de Python (https://docs.python.org/dev/library/random.html)

7. Implementar una función que compruebe si una palabra es un palíndromo.

8. Crear una función que compruebe si dos cadenas de caracteres son iguales recorriendo con un índice ambas cadenas (no puede utilizar cad1==cad2).

9. Distribuir 20 datos enteros leídos por teclado en dos listas de tal manera que se vayan generando dos secuencias ordenadas, una creciente y otra decreciente.

10. Escriba un programa que “codifique” una frase modificando todas las vocales según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el símbolo #. Por ejemplo, la frase: “Un perro del hortelano”, deberá devolverse: “#n p3rr0 d3l h0rt3l4n0”.

11. Crear un diccionario en python con parejas numero de tfno, nombre que represente una agenda telefónica. Posteriormente simular un manos libres, pidiendo al usuario “A quién desea llamar” y mostrando en pantalla el mensaje “Llamada al número XXX en curso” donde XXX seria el número telefónico de la persona elegida.

12. Escribir una función que reciba un tweet y retorne los hashtags en una lista

13. Escriba un programa que lea un archivo de texto y lo mete en una lista donde cada línea es una sublista

14. Realizar un programa que lea palabras hasta que se introduzca “fin”, mostrando una estadística de las longitudes de las palabras, es decir, el número total de palabras de longitud 1 que se hayan introducido, el total de longitud 2, etc. La máxima longitud de las palabras deberá ser de 25 caracteres. Una posible salida de este programa sería:

    Palabras longitud 1: 0
    
    Palabras longitud 2: 10
    
    ...
    
     Palabras longitud 25: 1
    
    