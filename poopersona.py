class Persona:
    # Propiedades
    def __init__(self, nombre, estado_salud, estatura, peso, genero, color_cabello, etnia=True):
        self.nombre = nombre
        self.estado_salud = estado_salud
        self.estatura = estatura
        self.peso = peso
        self.genero = genero
        self.color_cabello = color_cabello
        self.etnia = etnia

    # Métodos
    def comer(self):
        print("La persona está saboreando su comida")

    def correr(self):
        print("La persona corre rapido")

    def entrenar(self):
        print("La persona entrena con fuerza")

    def trabajar(self):
        print("La persona se levanta temprano para ir a trabajar")

    def jugar(self):
        print("La persona juega futbol los sabados")

    def cantar(self):
        print("La persona canta muy bien")

    # Método para mostrar todos los datos
    def mostrar_info(self):
        print("=== Información de la Persona ===")
        print(f"Nombre: {self.nombre}")
        print(f"Estado Salud: {self.estado_salud}")
        print(f"Estatura: {self.estatura} cm")
        print(f"Peso: {self.peso} kg")
        print(f"Genero: {self.genero}")
        print(f"Color de Cabello: {self.color_cabello}")
        print(f"Etnia: {self.etnia}")
        print("==============================")


# Crear un objeto (instancia) de Animal
Emilio = Persona(
    nombre= "Emilio",
    estado_salud="Saludable",
    estatura="178",
    peso=66,
    genero="Masculino",
    color_cabello="Castaño",
    etnia="Mestizo"
)

# Usar sus métodos
Emilio.mostrar_info()
Emilio.comer()
Emilio.correr()
Emilio.entrenar()
Emilio.jugar()
Emilio.trabajar()
Emilio.cantar()