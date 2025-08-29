#cuenta regresiva sin mostrar el 0

n=6
def contar(n):
    if n==0:
        return
    else:
        print(n)
        contar(n-1)

def contarA(i,n):
    if i>n:
        return
    else:
        print(i)
        contarA(i+1,n)

contar(n)

#cuenta ascendente de 1 al numero 
print()
print()
print()

contarA(1,n)
