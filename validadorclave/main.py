from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(clave:str) ->bool:
        ...
    
    def _contiene_mayuscula(clave:str) ->bool:
        ...

    def _contiene_minuscula(clave:str) ->bool:
        ...

    def _contiene_numero(clave:str) ->bool:
        ...

    @abstractmethod
    def es_valida(clave:str) ->bool:
        ...

class Validador(ABC):
    def __init__(self, regla:ReglaValidacion):
        ...
        
    @abstractmethod
    def es_valida(clave: str) ->bool:
        ...

class ReglaValidacionGanimedes(ReglaValidacion):
    def contine_caracter_especial(clave: str) ->bool:
        ...
    
    def es_valida(clave: str) -> bool:
        ...

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(clave: str) ->bool:
        ...
    
    def es_valida(clave: str) -> bool:
        ...

        