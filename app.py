from modelos.aluno import Aluno
from modelos.jurado import Jurado
 
def main():
 
      aluno_paulo = Aluno('paulo', 'sala2', 'mister')
      aluno_laura = Aluno('laura', 'sala1', 'miss')
      aluno_joao = Aluno('joao', 'sala3', 'mister')
      aluno_maria = Aluno('maria', 'sala2', 'miss')
 
      jurado = Jurado('miranda', 'computacao')
      jurado = Jurado('lopez', 'secretaria')
      jurado = Jurado('silva', 'literatura')
 
      jurado.atribuir_nota(aluno_paulo, 4, 7, 5, 9)
      jurado.atribuir_nota(aluno_paulo, 6, 5, 7, 6)
      jurado.atribuir_nota(aluno_paulo, 6, 6, 6, 6)
 
      jurado.atribuir_nota(aluno_laura, 6, 5, 7, 5)
      jurado.atribuir_nota(aluno_laura, 7, 5, 7, 7)
      jurado.atribuir_nota(aluno_laura, 6, 6, 7, 5)
 
      jurado.atribuir_nota(aluno_joao, 4, 6, 6, 7)
      jurado.atribuir_nota(aluno_joao, 6, 6, 5, 7)
      jurado.atribuir_nota(aluno_joao, 7, 6, 6, 7)
 
      jurado.atribuir_nota(aluno_maria, 6, 7, 6, 6)
      jurado.atribuir_nota(aluno_maria, 5, 7, 5, 6)
      jurado.atribuir_nota(aluno_maria, 7, 7, 7, 6)
 
 
 
      print(aluno_paulo)
      print(aluno_laura)
      print(aluno_joao)
      print(aluno_maria)
 
 
if __name__ == '__main__':
    main()