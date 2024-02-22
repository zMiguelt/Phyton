cantidad = 1 
precio = 0
descuento = 0


precio =float(input("Que precio tiene las manzanas? "))

while cantidad != 0: 
    cantidad =int(input("Hola, cuantas manzanas deseas comprar: "))
    
    if cantidad == 18:
        descuento =(cantidad * precio)*.15
        print("descuento secreto")
        print(f"vas a pagar {(cantidad * precio)-descuento}")
        print(f"el descuentio es de: {descuento}")
    elif cantidad >= 10:
        descuento = (cantidad * precio)*.10
        print("Vas a pagar: ", (cantidad*precio) - descuento)
        print(f"el descuento es de: {descuento}")
    else:
        print("gracias por comprar")
        print("Vas a pagar: ", (cantidad*precio))
print("adios")