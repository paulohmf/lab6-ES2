import numpy as np

class Circulo:
    def __init__(self, raio=1):
      self.raio = raio

    def mudar_raio(self, novo_raio):
      self.raio = novo_raio

    def calcular_area_circulo(self):
      return np.pi * self.raio * self.raio

    def calcular_perimetro_circulo(self):
      return np.pi * self.raio * 2

    def calcular_diametro(self):
      return self.raio * 2

    def get_raio(self):
      return self.raio
