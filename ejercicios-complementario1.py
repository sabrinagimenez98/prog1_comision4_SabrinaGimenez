numero1=int(input("Escribe un numero entero: "))
numero2=float(input("Escribe un numero decimal: "))
suma= numero1+numero2
print(f"La suma es {suma}")
resta = numero1-numero2
print(f"La resta es {resta}")
multiplicacion= numero1*numero2
print(f"La multiplicacion es {multiplicacion}")
division= numero1/numero2
print(f"La division es {division}")
nombre=input("Dime tu nombre: ")
precio=float(input("Dime el precio del articulo; "))
descuento=floar(input("Dime el descuento: "))
precio_final=precio*(100-descuento)/100
print(f"El precio final es {precio_final}")
cadena=str(input("Dime una algo"))
longitud=len(cadena)
precioentero=int(input("Dime un precio decimal"))
nombre=str(input("Dime tu nombre: "))
apellido=str(input("Dime tu apellido: "))
nombre_completo=nombre + apellido
print(f"Tu nombre completo es: {nombre_completo}")
edad=int(input("Dime tu edad"))
despues=edad+5
antes=edad-10
print(f"Hace 10 años tenias {antes}")
print(f"En 5 años tendras {despues}")
altura=float(input("Dime tu altura en metros y centimetros"))
alto= altura*4
bajo= altura/3