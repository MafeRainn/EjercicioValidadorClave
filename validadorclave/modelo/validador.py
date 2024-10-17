from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self,clave:str) ->bool:
        if len(clave) > self.longitud_esperada:
            return True
    
    def _contiene_mayuscula(clave:str) ->bool:
        mayuscula_presente= False
        for caracter in clave:
            if caracter.isupper():
                mayuscula_presente=True
            return True
                
        # str.issupper(clave)

    def _contiene_minuscula(clave:str) ->bool:
        ...
        # str.islower(clave)

    def _contiene_numero(clave:str) ->bool:
        # str.isdigit(clave)
        ...

    @abstractmethod
    def es_valida(clave:str) ->bool:
        ...

class Validador:
    def __init__(self, regla:ReglaValidacion):
        ...
        
    def es_valida(clave: str) ->bool:
        ...

class ReglaValidacionGanimedes(ReglaValidacion):
    def contine_caracter_especial(clave: str) ->bool:
        if clave.__contains__('@','_','#','$', '%'):
            return True
    
    def es_valida(clave: str) -> bool:
        ...

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(clave: str) ->bool:
        if clave.__contains__('calisto'):
            ...
    
    def es_valida(clave: str) -> bool:
        ...

        