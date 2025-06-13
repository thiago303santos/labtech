class MarsRover:
    def __init__(self):
        self.x, self.y, self.direcao = 0,0, "N"
        self.direcoes = ["N", "E", "S", "W"]

    def execute(self,comandos):
        for comando in comandos:
         if comando == "R":
             idx = self.direcoes.index(self.direcao)
             self.direcao = self.direcoes[(idx+1) % 4]
         elif comando == "L":
             idx = self.direcoes.index(self.direcao)
             self.direcao = self.direcoes[(idx-1) % 4]
         elif comando == "M" and self.direcao == "N":
            self.y = (self.y + 1) % 10
        return f"{self.x}:{self.y}:{self.direcao}"