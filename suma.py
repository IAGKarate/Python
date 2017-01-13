import random 

print("Programa para sumar 2 numeros")

a = int(input("Ingrese el numero 1: "))
b = int(input("Ingrese el numero 2: "))

c=random.randint(a, b)
print(c)




suma = a+b
print("La suma es : ", suma )


edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")