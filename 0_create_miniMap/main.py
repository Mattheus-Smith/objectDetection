import pandas as pd
from tkinter import *
from Jogador import *

df1 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 1_Wildes_Equipe 1.xlsx")
df2 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 2_Alvaro_Equipe 1.xlsx")
df3 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 3_Cristiano_Equipe 1.xlsx")

df4 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 4_Alan_Equipe 2.xlsx")
df5 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 5_Flavio_Equipe 2.xlsx")
df6 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 6_Antonio_Equipe 2.xlsx")

#bancosDados = [df1,df2, df3]
bancosDados = [df4,df5, df6]

x_campo = 1010
y_campo = 510

class Window:

    def __init__(self):
        self.tela = Tk()
        self.tela.title('MiniMapa dos Jogadores')
        self.is_paused = False  # variável de controle do estado do loop
        #self.background_image = PhotoImage(file="campo_futebol.png")
        # Obter as dimensões da imagem
        #self.img_width, self.img_height = self.background_image.width(), self.background_image.height()

        self.tela.geometry('1100x600')
        self.tela.resizable(False, False)

        # Cria a janela secundária
        self.tela_info = Toplevel()
        self.tela_info.title("Janela secundária")
        self.tela_info.geometry("400x400")
        self.tela.lift()

        self.canvas = Canvas(self.tela, width=1010, height=510, bg='black')
        self.canvas.pack()

        # Redimensionar a imagem para ajustar o canvas
        #self.resized_image = self.background_image.subsample(1010, 510)
        # self.canvas.create_image(0, 0, image=self.resized_image, anchor="nw")

        self.jogadores = []
        print("Criando os Jogadores!")
        for n in range(0,len(bancosDados)):
        #def __init__(self, canvas, diametro, color, x_values, y_values, contador, status, posicao_x, posicao_y,breakCont, id,x,y):
            self.jogadores.append(Jogador(self.canvas, 10, "blue", [], [], 0, 0, 0, 0, 0, n, 0, 0))
            # if ( n == 0 ):
            #     self.jogadores.append(Jogador(self.canvas, 10, "blue", [], [], 0, 0, 0, 0, 0, n, 0, 0))
            # else:
            #     self.jogadores.append(Jogador(self.canvas, 10, "red" , [], [], 0, 0, 0, 0, 0, n, 0, 0))

    def pause(self):
        self.is_paused = True

    def play(self):
        self.is_paused = False
        self.atualiza_posicao_bola()  # retoma o loop

    def inicializarLoop(self):
        print("Iniciando o Loop!")
        self.tela.after(0, self.atualiza_posicao_bola)  # agendamento inicial

        sair = Button(self.tela, text='Sair', bg='red', command=self.tela.destroy)
        sair.pack()

        pause = Button(self.tela, text='Pause', bg='red', command=self.pause)
        pause.pack(side='left')

        play = Button(self.tela, text='Play', bg='red', command=self.play)
        play.pack(side='left')

        self.tela.mainloop()

    def conectar_jogadores(self):
        # Obtém as coordenadas atuais dos círculos
        x1, y1, x2, y2 = self.canvas.coords(self.jogadores[0].jogador)
        #print(x1, y1, x2, y2)

        # Apaga as linhas antigas
        self.canvas.delete("line")

        # Cria as novas linhas entre os círculos
        for i in range(len(self.jogadores) - 1):
            x1, y1, x2, y2 = self.canvas.coords(self.jogadores[i].jogador)
            x3, y3, x4, y4 = self.canvas.coords(self.jogadores[i + 1].jogador)
            line = self.canvas.create_line(x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2,
                                      x3 + (x4 - x3) // 2, y3 + (y4 - y3) // 2, tags="line",fill='red')
        # Cria a última linha que liga o último círculo ao primeiro
        x1, y1, x2, y2 = self.canvas.coords(self.jogadores[-1].jogador)
        x3, y3, x4, y4 = self.canvas.coords(self.jogadores[0].jogador)
        line = self.canvas.create_line(x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2,
                                  x3 + (x4 - x3) // 2, y3 + (y4 - y3) // 2, tags="line",fill='red')

    def inicializarJogadoresNoMiniMapa(self):
        print("Inicializando os Jogados em Campo!")
        for n in range(0, len(self.jogadores)):
            self.jogadores[n].x = int(self.jogadores[n].x_values[self.jogadores[n].contador])
            self.jogadores[n].y = int(self.jogadores[n].y_values[self.jogadores[n].contador])

            self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y);
            self.canvas.move(self.jogadores[n].jogador, 0, 0);
        self.conectar_jogadores()

    def atualiza_posicao_bola(self):
        if not self.is_paused:  # verifica se o loop está pausado
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

            self.conectar_jogadores()

def achandoValoresXeY(jogadores,BD):
    print("Processando os Dados!")

    for k in range(0, len(BD)):
        # _, maxLat, maxLog, _, _, _ = BD[k].max()
        # _, minLat, minLog, _, _, _ = BD[k].min()

        _, maxLat, maxLog, _,_,_,_,_,_,_,_,_ = BD[k].max()
        _, minLat, minLog, _,_,_,_,_,_,_,_,_= BD[k].min()

        dfiLat = maxLat - minLat
        dfiLog = maxLog - minLog

        if(k==0):
            print("maior lat, menor lat: ", maxLat, minLat)
            print("maior Log, menor Log: ", maxLog, minLog)
            print("max - ",maxLat,maxLog)
            print("min - ",minLat,minLog)

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
