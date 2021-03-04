from Atividade03 import Ponto
from Atividade03 import Quadrilátero
class Play:
    def P(self):
        g = Ponto(5,5)
        print(g.qualQuadrante())
        f = Quadrilátero(10,7)
        print(f.contidoEmQ(g))
a = Play()
a.P()
