class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente

    def esta_vacia(self):
        return self.frente == -1

    def encolar(self, elemento):
        if self.esta_llena():
            print("⚠️ La cola está llena.")
            return
        if self.esta_vacia():
            self.frente = 0
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = elemento
        print(f"✅ Elemento '{elemento}' encolado.")

    def desencolar(self):
        if self.esta_vacia():
            print("⚠️ La cola está vacía.")
            return None
        elemento = self.cola[self.frente]
        if self.frente == self.final:
            self.frente = self.final = -1  # Cola vacía
        else:
            self.frente = (self.frente + 1) % self.capacidad
        print(f"🔄 Elemento '{elemento}' desencolado.")
        return elemento

    def mostrar(self):
        if self.esta_vacia():
            print("⚠️ La cola está vacía.")
            return
        print("📦 Elementos en la cola circular:")
        i = self.frente
        while True:
            print(self.cola[i], end=" ")
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        print()

cola = ColaCircular(5)
cola.encolar(10)
cola.encolar(20)
cola.encolar(30)
cola.mostrar()
cola.desencolar()
cola.mostrar()
cola.encolar(40)
cola.encolar(50)
cola.encolar(60) # Aquí debería estar llena
cola.encolar(61)
cola.desencolar()
cola.encolar(15)

cola.mostrar()
