class Nota:
    notas = []
    def __init__(self, elegancia, desemvoltura, simpatia, reutilizacao):
        self._elegancia = elegancia
        self._desemvoltura = desemvoltura
        self._simpatia = simpatia
        self._reutilizacao = reutilizacao
    def calcular_media():
        pass
   
    def __str__(self):
        return f'elegancia: {self._elegancia} | desemvoltura: {self._desemvoltura} | simpatia: {self._simpatia} | Reutilizacao: {self._reutilizacao}'