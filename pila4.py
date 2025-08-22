pilaFia = []

# Push: agregar los primeros 15 números consecutivos
for i in range(1, 16):
    pilaFia.append(i)

print("Pila después del push:", pilaFia)

# Pop: eliminar el último elemento (como en una pila)
pilaFia.pop()

print("Pila después del pop:", pilaFia)
