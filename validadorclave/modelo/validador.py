from abc import ABC, abstractmethod
from errores import ValidadorError, NoCumpleLongitudMinimaError, NoTieneCaracterEspecialError,NoTieneLetraMayusculaError,NoTieneLetraMinusculaError,NoTieneNumeroError,NoTienePalabraSecretaError

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self,clave:str) ->bool:
        if len(clave) > self.longitud_esperada:
            return True
        else: False
    
    def _contiene_mayuscula(clave:str) ->bool:
        for caracter in clave:
            if caracter.isupper():  
                return True
        else:
            return False

    def _contiene_minuscula(clave:str) ->bool:
        for caracter in clave:
            if caracter.islower():
                return True
        else:
            return False

    def _contiene_numero(clave:str) ->bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        else:
            return False

    @abstractmethod
    def es_valida(clave:str) ->bool:
        pass

class Validador:
    def __init__(self, regla:ReglaValidacion):
        self.regla: ReglaValidacion = regla
        
    def es_valida(self,clave: str) ->bool:
        return self.regla.es_valida(clave)


class ReglaValidacionGanimedes(ReglaValidacion):
    def contine_caracter_especial(clave: str) ->bool:
        caracteres = ['@', '#', '_', '$', '%']

        if any(caracteres) in clave:
            return True
    
    def es_valida(clave: str) -> bool:
        ...

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(clave: str) ->bool:
        if clave.__contains__('calisto'):
            ...
    
    def es_valida(clave: str) -> bool:
        ...

        