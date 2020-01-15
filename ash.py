def rot13(palabra):
    Cifrado = ''
    for i in palabra:
        buff = ord(i)
        if (buff >= 65 and buff <= 90) or (buff >= 97 and buff <= 122):
            if ((buff + 13 > 90 and buff + 13 <= 103) or (buff + 13 > 122 and buff + 13 <= 135)):
                Cifrado += chr(buff -13)
            else:
                Cifrado += chr(buff + 13)
    print (Cifrado)
    
def atbash(palabra):
    V1 = "abcdefghijklm"
    V2 = "zyxwvutsrqpon"
    
    Buff = ""
    
    for i in range(len(palabra)):
        for a in range(len(V1)):
            if V1[a] == palabra[i]:
                Buff += V2[a]
            elif V2[a] == palabra[i]:
                Buff += V1[a]
    print (Buff)
 
atbash(input("Ingresa tu texto a cifrar "))

#rot13(input("Ingresa tu texto a cifrar "))
 
