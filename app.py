from openpyxl import load_workbook
import os

wb1 = load_workbook("INVENTARIO.xlsx")
wb2 = load_workbook("VENTAS.xlsx")
inventario = wb1["Hoja 1"]
ventas = wb2["Hoja 1"]
print(ventas["A2"].value)

''''def main():

    print("Bienvenido/a")

    accion = input("Que queres hacer? \n[C]ompra \n[V]enta \n[E]ditar \n[M]irar \n.. ")


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



    if accion.upper() == "C":
        agregarItem()

main()
'''
