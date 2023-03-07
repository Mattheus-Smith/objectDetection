class Jogador:
    def __init__(self, canvas, diametro, color, x_values, y_values, contador, status, posicao_x, posicao_y, breakCont, id , x, y):
        self.canvas = canvas
        self.jogador = canvas.create_oval(0, 0, diametro, diametro, fill=color)
        self.x_values = x_values
        self.y_values = y_values
        self.contador = contador
        self.status = status
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.breakCont = breakCont
        self.id = id
        self.x = x
        self.y = y

    def move(self):
        #xb, yb, xs, ys = self.canvas.coords(self.jogador)
        teste = self.canvas.coords(self.jogador)
        print(teste)

    def left(self):
        self.x = -1

    def right(self):
        self.x = 1

    def up(self):
        self.y = 1

    def down(self):
        self.y = -1

    def definirStatus(self):

        if (self.posicao_x == 0 and self.posicao_y == 0):
            self.status = 0

        elif (self.posicao_x != 0 and self.posicao_y == 0):
            if (self.posicao_x > 0):
                self.status = 1  # direita
            else:
                self.status = 2  # esquerda

        elif (self.posicao_x == 0 and self.posicao_y != 0):
            if (self.posicao_y > 0):
                self.status = 3  # cima
            else:
                self.status = 4  # baixo

        elif (self.posicao_x != 0 and self.posicao_y != 0):
            if (self.posicao_x > 0 and self.posicao_y > 0):
                self.status = 5  # direita and cima
            elif (self.posicao_x < 0 and self.posicao_y > 0):
                self.status = 6  # esquerda and cima
            elif (self.posicao_x < 0 and self.posicao_y < 0):
                self.status = 7  # esquerda and baixo
            elif (self.posicao_x > 0 and self.posicao_y < 0):
                self.status = 8  # direita and baixo