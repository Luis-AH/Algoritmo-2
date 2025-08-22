pilaFia = []

# Push: agregar los nombres

for i in range(1, 21):
    print("\nnombre",i)
    nom=input("\nEscribe el nombre: ")
    pilaFia.append(nom)

print("Pila después del push:", pilaFia)

# Pop: eliminar el último elemento (como en una pila)
pilaFia.pop()

print("Pila después del pop:", pilaFia)
