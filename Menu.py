from VALID import ns, OKI
import subprocess

while True:
    texto=input("Tu texto: ")

    abc="ABCDEFGHIJKLMNQOPQRSTUVWXYZabcdefghijklmnopqrstuwxyz" 

    k=OKI(input("Valor de desplazamiento: "))
    cifrad=""
    
    for c in texto:
        if c in abc:
            cifrad += abc[(abc.index(c)+k)%(len(abc))]
        else:
            cifrad+=c

    print("Texto cifrado: ",cifrad)
    conti=ns(input("¿Desea acontinuar?: "))
    if conti==("n"):
        break
    #subprocess.call(["cmd.exe","/C","cls"])
