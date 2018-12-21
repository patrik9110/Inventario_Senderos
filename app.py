import numpy as np

def inicio():
    print("Bienvenido/a")

accion = input("Que queres hacer? \n[C]ompra \n[V]enta \n[E]ditar \n.. ")


iItem, iCantidad, iPrecioVenta = np.loadtxt("inventario.csv", delimiter = ",", unpack = True, dtype = "str")
vItem, vCantidadVendida, vTotalSS  = np.loadtxt("ventas.csv", delimiter = ",", unpack = True, dtype = "str")

def agregarItem():
    itemNuevo = input("Item Nuevo: ")
    for itemChecker in iItem:
        if itemChecker == itemNuevo:
            print(itemChecker + " ya esta en el inventario, que desea hacer: ")
            accion2 = input("[R]enombrar \n[A]gregar mas unidades de " + itemChecker + "\n[Ca]ncelar \n.. ")
            if accion2.upper() == "R":
                agregarItem()
            elif accion2.upper() == "A":
                masUnidades = input("Cuantas nuevas unidades hay de " + itemChecker + "? ")
                int(iCantidad[itemChecker.index()]) + int(masUnidades)
            elif accion2.upper() == "CA":
                inicio()
        if itemChecker != itemNuevo:
            iItem.append(itemNuevo)
            cantidadNueva = input("Cuantas unidades? ")
            int(iCantidad[itemNuevo.index()]) + int(cantidadNueva)
            nuevoItemVentaSS = input("A cuanto se vende? ")
            iPrecioVenta[itemNuevo.index()] = nuevoItemVentaSS


inicio()

if accion.upper() == "C":
    agregarItem()
