class persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

    def __str__(self):
        return f'Persona: {self.nombre} {self.apellido} {self.edad}'

a1 = persona('Juan', 'Perez', 28)
print(a1)