def saludar():
  print("Hola mundo")
saludar()


def saludar(nombre):
  print(f"Hola {nombre}")
saludar("Nacho")


def suma(a ,b):
  return a + b
resultado = suma(5, 3)
print(resultado)


def suma_lista(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma
mi_lista = [1,2,3,4,5]
print(suma_lista(mi_lista))


def maximo_lista(numeros):
  maximo = numeros[0]
  for numero in numeros:
    if numero > maximo:
      maximo = numero
  return maximo
mi_lista = [1, 2, 3, 4, 5]
print(maximo_lista(mi_lista)) # Muestra: 5
