from controladores import controladorRegistro, controladorBusqueda, controladorActualizar, controladorSaldo

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
    opcion=int(input('  Ingrese la Opcion '))

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
        
        try:
            
            print(' ')
            print('   SE MODIFICARA UN CLIENTE  ')
            documento=input(' ingrese el documento del cliente: ')
            
            busqueda=controladorBusqueda.BuscarCliente(documento)

            if len(busqueda)!=0:
                print("  El cliente que Modificara es: \n")
                print("Documento | Nombre | Movil | Saldo")
                print(busqueda[0])
                
                print(' Que desea modificar?:')
                print(' 1. Nombre')
                print(' 2. Movil')
                opcion=int(input(' DIGITE SU OPCION:  '))
                
                if opcion==1:
                    print(' ')
                    nombre=input('  Ingrese el nuevo Nombre:')
                    actualizar=controladorActualizar.ActualizarNombre(documento,nombre)
                    print(' Se ha actualizado correctamente ')
                    
                elif opcion==2:
                    print(' ')
                    movil=input(' Ingrese el nuevo movil del Cliente: ')
                    actualiza=controladorActualizar.ActualizaMovil(documento,movil)
                    print(' Se ha actualizado correctamente ')
                                
            else:
                print("  Cliente no encontrado.")
            
            
        except Exception as Ex:
            pass
        
    elif opcion==4:
        try:
            print(' ')
            print('  AGREGAR SALDO  ')
            documento=input(' Ingrese el documento del Cliente: ')
            
            busqueda=controladorBusqueda.BuscarCliente(documento)

            if len(busqueda)!=0:
                print("  El saldo del cliente ingresado es: \n")
                print("Nombre | Saldo")
                saldo = busqueda[0][3]
                print(busqueda[0][1]," | ",saldo)
                print("")
                print("  MENU SALDO  ")
                print(" 1. Agregar abono al saldo pendiente.")
                print(" 2. Agregar saldo pendiente.")
                print(" 3. Salir.")
                eleccion = int(input(" ¿Que desea hacer?  "))
                if eleccion == 1:
                    ingreso = int(input(' Ingrese el abono al saldo del Cliente: '))
                    if ingreso> saldo:
                        print("  No puede abonar mas dinero del que debe, debe: $", saldo, " e ingreso: $", ingreso)
                    else:
                        saldoNuevo=saldo-ingreso
                        controladorSaldo.CambiarDeuda(documento,saldoNuevo)

                        busqueda=controladorBusqueda.BuscarCliente(documento)
                    print("\n La deuda del cliente queda en: ", busqueda[0][3])
                elif eleccion == 2:
                    ingreso = int(input(' Ingrese la nueva deuda del Cliente: '))
                    saldoNuevo=saldo+ingreso
                    controladorSaldo.CambiarDeuda(documento,saldoNuevo)
                    busqueda=controladorBusqueda.BuscarCliente(documento)
                    print("\n La deuda del cliente queda en: ", busqueda[0][3])
                else:
                    print("  Opcion desconocida.")
            else:
                print("  Cliente no encontrado.")
        except Exception as Ex:
            print ('ha ocurrido un error, verifique los datos')