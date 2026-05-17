from random import randint

num1 = int(input("Ingrese límite inferior: "))
num2 = int(input("Ingrese límite superior: "))

numero = randint(num1, num2)

if numero % 2 != 0:
    if numero + 1 <= num2:
        numero += 1
    else:
        numero -= 1

intento1 = int(input("Intente adivinar: "))

if intento1 == numero:
    print("Felicitaciones, adivinó en el primer intento.")
else:
    if numero > intento1:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    
    intento2 = int(input("Intente de nuevo: "))
    
    if intento2 == numero:
        print("Felicitaciones, adivinó en su segundo intento.")
    else:
        if numero > intento2:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        
        print("Te daré una pista:")
        distancia1 = abs(numero - intento1)
        distancia2 = abs(numero - intento2)
        
        if distancia1 < distancia2:
            print(f"El número que buscas está más cerca de {intento1} que de {intento2}")
        elif distancia2 < distancia1:
            print(f"El número que buscas está más cerca de {intento2} que de {intento1}")
        else:
            print(f"El número que buscas está a la misma distancia de {intento1} y de {intento2}")

        intento3 = int(input("Intente la última vez: "))
        
        if intento3 == numero:
            print("Felicitaciones, pudiste adivinar.")
        else:
            print("Perdiste.")
            print(f"El número era: {numero}")
