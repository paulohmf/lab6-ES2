import unittest
import numpy as np
from quadrado import Quadrado
from circulo import Circulo

class TestQuadrado(unittest.TestCase):

  def test_criar_quadrado(self):
    q = Quadrado()
    self.assertEqual(1, q.get_lado())
    
    q = Quadrado(3)
    self.assertEqual(3, q.get_lado())

  def test_mudar_lado(self):
    q = Quadrado()

    q.mudar_lado(2)
    self.assertEqual(2, q.get_lado())

    q.mudar_lado(3)
    self.assertEqual(3, q.get_lado())

  def test_calcular_area_quadrado(self):
    q = Quadrado()
    self.assertEqual(1, q.test_calcular_area_quadrado())
    
    q = Quadrado(2)
    self.assertEqual(4, q.test_calcular_area_quadrado())

  def test_calcular_perimetro_quadrado(self):
    q = Quadrado()
    self.assertEqual(4, q.test_calcular_perimetro_quadrado())
    
    q = Quadrado(2)
    self.assertEqual(8, q.test_calcular_perimetro_quadrado())

  def test_somar_areas(self):
    q1 = Quadrado()
    q2 = Quadrado()
    self.assertEqual(2, q1.somar_areas(q2))
    
    q1 = Quadrado(1)
    q2 = Quadrado(2)
    self.assertEqual(5, q1.somar_areas(q2))


class TestCirculo(unittest.TestCase):

  def test_criar_circulo(self):
    c = Circulo()
    self.assertEqual(1, c.get_raio())
    
    c = Circulo(3)
    self.assertEqual(3, q.get_raio())

  def test_mudar_raio(self):
    c = Circulo()

    c.mudar_raio(2)
    self.assertEqual(2, c.get_raio())

    c.mudar_lado(3)
    self.assertEqual(3, c.get_raio())

  def calcular_diametro(self):
    c = Circulo()
    self.assertEqual(2, c.calcular_diametro())

    c = Circulo(2)
    self.assertEqual(4, c.calcular_diametro())

  def test_calcular_area_circulo(self):
    c = Circulo()
    self.assertEqual(np.pi, c.test_calcular_area_circulo())
    
    c = Circulo(2)
    self.assertEqual(4*np.pi, c.test_calcular_area_circulo())

  def test_calcular_perimetro_circulo(self):
    c = Circulo()
    self.assertEqual(2*np.pi, q.test_calcular_perimetro_circulo())
    
    c = Circulo(2)
    self.assertEqual(4*np.pi, q.test_calcular_perimetro_circulo())
