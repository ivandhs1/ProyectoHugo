deudaActual=5000
deudaActual=deudaActual-10000

if deudaActual<0:
    print("menor a cero",deudaActual)
    deudaActual=deudaActual*(-1)
    print (deudaActual)
elif deudaActual>0:
    print(deudaActual)