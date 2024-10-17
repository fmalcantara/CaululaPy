from src.calculators.calculator_2 import Calculator2
from src.drives.numpy_handler import NumpyHandler

def calculator2_factory():
  numpy_handler = NumpyHandler()
  calc = Calculator2(numpy_handler)
  return calc