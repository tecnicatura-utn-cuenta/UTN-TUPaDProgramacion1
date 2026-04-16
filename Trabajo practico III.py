#Ejercicio 1 - ''caja del kiosko''

nombre_cliente = input("Ingresar nombre: ")

while not nombre_cliente.isalpha():

    print("ERROR: el nombre solo debe contener letras.")
    nombre_cliente = input("Ingresar nombre nuevamente: ")


productos = input("Ingresar numero de productos a comprar: ")

while not productos.isdigit() or int(productos) == 0:

    print("ERROR: ingrese un numero mayor a 0.")
    productos = input("Ingresar numero nuevamente: ")

productos = int(productos)

total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(productos):
    precio = int(input(f"Precio del producto: {i + 1}: "))

    while not precio.isdigit():
        precio = input("ERROR: ingresar numero: ")
    precio_original = precio

    descuento = input("El producto tiene descuento S/N: ")
    while descuento.lower() != "s" and descuento.lower() != "n":
        descuento = input("ERROR: volver a ingresar: ")
    if descuento.lower() == "s" :
            precio_descuento = precio * 0.9
    else:
            precio_con_descuento = precio

    total_sin_descuentos += precio_original
    total_con_descuentos += precio_con_descuento

ahorro_total = (int(total_sin_descuentos - total_con_descuentos))
promedio = total_con_descuentos / productos

print(f"Total sin descuentos: {total_sin_descuentos}") 
print(f"Total con descuento: {precio_con_descuento}") 
print(f"Ahorro total: {ahorro_total}")
print(f"Promedio por producto: {promedio}")

#Ejercicio 2 - ''acceso al campus y menu seguro''


usuario_correcto = "alumno"
contraseña_correcta = "python123"

acceso = False

for intento in range(1, 4):
    print(f"intento {intentos}/3 - usuario:")
    usuario = input()

    print("Contraseña: ")
    contraseña = input()

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Usuario y contraseñas correctas")
        acceso = True
        break

    else:
         print("Vuelva a intentar.")

    if intento >= 3:
         print("cuenta bloqueada")

if acceso:

    opcion = 0

    while opcion != 4:
        print("1 - ver estado de inscripcion")
        print("2 - cambiar contraseña")
        print("3 - mensaje motivacional")
        print("4 - salir")

        opcion = input("Elegir opcion: ")

        if not opcion.isdigit():
            print("ERROR: ingrese un numero valido. ")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("ERROR: opcion no valida")
            continue

        if opcion == 1:
            print("Estado: inscripto")
        
        elif opcion == 2:
            nueva = input("Nueva contraseña: ")
            confirmacion = input("Confirmar contraseña: ")
            if len(nueva) < 6:
                print("clave rechazada: debe tener al menos 6 caracteres")
            elif nueva != confirmacion:
                print("la contraseña no coincide: ")
            else:
                contraseña_correcta = nueva
                print("clave actualizada correctamente")
        elif opcion == 3:
            print("Si alguien te pide que hagas algo por ellos, hacelo de mala gana asi nunca lo tenes que volver a hacer - Paris Hilton")
        elif opcion == 4:
            print("saliste")
            
else: 
    print("cuenta bloqueada")


#Ejercicio 3 -  "Agenda de Turnos con Nombres (sin listas)"


lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""


martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador: ")
while operador.isalpha() == False:
    operador = input("Error. Solo letras: ")

opcion = ""

while opcion != "5":

    print("1- reservar")
    print("2- cancelar")
    print("3- ver agenda")
    print("4- resumen")
    print("5- salir")

    opcion = input("Opcion: ")

    if opcion == "1":

        dia = input("dia: 1 lunes o 2 martes: ")
        while dia != "1" and dia != "2":
            dia = input("ERROR Ingrese 1 o 2: ")

        nombre = input("nombre del paciente: ")
        while nombre.isalpha() == False:
            nombre = input("ERROR. Solo letras: ")

        if dia == "1":

            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("ya existe ese paciente")
            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("no hay cupos")

        if dia == "2":

            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("ya existe ese paciente")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("no hay lcupos")


    if opcion == "2":

        dia = input("Dia 1 lunes o 2 martes: ")
        while dia != "1" and dia != "2":
            dia = input("ERROR Ingrese 1 o 2: ")

        nombre = input("Nombre paciente: ")
        while nombre.isalpha() == False:
            nombre = input("ERROR Solo letras: ")

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("no encontrado")

        if dia == "2":
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No encontrado")

    if opcion == "3":

        dia = input("Dia 1 lunes o 2 martes: ")
        while dia != "1" and dia != "2":
            dia = input("ERROR Ingrese 1 o 2: ")

        if dia == "1":
            print("Lunes")
            print("1:", lunes1 if lunes1 != "" else "libre")
            print("2:", lunes2 if lunes2 != "" else "libre")
            print("3:", lunes3 if lunes3 != "" else "libre")
            print("4:", lunes4 if lunes4 != "" else "libre")

        if dia == "2":
            print("Martes")
            print("1:", martes1 if martes1 != "" else "libre")
            print("2:", martes2 if martes2 != "" else "libre")
            print("3:", martes3 if martes3 != "" else "libre")


    if opcion == "4":

        ocup_lunes = 0
        ocup_martes = 0

        if lunes1 != "":
            ocup_lunes = ocup_lunes + 1
        if lunes2 != "":
            ocup_lunes = ocup_lunes + 1
        if lunes3 != "":
            ocup_lunes = ocup_lunes + 1
        if lunes4 != "":
            ocup_lunes = ocup_lunes + 1

        if martes1 != "":
            ocup_martes = ocup_martes + 1
        if martes2 != "":
            ocup_martes = ocup_martes + 1
        if martes3 != "":
            ocup_martes = ocup_martes + 1

        print("lunes ocupados:", ocup_lunes)
        print("martes ocupados:", ocup_martes)

        if ocup_lunes > ocup_martes:
            print("mas turnos en lunes")
        elif ocup_martes > ocup_lunes:
            print("mas turnos en martes")
        else:
            print("iguales")
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        print("opcion incorrecta")

print("fin del sistema")

#Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

nombre = input("ingrese nombre del agente: ")
while not nombre.isalpha():
    nombre = input("ERROR. ingrese solo letras: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("sistema bloqueado. perdiste.")
        break

    print("energia:", energia)
    print("tiempo:", tiempo)
    print("cerraduras abiertas:", cerraduras_abiertas)
    print("alarma:", alarma)

    print("1. forzar cerradura")
    print("2. hackear panel")
    print("3. descansar")

    opcion = input("opcion: ")
    while not opcion.isdigit() or (int(opcion) != 1 and int(opcion) != 2 and int(opcion) != 3):
        opcion = input("ERROR. elegi 1, 2 o 3: ")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            print("se trabo la cerradura. alarma activada.")
            alarma = True
            continue

        if energia < 40:
            riesgo = input("ingrese numero del 1 al 3: ")
            while not riesgo.isdigit() or (int(riesgo) != 1 and int(riesgo) != 2 and int(riesgo) != 3):
                riesgo = input("ERROR. ingrese 1, 2 o 3: ")

            if int(riesgo) == 3:
                alarma = True
                print("alarma activada")
            else:
                cerraduras_abiertas += 1
                print("abriste una cerradura")
        else:
            if not alarma:
                cerraduras_abiertas += 1
                print("abriste una cerradura")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("hackeando")
        for i in range(4):
            print("paso", i+1)
            codigo_parcial += "a"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("se abrio una cerradura")

    elif opcion == 3:
        tiempo -= 1
        racha_forzar = 0

        energia += 15
        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10

        print("descansaste")

print("resultado final:")

if cerraduras_abiertas == 3:
    print("ganaste")
elif energia <= 0 or tiempo <= 0:
    print("perdiste")
elif alarma and tiempo <= 3:
    print("perdiste por bloqueo")
else:
    print("fin del juego")


#Ejercicio 5: Arena Gladiador

nombre = ""
while nombre == "" or nombre.isalpha() == False:
    nombre = input("nombre del gladiador: ")
    if nombre == "" or nombre.isalpha() == False:
        print("ERROR: solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12

print("inicio del combate")

while vida_jugador > 0 and vida_enemigo > 0:

    print("nuevo turno")
    print(nombre + " (hp: " + str(vida_jugador) + ") vs enemigo (hp: " + str(vida_enemigo) + ") | pociones: " + str(pociones))

    opcion = ""
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 3:
        print("elige accion:")
        print("1. ataque pesado")
        print("2. rafaga veloz")
        print("3. curar")
        opcion = input("opcion: ")

        if opcion.isdigit() == False:
            print("ERROR: ingrese un numero valido.")
        else:
            if int(opcion) < 1 or int(opcion) > 3:
                print("ERROR: opcion fuera de rango.")

    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_base * 1.5
            print("golpe critico")
        else:
            danio = danio_base

        vida_enemigo = vida_enemigo - danio
        print("atacaste al enemigo por " + str(danio) + " puntos de daño")

    elif opcion == 2:
        print("inicias una rafaga de golpes")
        for i in range(3):
            vida_enemigo = vida_enemigo - 5
            print("> golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador = vida_jugador + 30
            pociones = pociones - 1
            print("te has curado 30 puntos de vida")
        else:
            print("no quedan pociones")

    if vida_enemigo > 0:
        vida_jugador = vida_jugador - danio_enemigo
        print("el enemigo te ataco por " + str(danio_enemigo) + " puntos de daño")

print("fin del combate")

if vida_jugador > 0:
    print("victoria! " + nombre + " ha ganado la batalla.")
else:
    print("derrota. has caido en combate.")