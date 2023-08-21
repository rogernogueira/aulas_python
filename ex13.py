import math

class Circulo():
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        area = math.pi*self.raio **2
        return area 
     
    def calcular_circurencia(self):
         circunferencia  = 2 * math.pi * self.raio
         return circunferencia

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura

    def calcular_volume(self):
        volume = (math.pi * self.raio **2)*self.altura
        return volume
cilindro_1  = Cilindro(15, 7)

# print(cilindro_1.calcular_area())
# print(cilindro_1.calcular_circurencia())
# print(cilindro_1.calcular_volume())

circulo1 = Circulo(10)
print(circulo1.calcular_area())
print(circulo1.calcular_circurencia())

        