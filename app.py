from openpyxl import load_workbook
import os

wb1 = load_workbook("INVENTARIO.xlsx")
wb2 = load_workbook("VENTAS.xlsx")
inventario = wb1["Hoja 1"]
ventas = wb2["Hoja 1"]


def main():

    print("Bienvenido/a")

    accion = input("Que queres hacer? \n[C]ompra \n[V]enta \n[E]ditar \n[M]irar \n[S]alir \n.. ")


    def agregarItem():

        def usado():
            print(itemChecker.value + " ya esta en el inventario, que desea hacer: ")
            accion2 = input("[R]eintentar \n[A]gregar mas unidades de " + itemChecker.value + "\n[I]nicio \n[S]alir \n.. ")
            if accion2.upper() == "R":
                agregarItem()
            elif accion2.upper() == "A":
                masUnidades = input("Cuantas nuevas unidades nuevas hay de " + itemChecker.value + "? ")
                precioProducto = inventario["B"+str(rowCounter)]
                inventario["B"+str(rowCounter)] = int(masUnidades) + int(precioProducto.value)
                print("Se actualizo la cantidad de " + itemChecker.value + " a " + str(inventario["B"+str(rowCounter)].value))
                main()
            elif accion2.upper() == "I":
                main()
            elif accion2.upper() == "S":
                quit()
        def nuevo():
            colLen = 1
            for i in inventario["A"]:
                colLen += 1
            cantidadNueva = input("Cuantas unidades? ")
            inventario["A"+str(colLen)] = itemNuevo
            inventario["B"+str(colLen)] = cantidadNueva
            precioNuevo = input("A cuanto se va a vender? ")
            inventario["C"+str(colLen)] = precioNuevo
            print(itemNuevo + " agregado al inventario!")
            sigue2 = input("Algo mas para agregar al inventario? \n[Si] \n[I]nicio \n[S]alir")
            if sigue2.upper() == "SI":
                wb1.save("INVENTARIO.xlsx")
                agregarItem()
            elif sigue2.upper() == "I":
                wb1.save("INVENTARIO.xlsx")
                main()
            elif sigue2.upper() == "S":
                wb1.save("INVENTARIO.xlsx")
                quit()

        itemNuevo = input("Item Nuevo: ")
        itemChecker = " "
        for itemChecker in inventario["A"]:
            rowCounter = 1
            if itemChecker.value == itemNuevo:
                usado()
            if itemChecker != itemNuevo:
                nuevo()
            rowCounter += 1


    if accion.upper() == "C":
        agregarItem()

    if accion.upper() == "S":
        quit()

main()

wb1.save("INVENTARIO.xlsx")
wb2.save("VENTAS.xlsx")
