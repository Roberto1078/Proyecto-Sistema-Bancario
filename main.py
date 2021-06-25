from funciones import registar_usuario,depositar_dinero,verificar_saldo,transferir_dinero,recarga_tiempo_aire,cambiar_nip
from pprint import pformat

diccionario = dict()

while True :
    print('\n')
    print('1. Registrar nuevo usuario')
    print('2. Depositar dinero a cuenta propia')
    print('3. Verificar Saldo')
    print('4. Transferir dinero a otra cuenta')
    print('5. Recargar tiempo aire')
    print('6. Cambiar NIP')
    print('0. Salir')
    opcion = (input('> '))

    if opcion== '1' :
        registar_usuario(diccionario) 
    elif opcion== '2' :
        depositar_dinero(diccionario)
    elif opcion== '3' :
        verificar_saldo(diccionario)
    elif opcion== '4' :
        transferir_dinero(diccionario)
    elif opcion== '5' :
        recarga_tiempo_aire(diccionario)
    elif opcion== '6' :
        cambiar_nip(diccionario)
    elif opcion== '0' :
        print('Que tengas un excelente dia!!!')
        break
    else :
        print('\n' + 'OPCIÓN INVÁLIDA')