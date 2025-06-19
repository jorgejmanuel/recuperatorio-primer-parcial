from funciones import*
import os

print("!!Hola bienvenido!!, por favor selecciones una de las siguientes opciones: ")
print()

while True:
    mostrar_menu()
    opcion = int(input("Su opcion: "))
    while opcion > 10 or opcion < 0:
        opcion = int(input("Reingrese su opcion (1-10): "))
    if opcion == 1:
        participantes = cargar_participantes()
        print("cargando la lista de los participantes: ")
        print()
        print(participantes)
        print()
    elif opcion == 2:
             puntaje = cargar_puntuacion(participantes)
             print()
    elif opcion == 3:
            mostrar_puntuaciones(puntaje)
            print()
    elif opcion == 4:
            promedios_mayor_a_4(puntaje,participantes)
            print()
    elif opcion == 5:
            promedios_mayor_a_7(puntaje,participantes)
            print()
    elif opcion == 6:
            print("mostrando promedios: ")
            promedio_por_jurados(puntaje)
            print()
    elif opcion == 7:
            print("mostrando al jurado mas estricto: ")
            jurado_mas_estricto(puntaje)
            print()
    elif opcion == 8:
            print("buscando por nombre.")
            buscar_participante_por_nombre(puntaje)
            print()
    elif opcion == 9:
            print("buscando el top con mayor puntaje: ")
            top_3_participantes(puntaje)
            print()
    elif opcion == 10:
            print("ordenando los participantes en orden alfabetico: ")
            participantes_alfabeticamente(puntaje)
            print()
    elif opcion == 0:
            print("cerrando el sistema... ")
            break

    else:
            print("ERROR: Opción no válida. Intente nuevamente.")

    input("toque cualquier boton para continuar. ")
    print("regresando.")
    os.system("cls")