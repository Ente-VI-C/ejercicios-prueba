def menu():
  print("[1] Margarita: $8000 ")
  print("[2] Pepperoni: $9500")
  print("[3] Cuatro Quesos: $11000")
  print("[4] Napolitana: $10000")
  print("[5]Salida")

def menu_prop():
    print("Desea dejar una propina (Esta es un 10% del coste total)")
    print("[1] Si")
    print("[2] No")     

def env():
    global cos_env
    global dem
    while True:
        try:
            km=int(input("¿A cuantos kilometros esta usted de la pizzeria?: "))
            if km>=1 and km<=2:
              cos_env=1500   
              dem=20
              print(f"Se agregara un costo de envio de ${cos_env}, y el envio llegara en {dem} minutos aprox.")
              break
            elif km>2 and km<=5:
                cos_env=2500
                dem=35
                print(f"Se agregara un costo de envio de ${cos_env}, y el envio llegara en {dem} minutos aprox.")
                break
            elif km>5:
                cos_env=4000
                dem=50
                print(f"Se agregara un costo de envio de ${cos_env}, y el envio llegara en {dem} minutos aprox.")
                break
            else:
                print("Error, selecciona un numero mayor a 0")   
        except ValueError:
               print("Error, ingrese numeros")        


print("Bienvenido a la pagina de pizza nostra, ¿que pizza pedira?")

while True:
 menu()
 try:       
     opc=int(input("Ingrese que pizza quiere: "))
     if opc==1:
         pizza=8000   
         print(f"Pizza margarita elegida, esta cuesta ${pizza}") 
         break  
     elif opc==2:
         pizza=9500 
         print(f"Pizza pepperoni elegida, esta cuesta ${pizza}")
         break
     elif opc== 3:
         pizza=11000
         print(f"Pizza cuatro quesos elegida, esta cuesta ${pizza}")
         break
     elif opc==4:
         pizza=10000
         print(f"Pizza napolitana elegia, esta cuesta ${pizza}")
         break
     elif opc==5:
         print("Saliendo")
         break
     else:
        print("Error, elige una opcion valida")        
 except ValueError:
    print("Error, ingresa un numero")
env()
while True:
   menu_prop()
   try:
        prop=int(input("Seleccione: "))
        if prop==1:
            pizza=pizza+cos_env*(1.1)
            print(f"Decidio dejar propina, por lo que su compra paso a costar {pizza}")
            break
        elif opc==2:
            print("Decidio no dejar propina")
            break
        else:
            print("Error, seleccione una opcion valida")
   except ValueError:
    print("Error, ingrese numeros")

print(f"Su pedido de pizza llegara en {dem} minutos aproximados, y costara ${pizza}, gracias por la compra")
