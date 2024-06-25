class Aluno:
    alunos = []
 
    def __init__ (self, nome, turma, categoria):
        self._nome = nome
        self._turma = turma
        self._categoria = categoria
 
        #criar un listado de notas
        self._notas = []
        Aluno.alunos.append(self)
 
    def __str__(self):
        return f'{self._nome} | {self._turma} | {self._categoria}'
   
    @classmethod
    def listar_alunos(cls):
        print(f"{'nome do aluno'.ljust(25)} | {'turma'.ljust(25)} | {'categoria'.ljust(25)} | {'nota'.ljust(25)}")
        for aluno in cls.alunos:
            print(f'{aluno._nome.ljust(25)} | {aluno._turma.ljust(25)} | {aluno._categoria.ljust(25)} ')
   
    def __str__ (self):
        notas_str='\n'.join(str(nota) for nota in self._notas)
        return f'Aluno:{self._nome} | Turma: {self._turma} | Categotia: {self._categoria} | Notas:\n{notas_str}'


        