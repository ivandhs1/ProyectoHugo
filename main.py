from controladores import controladorRegistro, controladorBusqueda

opcion=int(0)
while opcion!=5:

    print(' ')
    print('         MENU        ')
    print('  Que Desea Realizar?')
    print('  1.Crear Cliente')
    print('  2.Buscar Cliente')
    print('  3.Modificar Cliente')
    print('  4.Anexar Saldo al Cliente')
    print('  5. Salir')
    opcion=int(input('  Ingrese la Opcion'))

    if opcion==1:
        
        try:
            print(' ')
            print('  SE REGISTRARA UN CLIENTE  ')
            documento=input(' Ingrese el documento del Cliente: ')
            nombre=input(' ingrese el nombre del Cliente: ')
            movil=input(' ingrese el Numero de Movil del Cliente: ')
            saldo=int(input(' ingrese el saldo Principal: '))
            
            registro=controladorRegistro.RegistrarCliente(documento, nombre, movil, saldo)
            print('se ha registrado correctamente')
        except Exception as Ex:
            print ('ha ocurrido un error, verifique los datos')
        
    elif opcion==2:
        try:
            print(' ')
            print('  SE BUSCARA UN CLIENTE  ')
            documento=input(' Ingrese el documento del Cliente: ')
            
            busqueda=controladorBusqueda.BuscarCliente(documento)

            if len(busqueda)!=0:
                print("  El cliente buscado es: \n")
                print("Documento | Nombre | Movil | Saldo")
                print(busqueda[0])
            else:
                print("  Cliente no encontrado.")
        except Exception as Ex:
            print ('ha ocurrido un error, verifique los datos')
    elif opcion==3:
        pass
    elif opcion==4:
        pass