estaturas = [] 

while True:
    accion = input("Ingresa una estatura (cm) o escribe 'mostrar', 'promedio' o 'salir': ").strip().lower()
    
    if accion == "salir":
        print("Saliendo del programa...")
        break
    elif accion == "mostrar":
        print(f"Estaturas registradas: {estaturas}" if estaturas else "No hay estaturas registradas.")
    elif accion == "promedio":
        if estaturas:
            promedio = sum(estaturas) / len(estaturas) 
            print(f"El promedio de las estaturas es: {promedio:.2f} cm")
        else:
            print("No hay estaturas registradas para calcular el promedio.")
    else:
        try:
            estatura = float(accion) 
            if estatura > 0:
                estaturas.append(estatura) 
                print("Estatura registrada.")
            else:
                print("Ingresa una estatura válida (mayor a 0).")
        except ValueError:
            print("Entrada no válida. Ingresa un número o un comando válido.")
    if not estaturas:
        print("No hay estaturas registradas. Finalizando programa...")
        break
