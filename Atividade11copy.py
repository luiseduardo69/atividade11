from Atividade03 import Ponto
from Atividade03 import Quadrilátero
class Play:
    def P(self):
        g = Ponto(5,5)
        #definir ponto no plano
        print(g.qualQuadrante())
        f = Quadrilátero(10,7)
        #definir tamanho do quadrilátero
        print(f.contidoEmQ(g))

a = Play()
a.P()