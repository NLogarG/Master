# VARIABLES Y OPERADORES
# 1. Ejercicio: Crea una variable llamada nombre y asígnale tu nombre como valor. Luego, imprime la variable.
# 2. Ejercicio: Crea dos variables, a y b , y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de a y b .
# 3. Ejercicio: Calcula el área de un triángulo con base 10 y altura 5.
# 4. Ejercicio: Calcula el resto de dividir 17 entre 3

# 1
nombre = "Nacho"
print(nombre)

# 2
a = 5
b = 10
suma = a + b
print(suma)

# 3
base = 10
altura = 5
area = (base * altura)/2
print(area)

# 4
a = 17
b = 3
resto = a % b
print(resto)

# CONDICIONALES
# 1. Ejercicio: Dado un número, imprime si es positivo o negativo.
# 2. Ejercicio: Dado un número, imprime si es par o impar.
# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.

# 1
numero = int(input("Introduzca un numero: "))
if numero < 0:
  print("Es negativo")
elif numero > 0:
  print("Es positivo")


# 2
numero = int(input("Introduzca un numero: "))
if numero % 2 == 0:
  print("Es par")
else:
  print("Es impar")

# 3
a, b, c = 5, 7, 2
mayor = max(a, b, c)
print(mayor)


