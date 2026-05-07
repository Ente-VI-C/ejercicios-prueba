def menu():
    print("Aqui estan los destinos turisicos junto a sus respectivos paquetes") 
    print("[1] San Pedro de Atacama ($120000 por persona)")
    print("[2] Torres del Paine ($150000 por persona)")
    print("[3] Isla de Chiloé ($90000 persona)")
    print("[4 Salir del menu")
#----
def descuento():
    try:
        if cant>=4:
            des=pack*0.90  
            print(f"Al ser {cant} personas se aplica un descuento del 10%, el coste ahora es de {des}")         
    except ValueError:
        print("Error, como siquiera sacas este error?")
        breakpoint
#-----
while True:
 try:
     menu()
     cant=int(input("Ingresa la cantidad de persona que iran al viaje: ")) 
     opc=int(input("Seleccione un destino turistico: "))   
     if opc==1:
         pack=120000*cant
         print(f"Eligio San Pedro de Atacama con {cant} persona/s, el coste es ${pack}")
         break
     elif opc==2:
            pack=150000*cant
            print(f"Eligio Torres del Paine con {cant} persona/s, el coste es ${pack}")
            break
     elif opc==3:
            pack=90000*cant
            print(f"Eligio Isla de Chiloé con {cant} personas/s el coste es  ${pack}")
            break
     elif opc==4:
            print("Saliendo")
            break
     else:
            print("Error, ingrese numeros validos")    
 except ValueError:
           print("Error, ingrese numeros" )
descuento()   
