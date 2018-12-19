import numpy as np

def main():
    items, cantidad, preciov = np.loadtxt('inventario.csv', delimiter = ',', unpack = True, dtype = 'str') #saco la info

    print(items[1], cantidad[1], preciov[1]) #Printeo la info

main()
