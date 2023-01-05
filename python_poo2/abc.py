from abc import ABC 
from collections.abc import MutableSequence
from numbers import Complex
from collections.abc import Sized

class Numero(Complex):
    pass

class Playlist(MutableSequence):
    pass



class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

lista = MinhaListagem()
print(lista)