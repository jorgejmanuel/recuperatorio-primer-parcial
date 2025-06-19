#MOSTRAR MENU
def mostrar_menu():
    print("1. cargar nombres\n2. cargar puntuacion\n3. mostrar puntuaciones\n4. ver participantes con promedio mayor a 4\n5. ver participantes con promedio mayor a 7 \n6. ver promedio de jurados\n7. ver jurado más estricto\n8. buscar participante por nombre\n9. mostar el top 3 con mayor promedio\n10. ordenar participantes alfabeticamente\n0. cerrar sistema. ")
#CARGAR LOS PARTICIPANTES:
def cargar_participantes () -> list: 
    participantes = []
    for i in range (5):
        nombre_participantes = input(f"ingrese el nombre del participante {i+1}: ")
        participantes += [nombre_participantes]
        while len(nombre_participantes) < 3 or nombre_participantes == int:
            print("Nombre inválido")
            nombre_participantes = input (f"reingrese el nombre del participante {i+1}: ")
    return participantes

#CARGAR LAS PUNTUACIONES:
def cargar_puntuacion(participantes) -> list:
    puntos_de_participante = []
    for nombre_participante in participantes:
        print(f"ingrese la puntuacion del participante {nombre_participante}...")
        puntaje = []
     
        for j in range (1, 4):
            nota = int (input(f"ingresar la puntuacion del jurado {j} (1-10): "))
            print()
            while nota < 1 or nota > 10:
                print("INGRESAR UN NUMERO VALIDO")
                nota = int(input(f"reingrese la puntuacion del jurado {j} (1-10): "))
            puntaje += [nota]
        
        puntos_de_participante += [[nombre_participante, puntaje]]
    return puntos_de_participante

#MUESTRAR PUNTUACIONES:
def mostrar_puntuaciones (participantes:list):


    print()
    print("informacion de cada participante: ")
    print()
    for participante in participantes:
        nombre = participante [0]
        puntos = participante [1]

        print (f"nombre del participante: {nombre}")
        total = 0
        for i in range (len(puntos)):
            print(f"puntaje del jurado {i+1}: {puntos[i]} ")
            total += puntos[i]
        promedio = total/ len(puntos)
        print(f"promedio: {promedio}")
        print()

#MOSTRAR PROMEDIO MAYOR A 4:
def promedios_mayor_a_4(puntos_de_participante: list, promedio_mayor_4: float ):
    print()
    print(f"\nparticipantes con un promedio superior a 4 {promedio_mayor_4}: \n ")
    bandera = False
    for participante in puntos_de_participante:
        nombre = participante [0]
        puntos = participante [1]

        total = 0
        for p in puntos:
            total += p
        
        promedio = total /len(puntos)
        if promedio > 4:
            print (f"{nombre} promedio: {promedio}\n ")
            bandera = True
    if bandera == False: 
        print(" NO HAY CONCURSANTE CON ESE PROMEDIO:" )

#MOSTRAR PROMEDIO MAYOR A 7:
def promedios_mayor_a_7(puntos_de_participante: list, promedio_mayor_7: float ):
    print()
    print(f"\n participantes con un promedio superior a 4 {promedio_mayor_7}: \n ")
    bandera = False
    for participante in puntos_de_participante:
        nombre = participante [0]
        puntos = participante [1]

        total = 0
        for p in puntos:
            total += p
        
        promedio = total /len(puntos)
        if promedio > 7:
            print (f"{nombre} promedio: {promedio}\n ")
            bandera = True
    if bandera == False: 
        print(" NO HAY CONCURSANTE CON ESE PROMEDIO:" )

#MOSTRAR PROMEDIO POR JURADOS:
def promedio_por_jurados(puntos_de_participantes):
    print("\nPromedio de puntuaciones por jurado:\n")
    total_participantes = len(puntos_de_participantes)
    total_jurados = len(puntos_de_participantes[0][1])

    for i in range(total_jurados):
        suma = 0
        for participante in puntos_de_participantes:
            suma += participante[1][i]
        promedio = suma / total_participantes
        print(f"Jurado {i + 1}: {promedio:.2f}")

#MOSTRAR JURADO MAS ESTRICTO:
def jurado_mas_estricto(puntos_de_participantes):
    total_participantes = len(puntos_de_participantes)
    total_jurados = len(puntos_de_participantes[0][1])

    promedio_mas_bajo = None
    indice_estricto = -1

    for i in range(total_jurados):
        suma = 0
        for participante in puntos_de_participantes:
            suma += participante[1][i]
        promedio = suma / total_participantes

        if promedio_mas_bajo is None or promedio < promedio_mas_bajo:
            promedio_mas_bajo = promedio
            indice_estricto = i

    print(f"\n el jurado mas estricto: Jurado {indice_estricto + 1} (promedio {promedio_mas_bajo:.2f})")

#busqueda por nombre 
def buscar_participante_por_nombre(puntos_participante: list):
    buscar_participante = input("ingresar nombre del participante que desea buscar: ")
    encontrado = False
    print()

    for participante in puntos_participante:
        nombre = participante[0]
        puntos = participante[1]

        if buscar_participante == nombre:
            print("Se ah encontrado al participante, cargando sus datos.")
            print(f"Nombre: {nombre}")
            total = 0
            for i in range(len(puntos)):
                print(f"Puntaje del jurado {i+1}: {puntos[i]}")
                total += puntos[i]
            promedio = total / len(puntos)
            print(f"Promedio: {promedio}")
            encontrado = True
            print()
            break
    if not encontrado:
        print("Error al encontrar participante. Por favor ingrese un nombre valido.") 

#BUSCAR EL TOP 3:
def top_3_participantes(puntos_de_participantes):
    print("\n Top 3 participantes con mayor puntaje promedio:\n")

    promedios = [ ["", 0] for l in range(len(puntos_de_participantes)) ]

    for i in range(len(puntos_de_participantes)):
        nombre = puntos_de_participantes[i][0]
        puntajes = puntos_de_participantes[i][1]

        total = 0
        cantidad = 0
        for j in range(len(puntajes)):
            total += puntajes[j]
            cantidad += 1

        promedio = total / cantidad
        promedios[i][0] = nombre
        promedios[i][1] = promedio

    for i in range(len(promedios) - 1):
        for j in range(i + 1, len(promedios)):
            if promedios[j][1] > promedios[i][1]:
                promedios[i][0], promedios[i][1], promedios[j][0], promedios[j][1] = (
                    promedios[j][0], promedios[j][1], promedios[i][0], promedios[i][1])

    top = 3
    if len(promedios) < 3:
        top = len(promedios)

    for i in range(top):
        print(f"{i+1}. {promedios[i][0]} - Promedio: {promedios[i][1]:.2f}")

#ORDENAR PARTICIPANTES ALFABETICAMENTE:
def participantes_alfabeticamente(puntos_de_participantes):   
  
    for i in range(len(puntos_de_participantes) - 1):
        for j in range(i + 1, len(puntos_de_participantes)):
            if puntos_de_participantes[j][0] < puntos_de_participantes[i][0]:
                puntos_de_participantes[i][0], puntos_de_participantes[j][0] = puntos_de_participantes[j][0], puntos_de_participantes[i][0]
                puntos_de_participantes[i][1], puntos_de_participantes[j][1] = puntos_de_participantes[j][1], puntos_de_participantes[i][1]

    print("\nParticipantes ordenados alfabéticamente:\n")
    for i in range(len(puntos_de_participantes)):
        nombre = puntos_de_participantes[i][0]
        puntajes = puntos_de_participantes[i][1]

        total = 0
        cantidad = 0
        for j in range(len(puntajes)):
            total += puntajes[j]
            cantidad += 1
        promedio = total / cantidad

        print(f"{nombre}: Puntajes = {puntajes}, Promedio = {promedio:.2f}")        