class Quadrado:
    def __init__(self, lado=1):
      self.lado = lado

    def mudar_lado(self, novo_lado):
      self.lado = novo_lado

    def calcular_area_quadrado(self):
      return self.lado * self.lado

    def calcular_perimetro_quadrado(self):
      return self.lado * 4

    def get_lado(self):
      return self.lado

    def somar_areas(self, quadrado):
      return self.calcular_area_quadrado() + quadrado.calcular_area_quadrado()
