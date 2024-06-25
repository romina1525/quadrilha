from modelos.nota import Nota
 
class Jurado:
    def __init__(self, nome, area):
        self._nome = nome
        self._area = area
    def __str__(self):
        return f'Jurado: {self._nome}, Area: {self._area}'
   
    def atribuir_nota(self, aluno, elegancia, desemvoltura, simpatia, reutilizacao):
        avaliacao = Nota(elegancia, desemvoltura, simpatia, reutilizacao)
   
        aluno._notas.append(avaliacao)