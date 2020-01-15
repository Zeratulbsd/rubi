#!/usr/bin/python
import os
print("Menu segunda oportunidad  Unidad 1")
print ("materia:Seguridad informatica")
print("Docente: Juan Monrroy")
print("Alumna:Rubi guadalupe serapio herrejon")
aver =0
while aver != 6 and aver <7:
   print("1 vigenere")
   print("2 transposicion")
   print("3 rot13")
   print("4 cesar")
   print("5 atash")
   print("6 salir")
   aver=int(input("Ingresa tu opcion "))
   if aver == 1:  
       os.system("python vigenere.py")
   if aver == 2:  
       os.system("transposicion.py")
   if aver == 3:  
      os.system("python rot13.py")

   if aver == 4:  
       os.system("python Menu.py")
   if aver == 5:  
       os.system("python ash.py")
   
