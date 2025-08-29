tam=int(input("cuántos atletas participaron: "))

at=[0]*tam

def Poblar():
    for i in range (tam):
     at[i]=int(input("el tiempo que tardó (seg.): "))

def Mostrar():
   for i in range (tam):
        print(at[i],end=" ")

def OrdenarSort():
   for i in range (tam):
      mI=i
      for j in range(i+1,tam):
         if(at[i]>at[j]):
            mI=j
      aux=at[i]
      at[i]=at[mI]
      at[mI]=aux

Poblar()
print("Antes de ordenarlos\n")
Mostrar()
OrdenarSort()
print("\nDespués de ordenarlos\n")
Mostrar()
