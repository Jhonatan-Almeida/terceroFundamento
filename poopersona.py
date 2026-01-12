class Persona: 
    # Propiedades
    def __init__(self, colorpiel, estatura, peso, contestura, discapacidad=True):
        self.colorpiel = colorpiel
        self.estatura = estatura
        self.peso = peso
        self.contestura = contestura
        self.discapacidad = discapacidad

    # Métodos
    def desplazarse(self, velocidad=10):
        print("La persona se está desplazando a una velocidad de ", velocidad, "km/h.")

    def masticar(self):
        print("La persona mastica su comida.")  
   
    def respirar(self):
        print("La persona está respirando.")
    
    def parpadear(self):
        print("La persona parpadea para proteger y humedecer sus ojos.")

    # Método para mostrar todos los datos
    def mostrar_info(self):
        print("=== Información de la persona ===")
        print(f"Color de piel: {self.colorpiel}")
        print(f"Estatura: {self.estatura} m")
        print(f"Peso: {self.peso} kg")
        print(f"Contextura: {self.contestura}")
        print(f"¿Tiene discapacidad?: {self.discapacidad}")
        print("===============================")
       

# Crear un objeto (instancia) de Animal
Carlos = Persona(
    colorpiel="Blanca",
    estatura="1.85",
    peso=100,
    contestura="Fuerte",
    discapacidad=True
)

# Usar sus métodos
Carlos.mostrar_info()
Carlos.desplazarse(80)
Carlos.masticar()
Carlos.respirar()
Carlos.parpadear()
