from openpyxl import load_workbook
import os

wb1 = load_workbook("INVENTARIO.xlsx")
wb2 = load_workbook("VENTAS.xlsx")
inventario = wb1["Hoja 1"]
ventas = wb2["Hoja 1"]
'''row = ""
c = 0

for row in ventas["A"]:
    c += 1

print(row.value)
print(ventas["B"+str(c)].value)'''



def main():

    print("Bienvenido/a")

    accion = input("Que queres hacer? \n[C]ompra \n[V]enta \n[E]ditar \n[M]irar \n.. ")


    def agregarItem():
        itemNuevo = input("Item Nuevo: ")
        for itemChecker in inventario["A"]:
            rowCounter = 0
            if itemChecker == itemNuevo:
                print(itemChecker + " ya esta en el inventario, que desea hacer: ")
                accion2 = input("[R]eintentar \n[A]gregar mas unidades de " + itemChecker + "\n[Ca]ncelar \n.. ")
                if accion2.upper() == "R":
                    agregarItem()
                elif accion2.upper() == "A":
                    masUnidades = input("Cuantas nuevas unidades hay de " + itemChecker + "? ")
                    inventario["B"+str(rowCounter)] = str(int(masUnidades) + int(inventario["B"+str(rowCounter)]))
                    print("Se actualizo la cantidad de " + itemChecker + " a " + inventario["B"+str(rowCounter)])
                elif accion2.upper() == "CA":
                    main()
            if itemChecker != itemNuevo:
                colLen = 1
                for i in inventario["A"]:
                    colLen += 1
                cantidadNueva = input("Cuantas unidades? ")
                inventario["A"+str(colLen)] = itemNuevo
                inventario["B"+str(colLen)] = cantidadNueva
                precioNuevo = input("A cuanto se va a vender? ")
                inventario["C"+str(colLen)] = precioNuevo
                print(itemNuevo + " agregado al inventario!")
            rowCounter += 1


    if accion.upper() == "C":
        agregarItem()

main()

wb1.save("INVENTARIO.xlsx")
wb2.save("VENTAS.xlsx")
