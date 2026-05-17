# Ejercicio 1.
print ("Bienvenido al sistema de descuentos.")
precio_medicameto = 60000
precio_despacho = 8000

edad = int(input(" por favor ingrese su edad:"))
tramo = input("Ingrese su tramo (A, B, C, D):").strip().upper()

descuento_med = 0.0
desc_despacho = 0.0

if edad <= 30:
    if tramo in ["A", "B"]:
        descuento_med = 0.18
    elif tramo in ["C", "D"]:
        descuento_med = 0.12
elif 31 <= edad <= 60:
    if tramo in ["A", "B"]:
         descuento_med = 0.12
    elif tramo in ["C", "D"]:
        descuento_med = 0.08
else:
    # si edad es mayor a 60 no hay descuento.
    descuento_med = 0.0
    
#Descuentos para el despacho 
if tramo in ["A", "B"]:
    desc_despacho = 0.10
    
    if edad >= 55:
        desc_despacho += 0.05

descuento_med = int(precio_medicameto * (1 - descuento_med))
desc_despacho = int(precio_despacho *(1 - desc_despacho ))

print(f" el valor del medicamento es: {descuento_med}")
print(f"El valor de despacho es: {desc_despacho}")

