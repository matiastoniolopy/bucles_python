# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

print('1. suma.')
print('2. resta.')
print('3. multiplicacion.')
print('4. division.')
print('5. exponente.')
print('6. FIN.\n')

numero = int(input('seleccione una opcion:\n'))

while numero == 1:
    print('seleccionaste suma\n')
    numero = int(input('ingrese el primer numero: '))
    numero+= int(input('ingrese el segundo numero: '))
    print('el resultado de la suma es', numero)
    if numero == 1:
        continue
while numero == 2:
    print('seleccionaste resta\n')
    numero = int(input('ingrese el primer numero: '))
    numero-= int(input('ingrese el segundo numero: '))
    print('el resultado de la resta es', numero)
    if numero == 2:
        continue
while numero == 3:
    print('seleccionaste multiplicacion\n')
    numero = int(input('ingrese el primer numnero: '))
    numero*= int(input('ingrese el segundo numero: '))
    print('el resultado de la multiplicacion es', numero)
    if numero == 3:
        continue
while numero == 4:
    print('seleccionaste division\n')
    numero = int(input('ingrese el primer numero: '))
    numero/= int(input('ingrese el segundo numero: '))
    print('el resultado de la division es', numero)
    if numero == 4:
        continue
while numero == 5:
    print('seleccionaste exponente\n')
    numero = int(input('ingrese el primer numero: '))
    numero**= int(input('ingrese el segundo numero: '))
    print('el resultado del exponente es', numero)
    if numero == 5:
        continue
while numero == 6:
       break


    
