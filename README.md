# Python_para_principiantes
Ejercicios resueltos del curso online Python para principiantes de la UMA.



TEMA 1:
--------------------------------------------------------------------------------------------------------------------------
Unidad 2: Escribir un programa que pregunte al usuario un número de horas y el precio por hora para calcular el total a pagar.

TEMA 2:
--------------------------------------------------------------------------------------------------------------------------
Unidad 3:

1. Reescribe el programa de pagos para incrementar en un factor de 1.5 las horas que se trabajen por encima de 40 horas.

2. Reescribe el programa de pagos usando try y except para que se manejen adecuadamente entradas no numéricas (nota: no hace falta que se vuelvan a pedir los números si falla)

Unidad 4: Reescribe
el cálculo del pago por horas de la unidad anterior y escribe una función llamada calculapago que toma dos parámetros (horas y precio ) y devuelve el total a pagar.

Unidad 5: Escribe un programa que pida números al usuario hasta que escriba 'fin'. Una vez escrito 'fin', el programa debe mostrar el número más grande y el más pequeño . Si el usuario escribe algo diferente a un número , se debe capturar con un try/except e ignorar el valor introducido.

Probar con 7, 2, bob, 10, y 4

TEMA 3: 
--------------------------------------------------------------------------------------------------------------------------
Unidad 6: Utilizar find() y los slices (:) para extraer el número en el string que se indica a continuación. Convertir el número a flotante y mostrarlo.

"X DSPAM Confidence: 0.8475"

Unidad 7: Escribir un programa que pregunte por un nombre de archivo, lo abra, y lo lea mostrando las líneas de la forma:
X DSPAM Confidence: 0.8475

Contar las líneas y extraer los valores flotantes de cada una de ellas, calculando el promedio y mostrándolo al final.

Los datos de muestra se encuentran en el archivo mbox-short.txt. El valor promedio resultante debería ser: 0.7507185185185187

TEMA 4
--------------------------------------------------------------------------------------------------------------------------
Unidad 8: 

1. Abre el archivo romeo.txt y léelo línea a línea. Para cada línea, divide la línea en palabras usando el método split(). El programa debería construir una lista de palabras. Para cada palabra de cada línea , comprobar si ya estaba en la lista, y si no, añádela. Cuando el programa termine, ordenar la lista y mostrar las palabras resultantes en orden alfabético.

2. Abre el archivo mbox-short.txt y léelo línea a línea. Cuando encuentres una línea que comience con 'From' como la siguiente:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 
trocea la línea usando split() e imprime la segunda palabra de la línea (es decir , la dirección de la persona que envió el mensaje). Al final, indica cuántas personas hubo (no es necesario tener en cuenta repeticiones

Nota: asegúrate de no incluir las líneas que comiencen con 'From:'.

Unidad 9: Escribe un programa que lea el archivo mbox-short.txt e indique quién ha enviado el mayor número de e mails junto con el número de e-mails. El programa busca líneas con 'From' y toma la segunda palabra de estas líneas como la persona que envió el e-mail.

Debes crear un diccionario Python que mapea el nombre del emisor con el número de veces que aparece en el archivo. Después de generar el diccionario, el programa itera a través del diccionario para ver quién ha sido el emisor con más mensajes.

Unidad 10: Escribe un programa que lea el archivo mbox-short.txt y muestre la distribución por horas del día de los mensajes.

Se puede extraer la hora de las líneas que comiencen por 'From', extrayendo la hora completa y dividiendo una segunda vez con los ':' como delimitador.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16
2008

Una vez hayas obtenido el total de mensajes en cada hora, muestra los totales ordenados por hora. Deberías obtener el resultado que se muestra abajo

04 3

06 1

07 1

09 2

10 3

11 6

14 1

15 2

16 4

17 2

18 1

19 1

