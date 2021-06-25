def verificar_usuario(diccionario) :
    a=0
    while a==0 :
        celular = input('Digite su numero de celular: ')
        nip = input('Digite su NIP: ')
        key = (celular,nip)

        if key in diccionario :
            a+=1
        else :
            print('\n' + '> EL USUARIO NO EXISTE' + '\n')
            a=0
    return key

def registar_usuario(diccionario) :

    lista = []
    nombre = input('Ingresa tu nombre: ')
    lista.append(nombre) #Posicion 0
    apellidos = input('Ingresa tus apellidos: ')
    lista.append(apellidos) #Posicion 1
    celular = input('Digite su numero telefonico: ')
    tarjeta = input('Digite su numero de Tarjeta: ')
    lista.append(tarjeta) #Posicion 2
    nip = input('Cree un NIP (4 digitos): ')
    saldo = float(0)
    lista.append(saldo) #Posicion 3

    key = (celular,nip)
    value = lista

    diccionario[key] = value
    print('\nRegistro Exitoso!!')


def depositar_dinero(diccionario) :

    key = verificar_usuario(diccionario)
    value = list(diccionario[key])

    print('\n' +'Bienvenido', value[0] + ' ' + value[1] + '\n')

    i=0
    while i == 0 :
        cantidad = float(input('Digite la cantidad deseada a depositar : '))
        opcion = input('¿Estas seguro?  ').upper()
        if opcion == 'SI' :
            value[3] = value[3] + cantidad
            diccionario[key] = value
            print('\n' + 'Se ha depositado', cantidad , 'a su tarjeta ')
            i+=1
        elif opcion == 'NO' :
            i=0

def verificar_saldo(diccionario) :

    key = verificar_usuario(diccionario)
    value = list(diccionario[key])

    print('\n' + 'Bienvenido', value[0] + ' ' + value[1])
    print('El saldo en su tarjeta es : ', value[3])

def transferir_dinero(diccionario) :

    key = verificar_usuario(diccionario)
    value = list(diccionario[key]) #El que da dinero

    print('\n' + 'Bienvenido', value[0] + ' ' + value[1])
    print('El saldo en su tarjeta es : ', value[3])
    print('\n')
    
    j=0
    while j==0 :

        nombre = input('Nombre de la persona a depositar: ')
        tarjeta = input('Numero de la tarjeta a depositar: ')

        for keys,values in diccionario.items() :
            i=0
            lista=[]
            for valor in values :
                lista.append(valor)
                if nombre == valor :
                    i+=1
                if tarjeta == valor :
                    i+=1
            if i==2 :
                receptor = keys
                break

        if i==2 :
            a=0
            while a==0 :
                cantidad = float(input('\n' + 'Digite la cantidad deseada a depositar : '))
                if cantidad <= value[3] :
                    opcion = input('¿Estas seguro?  ').upper()
                    if opcion == 'SI' :
                        lista[3] = lista[3] + cantidad
                        diccionario[receptor] = lista
                        saldo = value[3] - cantidad
                        value[3] = round(saldo,2)
                        diccionario[key] = value
                        print('> TRANSFERENCIA EXITOSA !!' + '\n')
                        print(nombre + ' ' + lista[1])
                        print('Tarjeta:  ' + lista[2])
                        print('\n' + 'Saldo Anterior: ', value[3]+cantidad)
                        print('Monto Transferido : ', cantidad)
                        print('Saldo actual: ', value[3])
                        a+=1
                        j+=1
                    else:
                        a=0
                else :
                    print('\n' + ' > NO CUENTA CON SUFICIENTE DINERO')
                    a=0
        else :
            print('> LA PERSONA NO EXISTE')
            j=0

def recarga_tiempo_aire(diccionario) :

    key = verificar_usuario(diccionario)
    value = list(diccionario[key])

    print('\n' + 'Bienvenido', value[0] + ' ' + value[1])
    print('El saldo en su tarjeta es : ', value[3])

    a=0
    while a==0 :
        print('----RECARGA TIEMPO AIRE----')
        print('1. AT&T')
        print('2. Telcel')
        print('3. Movistar')
        opcion = (input('> '))

        if opcion == '1' or opcion == '2' or opcion == '3' :
            cantidad = float(input('Ingrese la cantidad a recargar: '))
            celular = input('Ingrese el numero de celular: ')
            if cantidad <= value[3] :
                opcion1 = input('\n' + '¿Estas seguro?  ').upper()
                if opcion1 == 'SI' :
                    print('\n' + 'RECARGA EXITOSA!')
                    print('Celular : ' + celular)
                    print('Saldo recargado : ', cantidad)
                    saldo = value[3] - cantidad
                    value[3] = round(saldo,2)
                    diccionario[key] = value
                    a+=1
                else:
                    a=0
            else :
                print('\n' + '> NO CUENTA CON SUFICIENTE DINERO')
                a=0
        else :
            print('\n' + 'OPCIÓN INVÁLIDA' + '\n')
            a=0

def cambiar_nip(diccionario) :

    key = verificar_usuario(diccionario)
    value = list(diccionario[key])

    for keys,values in diccionario.items() :
        if value == values :
            print('\n' + 'Bienvenido', value[0] + ' ' + value[1])
            print('SU NIP ES ', keys[1])
            key = keys
            break

    celular = key[0]

    a=0
    while a==0 :

        nip = input('Digite su nuevo NIP (4 Digitos) : ')
        opcion= input('\n' + '¿Es correcto su nuevo NIP?  ').upper()

        if opcion == 'SI' :
            print('\n' + 'NIP modificado correctamente!')
            del diccionario[key]
            new_key = (celular,nip)
            diccionario[new_key] = value
            a+=1
        else :
            a=0