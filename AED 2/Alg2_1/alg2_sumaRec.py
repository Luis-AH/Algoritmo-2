def Ingresar():
    return int(input("ingresa el número "))

def calcular(sum):
    if sum==0:
        return 0
    else:
        return sum+calcular(sum-1)
    

sum=Ingresar()
res=calcular(sum)
print()
print(res)