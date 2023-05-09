import pandas as pd
import numpy as np
from tkinter import *

from PIL import Image, ImageTk

from Jogador import *
from Metricas import *

df1 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 1_Wildes_Equipe 1.xlsx")
df2 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 2_Alvaro_Equipe 1.xlsx")
df3 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 3_Cristiano_Equipe 1.xlsx")

df4 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 4_Alan_Equipe 2.xlsx")
df5 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 5_Flavio_Equipe 2.xlsx")
df6 = pd.read_excel("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\1_VisaoComputacional\\yolov3-tf2-darknet\\0_create_miniMap\\data\\GPS 6_Antonio_Equipe 2.xlsx")

bancosDados = [df1,df2, df3, df4,df5,df6]
bancosDados1 = [df1,df2, df3]
#bancosDados2 = [df4,df5, df6]


x_campo = 1010
y_campo = 510

class Window:

    def __init__(self):
        self.tela = Tk()
        self.tela.title('MiniMapa dos Jogadores')
        self.is_paused = False  # variável de controle do estado do loop
        self.is_next = False
        self.speed = 5

        # Carrega a imagem original usando a biblioteca PIL
        self.background_image_original = Image.open("campo_futebol_menor.png")

        # Obter as dimensões da imagem
        self.width = 1100
        self.height = 600

        self.image_resized = self.background_image_original.resize((self.width, self.height), resample=Image.LANCZOS)

        # Converte a imagem para um objeto Tkinter PhotoImage
        self.image_tk = ImageTk.PhotoImage(self.image_resized)

        self.tela.geometry('1300x700')
        self.tela.resizable(False, False)

        # Criando o frame1 - minimapa
        self.frame1 = Frame(self.tela, height=600)
        self.frame1.pack(side="top", fill="both", expand=True)

        # Criando o frame2 - footer
        self.frame2 = Frame(self.tela, height=100, width=600)
        self.frame2.pack(side="bottom", fill="both", expand=True)

        # Criando o footer da EQUIPE 1
        self.footer1 = Frame(self.frame2, bg="lightblue", width=300)
        self.footer1.pack(side="left", padx=10, pady=10)

        # Criando o footer da EQUIPE 2
        self.footer2 = Frame(self.frame2, bg="lightgreen", width=300)
        self.footer2.pack(side="right", padx=10, pady=10)

        # Criando o frame3 - botoes de reproducao
        self.frame3 = Frame(self.frame1)
        self.frame3.pack(side="bottom", anchor="s")

        self.canvas = Canvas(self.frame1, width=1010, height=510)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")


        print("Criando as Equipes!")
        self.jogadores = []
        cores = ["blue", "red", "pink"]

        for n in range(0,len(bancosDados)):
            if(n < 3):
                #(self, canvas, diametro, equipe,color, x_values, y_values, contador, status, posicao_x, posicao_y, breakCont, id , x, y, x_org, y_org):
                self.jogadores.append(Jogador(self.canvas, 10, 1,cores[0], [], [], 0, 0, 0, 0, 0, n, 0, 0, 0, 0))
            else:
                self.jogadores.append(Jogador(self.canvas, 10, 2,cores[1], [], [], 0, 0, 0, 0, 0, n, 0, 0, 0, 0))

        equipe1,equipe2 = self.dividir_em_equipe()

        self.metricas_1 = Metricas(equipe1, 0, 0, 0, 0)
        self.centroide1 = self.canvas.create_oval(0, 0, 10, 10, fill=cores[2])

        self.metricas_2 = Metricas(equipe2, 0, 0, 0, 0)
        self.centroide2 = self.canvas.create_oval(0, 0, 10, 10, fill=cores[2])

        self.label_comprimento_valor_1 = None
        self.label_largura_valor_1 = None
        self.label_LPW_valor_1 = None
        self.label_team_Separateness_1 = None

        self.label_comprimento_valor_2 = None
        self.label_largura_valor_2 = None
        self.label_LPW_valor_2 = None
        self.label_team_Separateness_2 = None

    def criar_footer_informacoes(self):
        ###==================== EQUIPE 1

        equipe1 = Label(self.footer1, text="EQUIPE 1", fg="blue")
        equipe1.grid(row=0, column=0, columnspan=2)

        label_comprimento_1 = Label(self.footer1, text="comprimento: ")
        label_comprimento_1.grid(row=1, column=0, sticky=W)

        self.label_comprimento_valor_1 = Label(self.footer1, text=self.metricas_1.comprimento)
        self.label_comprimento_valor_1.grid(row=1, column=1, sticky=W)

        label_largura_1 = Label(self.footer1, text="largura: ")
        label_largura_1.grid(row=2, column=0, sticky=W)

        self.label_largura_valor_1 = Label(self.footer1, text=self.metricas_1.largura)
        self.label_largura_valor_1.grid(row=2, column=1, sticky=W)

        label_LPW_1 = Label(self.footer1, text="LpW: ")
        label_LPW_1.grid(row=3, column=0, sticky=W)

        self.label_LPW_valor_1 = Label(self.footer1, text=self.metricas_1.LPW)
        self.label_LPW_valor_1.grid(row=3, column=1, sticky=W)

        label_team_Separateness_1 = Label(self.footer1, text="Team's Separateness: ")
        label_team_Separateness_1.grid(row=4, column=0, sticky=W)

        self.label_team_Separateness_1 = Label(self.footer1, text=self.metricas_1.team_Separateness)
        self.label_team_Separateness_1.grid(row=4, column=1, sticky=W)


        ###==================== EQUIPE 2

        equipe1 = Label(self.footer2, text="EQUIPE 2", fg="red")
        equipe1.grid(row=0, column=0, columnspan=2)

        label_comprimento_1 = Label(self.footer2, text="comprimento: ")
        label_comprimento_1.grid(row=1, column=0, sticky=W)

        self.label_comprimento_valor_2 = Label(self.footer2, text=self.metricas_2.comprimento)
        self.label_comprimento_valor_2.grid(row=1, column=1, sticky=W)

        label_largura_1 = Label(self.footer2, text="largura: ")
        label_largura_1.grid(row=2, column=0, sticky=W)

        self.label_largura_valor_2 = Label(self.footer2, text=self.metricas_2.largura)
        self.label_largura_valor_2.grid(row=2, column=1, sticky=W)

        label_LPW_1 = Label(self.footer2, text="LpW: ")
        label_LPW_1.grid(row=3, column=0, sticky=W)

        self.label_LPW_valor_2 = Label(self.footer2, text=self.metricas_2.LPW)
        self.label_LPW_valor_2.grid(row=3, column=1, sticky=W)

        label_team_Separateness_2 = Label(self.footer2, text="Team's Separateness: ")
        label_team_Separateness_2.grid(row=4, column=0, sticky=W)

        self.label_team_Separateness_2 = Label(self.footer2, text=self.metricas_2.team_Separateness)
        self.label_team_Separateness_2.grid(row=4, column=1, sticky=W)

    def pause(self):
        self.is_paused = True

    def play(self):
        self.is_paused = False
        self.atualiza_posicao_bola()  # retoma o loop

    def next(self):
        self.pause()
        self.is_next = True
        self.movimentar_jogadores()
        self.metricas_1.jogadores, self.metricas_2.jogadores = self.dividir_em_equipe()
        self.conectar_jogadores(self.metricas_1.jogadores, self.metricas_2.jogadores)
        self.verificar_centroide(self.metricas_1.jogadores, self.metricas_2.jogadores)

        self.metricas_1.verificar_comprimento()
        self.metricas_1.verificar_largura()
        self.metricas_1.verificar_team_Separateness()
        self.metricas_1.att_lpw()

        self.metricas_2.verificar_comprimento()
        self.metricas_2.verificar_largura()
        self.metricas_2.verificar_team_Separateness()
        self.metricas_2.att_lpw()

        self.att_labels()

    def atualizar_speed(self, valor):
        self.speed = valor

    def inicializarLoop(self):
        print("Iniciando o Loop!")
        self.frame1.after(0, self.atualiza_posicao_bola)  # agendamento inicial

        # Cria o controle deslizante
        controle_deslizante = Scale(self.frame3, from_=1, to=30, orient="horizontal", resolution=1, command=self.atualizar_speed)
        controle_deslizante.set(self.speed)  # Define o valor inicial
        controle_deslizante.pack(side="left", padx=20, pady=20, anchor="center")

        sair = Button(self.frame3, text='Sair', bg='red', command=self.tela.destroy)
        sair.pack(side="left", padx=20, pady=10, anchor="center")

        pause = Button(self.frame3, text='Pause', bg='red', command=self.pause)
        pause.pack(side="left", padx=20, pady=20, anchor="center")

        play = Button(self.frame3, text='Play', bg='red', command=self.play)
        play.pack(side="left", padx=20, pady=20, anchor="center")

        next = Button(self.frame3, text='Next', bg='red', command=self.next)
        next.pack(side="left", padx=20, pady=20, anchor="center")

        self.tela.mainloop()

    def dividir_em_equipe(self):
        equipe1 = []
        equipe2 = []

        for i in range(len(self.jogadores)):
            if (self.jogadores[i].equipe == 1):
                equipe1.append(self.jogadores[i])
            else:
                equipe2.append(self.jogadores[i])
        return equipe1,equipe2

    def conectar_jogadores(self, equipe1,equipe2):

        # Apaga as linhas antigas
        self.canvas.delete("line")

        # Cria as novas linhas entre as equipe 1
        for i in range(len(equipe1) - 1):
            x1, y1, x2, y2 = self.canvas.coords(equipe1[i].jogador)
            x3, y3, x4, y4 = self.canvas.coords(equipe1[i + 1].jogador)
            line = self.canvas.create_line(x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2,
                                      x3 + (x4 - x3) // 2, y3 + (y4 - y3) // 2, tags="line",fill='red')
        # Cria a última linha que liga o último círculo ao primeiro
        x1, y1, x2, y2 = self.canvas.coords(equipe1[-1].jogador)
        x3, y3, x4, y4 = self.canvas.coords(equipe1[0].jogador)
        line = self.canvas.create_line(x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2,
                                  x3 + (x4 - x3) // 2, y3 + (y4 - y3) // 2, tags="line",fill='red')

        # Cria as novas linhas entre a equipe 2
        for i in range(len(equipe2) - 1):
            x1, y1, x2, y2 = self.canvas.coords(equipe2[i].jogador)
            x3, y3, x4, y4 = self.canvas.coords(equipe2[i + 1].jogador)
            line = self.canvas.create_line(x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2,
                                           x3 + (x4 - x3) // 2, y3 + (y4 - y3) // 2, tags="line", fill='red')
        # Cria a última linha que liga o último círculo ao primeiro
        x1, y1, x2, y2 = self.canvas.coords(equipe2[-1].jogador)
        x3, y3, x4, y4 = self.canvas.coords(equipe2[0].jogador)
        line = self.canvas.create_line(x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2,
                                       x3 + (x4 - x3) // 2, y3 + (y4 - y3) // 2, tags="line", fill='red')

    def verificar_centroide(self, equipe1,equipe2):
        #========= centroide EQUIPE 1
        media_x=[]
        for i in range(0, len(equipe1)):
            media_x.append(equipe1[i].x_org)

        media_y = []
        for i in range(0, len(equipe1)):
            media_y.append(equipe1[i].y_org)

        centroide_x = np.mean(media_x)
        centroide_y = np.mean(media_y)

        # Atualiza a posição do objeto oval
        self.canvas.coords(self.centroide1, centroide_x, centroide_y, centroide_x + 10, centroide_y + 10);

        # ========= centroide EQUIPE 2
        media_x = []
        for i in range(0, len(equipe2)):
            media_x.append(equipe2[i].x_org)

        media_y = []
        for i in range(0, len(equipe2)):
            media_y.append(equipe2[i].y_org)

        centroide_x = np.mean(media_x)
        centroide_y = np.mean(media_y)

        # Atualiza a posição do objeto oval
        self.canvas.coords(self.centroide2, centroide_x, centroide_y, centroide_x + 10, centroide_y + 10);

    def att_labels(self):
        self.label_comprimento_valor_1.configure(text=self.metricas_1.comprimento)
        self.label_largura_valor_1.configure(text=self.metricas_1.largura)
        texto_formatado = "{:.2f}".format(self.metricas_1.LPW)
        self.label_LPW_valor_1.configure(text=texto_formatado)
        texto_formatado = "{:.2f}".format(self.metricas_1.team_Separateness)
        self.label_team_Separateness_1.configure(text=texto_formatado)

        self.label_comprimento_valor_2.configure(text=self.metricas_2.comprimento)
        self.label_largura_valor_2.configure(text=self.metricas_2.largura)
        texto_formatado = "{:.2f}".format(self.metricas_2.LPW)
        self.label_LPW_valor_2.configure(text=texto_formatado)
        texto_formatado = "{:.2f}".format(self.metricas_2.team_Separateness)
        self.label_team_Separateness_2.configure(text=texto_formatado)

    def inicializarJogadoresNoMiniMapa(self):
        print("Inicializando os Jogados em Campo!")
        for n in range(0, len(self.jogadores)):
            self.jogadores[n].x = int(self.jogadores[n].x_values[self.jogadores[n].contador])
            self.jogadores[n].y = int(self.jogadores[n].y_values[self.jogadores[n].contador])
            self.jogadores[n].x_org = int(self.jogadores[n].x_values[self.jogadores[n].contador])
            self.jogadores[n].y_org = int(self.jogadores[n].y_values[self.jogadores[n].contador])

            # print(self.jogadores[n].x_org, self.jogadores[n].y_org, self.jogadores[n].color)

            self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y);
            self.canvas.move(self.jogadores[n].jogador, 0, 0);
            self.canvas.coords(self.centroide1, 0, 0, 0 + 10, 0 + 10);
            self.canvas.coords(self.centroide2, 0, 0, 0 + 10, 0 + 10);

        self.metricas_1.jogadores,self.metricas_2.jogadores = self.dividir_em_equipe()
        self.conectar_jogadores(self.metricas_1.jogadores,self.metricas_2.jogadores)
        self.verificar_centroide(self.metricas_1.jogadores,self.metricas_2.jogadores)

        self.metricas_1.verificar_comprimento()
        self.metricas_1.verificar_largura()
        self.metricas_1.verificar_team_Separateness()
        self.metricas_1.att_lpw()

        self.metricas_2.verificar_comprimento()
        self.metricas_2.verificar_largura()
        self.metricas_2.verificar_team_Separateness()
        self.metricas_2.att_lpw()

        self.att_labels()

    def movimentar_jogadores(self):
        for n in range(0, len(self.jogadores)):
            # print(tam," == ", contador)
            if (len(self.jogadores[n].x_values) == self.jogadores[n].contador + 1):
                self.jogadores[n].breakCont = 1
                self.jogadores[n].status = -1

            if (self.jogadores[n].status == 0):
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                self.jogadores[n].contador = self.jogadores[n].contador + 1
                self.jogadores[n].posicao_x = int(self.jogadores[n].x_values[self.jogadores[n].contador] - self.jogadores[n].x_values[self.jogadores[n].contador - 1])
                self.jogadores[n].posicao_y = int(self.jogadores[n].y_values[self.jogadores[n].contador] - self.jogadores[n].y_values[self.jogadores[n].contador - 1])
                self.jogadores[n].definirStatus()
                # print("Xa:", xb, "- Ya:", ys - 10, " ||  Xd:", int(self.jogadores[n].x_values[self.jogadores[n].contador]),"- Yd:", int(self.jogadores[n].y_values[self.jogadores[n].contador]), "status: ", self.jogadores[n].status)

            elif (self.jogadores[n].status == 1):  # direita
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x - 1
                self.jogadores[n].right()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, 0)
                self.jogadores[n].x_org += 1
                self.jogadores[n].y_org += 0
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 1 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 2):  # esquerda
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x + 1
                self.jogadores[n].left()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, 0)
                self.jogadores[n].x_org += -1
                self.jogadores[n].y_org += 0
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 2 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 3):  # cima
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y - 1
                self.jogadores[n].up()
                self.canvas.move(self.jogadores[n].jogador, 0, self.jogadores[n].y)
                self.jogadores[n].x_org += 0
                self.jogadores[n].y_org += 1
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 3 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 4):  # baixo
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y + 1
                self.jogadores[n].down()
                self.canvas.move(self.jogadores[n].jogador, 0, self.jogadores[n].y)
                self.jogadores[n].x_org += 0
                self.jogadores[n].y_org += -1
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 4 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 5):  # direita and cima
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x - 1
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y - 1
                self.jogadores[n].up()
                self.jogadores[n].right()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y)
                self.jogadores[n].x_org += 1
                self.jogadores[n].y_org += 1
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 5 - x: ",xb ," y: ",ys-10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 6):  # esquerda and cima
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x + 1
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y - 1
                self.jogadores[n].up()
                self.jogadores[n].left()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y)
                self.jogadores[n].x_org += -1
                self.jogadores[n].y_org += 1
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
                self.jogadores[n].x_org += -1
                self.jogadores[n].y_org += -1
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 7 - x: ", xb, " y: ", ys - 10)
                self.jogadores[n].definirStatus()

            elif (self.jogadores[n].status == 8):  # direita and baixo
                self.jogadores[n].posicao_x = self.jogadores[n].posicao_x - 1
                self.jogadores[n].posicao_y = self.jogadores[n].posicao_y + 1
                self.jogadores[n].down()
                self.jogadores[n].right()
                self.canvas.move(self.jogadores[n].jogador, self.jogadores[n].x, self.jogadores[n].y)
                self.jogadores[n].x_org += 1
                self.jogadores[n].y_org += -1
                xb, yb, xs, ys = self.canvas.coords(self.jogadores[n].jogador)
                # print("status 8 - x: ",xb ," y: ",ys-10)
                self.jogadores[n].definirStatus()

            if (self.jogadores[n].breakCont == 1 and self.jogadores[n].status == -1):
                print("estorou tamanho")
                self.canvas.move(self.jogadores[n].jogador, 0, 0)
                self.metricas_1.relatorio_metricas(1)
                self.metricas_2.relatorio_metricas(2)
                break
            elif(self.is_next):
                a=1
            else:
                if (n == len(self.jogadores) - 1):
                    self.frame1.after(self.speed, self.atualiza_posicao_bola)  # agenda pra daqui a pouco

    def atualiza_posicao_bola(self):
        if not self.is_paused:  # verifica se o loop está pausado

            self.movimentar_jogadores()

            self.metricas_1.jogadores, self.metricas_2.jogadores = self.dividir_em_equipe()
            self.conectar_jogadores(self.metricas_1.jogadores, self.metricas_2.jogadores)
            self.verificar_centroide(self.metricas_1.jogadores, self.metricas_2.jogadores)

            self.metricas_1.verificar_comprimento()
            self.metricas_1.verificar_largura()
            self.metricas_1.verificar_team_Separateness()
            self.metricas_1.att_lpw()

            self.metricas_2.verificar_comprimento()
            self.metricas_2.verificar_largura()
            self.metricas_2.verificar_team_Separateness()
            self.metricas_2.att_lpw()

            self.att_labels()

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

frame1 = Window()
frame1.criar_footer_informacoes()
achandoValoresXeY(frame1.jogadores,bancosDados)
frame1.inicializarJogadoresNoMiniMapa()
frame1.inicializarLoop()
