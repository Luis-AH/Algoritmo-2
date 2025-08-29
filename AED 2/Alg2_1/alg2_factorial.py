def Ingresar():
    return int(input("ingresa el factorial: "))

def calcular(fac):
    if fac==0 or fac==1:
        return 1
    else:
        return fac*calcular(fac-1)
    

fac=Ingresar()
res=calcular(fac)
print()
print(res)