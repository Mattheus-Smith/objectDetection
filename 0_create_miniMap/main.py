import pandas as pd
from tkinter import *
from Jogador import *

df1 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\novos\\GPS 01_Jogo 01-t.xlsx")
df2 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\novos\\GPS 02_Elias-t.xlsx")
df3 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\novos\\GPS 02_Jogador 2-t.xlsx")
df4 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\novos\\GPS 04_Joao Diego-t.xlsx")

# df1 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe A_Gps1.xlsx")
# df2 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe A_Gps2.xlsx")
# df3 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe A_Gps3.xlsx")
# df4 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe A_Gps7.xlsx")
#
# df5 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe B_Gps4.xlsx")
# df6 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe B_Gps5.xlsx")
# df7 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe B_Gps6.xlsx")
# df8 = pd.read_excel("C:\\Users\\Smith Fernandes\\OneDrive\\3 - PIBIC\\datas\\Jogo1_Equipe B_Gps8.xlsx")

bancosDados = [df1,df3]

x_campo = 1010
y_campo = 510

class Window:

    def __init__(self):
        self.tela = Tk()
        self.tela.title('MiniMapa dos Jogadores')

        self.tela.geometry('1100x600')
        self.tela.resizable(False, False)

        self.canvas = Canvas(self.tela, width=1010, height=510, bg='black')

        self.jogadores = []
        print("Criando os Jogadores!")
        for n in range(0,len(bancosDados)):
        #def __init__(self, canvas, diametro, color, x_values, y_values, contador, status, posicao_x, posicao_y,breakCont, id,x,y):
            if ( n == 0 ):
                self.jogadores.append(Jogador(self.canvas, 10, "blue", [], [], 0, 0, 0, 0, 0, n, 0, 0))
            else:
                self.jogadores.append(Jogador(self.canvas, 10, "red" , [], [], 0, 0, 0, 0, 0, n, 0, 0))
        self.canvas.pack()

    def inicializarLoop(self):
        print("Iniciando o Loop!")
        self.tela.after(0, self.atualiza_posicao_bola)  # agendamento inicial

        sair = Button(self.tela, text='Sair', bg='red', command=self.tela.destroy)
        sair.pack()

        pause = Button(self.tela, text='Pause', bg='red', command=self.tela.destroy)
        pause.pack(side='left')

        play = Button(self.tela, text='Play', bg='red', command=self.tela.destroy)
        play.pack(side='left')

        self.tela.mainloop()

    def inicializarJogadoresNoMiniMapa(self):
        print("Inicializando os Jogados em Campo!")
        for n in range(0, len(self.jogadores)):
            self.jogadores[n].x = int(self.jogadores[n].x_values[self.jogadores[n].contador])
            self.jogadores[n].y = int(self.jogadores[n].y_values[self.jogadores[n].contador])

            self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y);
            self.canvas.move(self.jogadores[n].jogador, 0, 0);

    def atualiza_posicao_bola(self):

        for n in range (0, len(self.jogadores)):
            # print(tam," == ", contador)
            if ( len(self.jogadores[n].x_values) == self.jogadores[n].contador + 1 ):
                self.jogadores[n].breakCont = 1

            if (self.jogadores[n].status == 0):
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                self.jogadores[n].contador = self.jogadores[n].contador + 1
                self.jogadores[n].posicao_x = int(self.jogadores[n].x_values[self.jogadores[n].contador] - self.jogadores[n].x_values[self.jogadores[n].contador - 1])
                self.jogadores[n].posicao_y = int(self.jogadores[n].y_values[self.jogadores[n].contador] - self.jogadores[n].y_values[self.jogadores[n].contador - 1])
                self.jogadores[n].definirStatus()
                #print("Xa:", xb, "- Ya:", ys - 10, " ||  Xd:", int(self.jogadores[n].x_values[self.jogadores[n].contador]),"- Yd:", int(self.jogadores[n].y_values[self.jogadores[n].contador]), "status: ", self.jogadores[n].status)

            elif (self.jogadores[n].status == 1):  # direita
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x - 1
                self.jogadores[n].right()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, 0)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 1 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 2):  # esquerda
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x + 1
                self.jogadores[n].left()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, 0)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 2 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 3):  # cima
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y - 1
                self.jogadores[n].up()
                self.canvas.move(self.jogadores[n].jogador, 0, self.jogadores[n].y)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 3 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 4):  # baixo
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y + 1
                self.jogadores[n].down()
                self.canvas.move(self.jogadores[n].jogador, 0, self.jogadores[n].y)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 4 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 5):  # direita and cima
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x - 1
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y - 1
                self.jogadores[n].up()
                self.jogadores[n].right()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                #print("status 5 - x: ",xb ," y: ",ys-10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 6):  # esquerda and cima
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x + 1
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y - 1
                self.jogadores[n].up()
                self.jogadores[n].left()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 6 - x: ",xb ," y: ",ys-10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 7):  # esquerda and baixo
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x + 1
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y + 1
                # print("Px: ", posicao_x," - Py: ", posicao_y)
                self.jogadores[n].down()
                self.jogadores[n].left()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 7 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 8):  # direita and baixo
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x - 1
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y + 1
                self.jogadores[n].down()
                self.jogadores[n].right()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y)
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 8 - x: ",xb ," y: ",ys-10)
                self.jogadores[n].definirStatus()

            if (self.jogadores[n].breakCont == 1 and self.jogadores[n].status == 0):
                print("estorou tamanho")
                self.canvas.move(self.jogadores[n].jogador, 0, 0)

            else:
                if( n == len(self.jogadores)-1 ):
                    self.tela.after(5, self.atualiza_posicao_bola)  # agenda pra daqui a pouco


def achandoValoresXeY(jogadores,BD):
    print("Processando os Dados!")

    for k in range(0, len(BD)):
        # _, maxLat, maxLog, _, _, _ = BD[k].max()
        # _, minLat, minLog, _, _, _ = BD[k].min()

        _, maxLat, maxLog = BD[k].max()
        _, minLat, minLog = BD[k].min()

        dfiLat = maxLat - minLat
        dfiLog = maxLog - minLog

        # print("max - ",maxLat,maxLog)
        # print("min - ",minLat,minLog)

        for n in range(0, len(BD[k])):
            jogadores[k].x_values.append(((BD[k].get(BD[k].columns[1])[n] - minLat) / dfiLat) * x_campo)
            jogadores[k].y_values.append(((BD[k].get(BD[k].columns[2])[n] - minLog) / dfiLog) * y_campo)

        # print(df)
        # print(x_values)
        # print(y_values)
        # print("===================================")


tela = Window()
achandoValoresXeY(tela.jogadores,bancosDados)
tela.inicializarJogadoresNoMiniMapa()
tela.inicializarLoop()

# def atualizarValoresY():
#     for n in range(0, len(tela.jogadores[id].y_values)):
#         tela.jogadores[id].y_values[n] = y_campo - tela.jogadores[id].y_values[n]
#
# # atualizarValoresY()
#
#
# def miniMapa():
#
#
#     canvas.move(jogadores[0].jogador, jogadores[0].x, jogadores[0].y);canvas.move(jogadores[0].jogador, 0, 0);
#     tela.after(0, atualiza_posicao_bola)  # agendamento inicial
#
#     sair = Button(tela, text='Sair', bg='red', command=tela.destroy)
#     sair.pack()
#     tela.mainloop()
#
# miniMapa()
