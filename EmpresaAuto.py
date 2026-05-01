bonoxl=500000
bono=50000
while True:
    cantidad_autos=0
    dias_pas=0
    monto_total=0

    while True:
        try:
            dias = int(input("Ingrese cantidad de días a analizar "))   
            break   
        except ValueError:
            print("Error en los caracteres, intente de nuevo")
    while dias_pas<dias:
        try:
            monto=float(input("Ingrese monto total de los autos vendidos en el día "))              
            auto=int(input("Ingrese la cantidad de autos vendidos en el día "))
            cantidad_autos=cantidad_autos+auto
            dias_pas=dias_pas+1
            monto_total=monto_total+monto
            if dias_pas<dias:
                print("Ok, vamos con el siguiente día")
        except ValueError:
            print("Error en los caracteres, intente de nuevo")            

    if monto_total>bonoxl:
        resultado="Obtuvo un 0km"
    elif monto_total>bono:
        resultado="Obtuvo el Bono"
    else:
        resultado="No obtuvo el Bono"
    print("Vendió:",cantidad_autos,"autos")
    print("Facturó:",monto_total)
    print("Resultado:",resultado)
    while True:
        otro=input("Desea realizar otro analisis? Si/No ").strip().lower()
        if otro in ("si","no"):
            break
    if otro=="si":
        print("Vamos de nuevo con este siguiente analisis :D")
    else:
        print("Gracias por utilizar el programa, hasta luego")
        break
    