

from __future__ import annotations
from typing import List


class Pessoa:
    olhos = 2

    def __init__(self, *filhos: Pessoa, nome: str = None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self) -> str:
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls.olhos} - olhos'


class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    robson = Mutante(nome='Robson')
    luciano = Homem(robson, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)

    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho'

    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(robson.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(robson.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(robson.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_class(), luciano.nome_e_atributos_de_class())
    pessoa = Pessoa('Anomimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(robson, Pessoa))
    print(isinstance(robson, Pessoa))
    print(robson.olhos)