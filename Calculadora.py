
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))


while True:
    
    print("""
    Indique la operación que desea realizar:
          
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Cambio de valores
    6) Salir
    """)
    
    
    eleccion = int(input("Ingrese su elección: "))

    
    if eleccion == 6:
        print("Calculadora creada por: Santiago Duarte Zuckerberg")
        break

    
    if eleccion == 5:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        continue

    
    if eleccion < 1 or eleccion > 6:
        print("Opción inválida. Por favor, elija una opción válida.")
        continue

    
    if eleccion == 1:
        print("Resultado:", numero1, "+", numero2, "=", numero1 + numero2)
    elif eleccion == 2:
        print("Resultado:", numero1, "-", numero2, "=", numero1 - numero2)
    elif eleccion == 3:
        print("Resultado:", numero1, "*", numero2, "=", numero1 * numero2)
    elif eleccion == 4:
        
        if numero2 != 0:
            print("Resultado:", numero1, "/", numero2, "=", numero1 / numero2)
        else:
            print("No se puede dividir entre cero.")




