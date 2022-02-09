#!/usr/bin/python3

cantPalabras = 0
f =  open("datos.txt" , "r" )
for lienea in f:
	a = linea.strip().split()
	cantPalabras += len(a)

print(cantPalabras)
