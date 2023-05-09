import numpy as np
from Jogador import *

class Metricas:
    def __init__(self, jogadores,comprimento, largura, LPW, team_Separateness):
        self.jogadores = jogadores
        self.comprimento = comprimento
        self.largura = largura
        self.LPW = LPW
        self.team_Separateness = team_Separateness

        self.comprimento_vetor = []
        self.largura_vetor = []
        self.LPW_vetor = []
        self.team_Separateness_vetor = []
        self.centroidde_vetor = []
        self.qte_mov_jogadores_vetor = []
        self.media_jogadores_x_vetor = []
        self.media_jogadores_y_vetor = []

    def att_info_IES(self):
        for n in range(0, len(self.jogadores)):
            self.qte_mov_jogador_vetor.append(self.jogadores[n].x_values)

            self.media_jogadores_x_vetor.append(self.jogadores[n].x_values)
            self.media_jogadores_y_vetor.append(self.jogadores[n].x_values)

    def verificar_largura(self):
        # verificar X mais a esquerda(MAIOR X)
        id1 = 0
        maior = self.jogadores[id1].y_org
        for i in range(1, len(self.jogadores)):
            if (self.jogadores[i].y_org > maior):
                maior = self.jogadores[i].y_org
                id1 = i

        # verificar X mais a direita(MENOR X)
        id2 = 0
        menor = self.jogadores[id2].y_org
        for i in range(1, len(self.jogadores)):
            if (self.jogadores[i].y_org < menor):
                menor = self.jogadores[i].y_org
                id2 = i

        # print("maior: ",maior, self.jogadores[id1].color)
        # print("menor: ", menor, self.jogadores[id2].color)
        # print("dff: ", maior - menor)
        self.largura = maior - menor
        self.largura_vetor.append(self.largura)

    def verificar_comprimento(self):
        #verificar X mais a esquerda(MAIOR X)
        id1 = 0; maior = self.jogadores[id1].x_org
        for i in range(1, len(self.jogadores)):
            if(self.jogadores[i].x_org > maior):
                id1 = i; maior = self.jogadores[i].x_org

        # verificar X mais a direita(MENOR X)
        id2 = 0; menor = self.jogadores[id2].x_org
        for i in range(1, len(self.jogadores)):
            if (self.jogadores[i].x_org < menor):
                id2 = i; menor = self.jogadores[i].x_org

        # print("maior: ",maior, self.jogadores[id1].color); print("menor: ", menor, self.jogadores[id2].color); print("dff: ", maior - menor)
        self.comprimento = maior-menor
        self.comprimento_vetor.append(self.comprimento)

    def att_lpw(self):
        self.LPW = self.comprimento / self.largura
        self.LPW_vetor.append(self.LPW)

    def verificar_team_Separateness(self):
        total_dist = 0
        for i in range(0, len(self.jogadores)):
            for j in range(0, len(self.jogadores)):
                distancia = np.sqrt( pow(self.jogadores[i].x_org-self.jogadores[j].x_org, 2) + pow(self.jogadores[i].y_org-self.jogadores[j].y_org, 2))
            total_dist+=distancia
        self.team_Separateness = total_dist
        self.team_Separateness_vetor.append(total_dist)

    def get_largura_media(self):
        media = np.mean(self.largura_vetor)
        print("largura media: ",media)

    def get_comprimento_media(self):
        media = np.mean(self.comprimento_vetor)
        print("comprimento media: ",media)

    def get_lpw_media(self):
        media = np.mean(self.LPW_vetor)
        print("LPW media: ",media)

    def get_centroide_media(self):
        media = np.mean(self.centroide_vetor)
        print("centroide media: ",media)

    def relatorio_metricas(self):
        print("Largura: ", self.get_largura_media(), " | Comprimento: ", self.get_comprimento_media(), " | LpW: ", self.get_lpw_media(), " | Centroide: ", self.get_centroide_media())