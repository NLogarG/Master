#Bucles FOR
# Iterar sobre una lista
nombres = ["Ana", "Juan", "Carlos"]
for nombre in nombres:
  print(nombre)

# Interar sobre una cadena
s = "Hola mundo"
for letra in s:
  print(letra) 

#Bucles WHILE
#Imprimir numeros del 1 al 5
i = 1
while i <= 5:
  print(i)
  i += 1

#MAS EJEMPLOS
numeros = [1,2,3,4,5]
suma = 0

for numero in numeros:
  suma += numero

print("La suma es:", suma)


numeros = [12, 16, 18, 20, 25]
i = 0
while numeros[i] % 5 !=0:
  i += 1
print(numeros[i])


numeros = [1,3,9,16,20,22,25]
for numero in numeros:
    if numero % 8 == 0:
      print("El pimer numero divisible por 8 encotrado es: ", numero)
      break


numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
  if numero % 2 == 0:
    print(numero)


texto = "Hola mundo"
vocales = "aeiouAEIOU"
for letra in texto:
  if letra in vocales:
    print(letra)


numero = -1
while numero < 0:
  numero = int(input("Introduzca un numero positivo:"))


numeros = [5, 8, 10, -3, 2, 1]
for numero in numeros:
  if numero < 0:
    print("El primer numero negativo es: ", numero)
    break