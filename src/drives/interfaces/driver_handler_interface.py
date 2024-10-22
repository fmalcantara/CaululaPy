from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterface(ABC):
  
  @abstractmethod
  def standart_derivation(self, numbers: List[float])-> float:
    pass
  
  @abstractmethod
  def variance(self, numbers: List[float])-> float:
    pass