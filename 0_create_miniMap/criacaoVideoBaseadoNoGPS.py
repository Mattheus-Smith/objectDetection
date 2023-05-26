import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyproj import Proj

# Função para converter latitudes e longitudes em coordenadas X e Y
def latlon_to_xy(latitude, longitude):
    # Defina a projeção UTM adequada para Manaus (zona 20 da UTM)
    p = Proj(proj='utm', zone=20, ellps='WGS84')

    # Converta as coordenadas de latitude e longitude para X e Y
    x, y = p(longitude, latitude)

    return x, y

# Obter as dimensões dos vídeos
width = int(640)
height = int(480)

# Criar o codec de vídeo para salvar o vídeo de saída
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video_saida.mp4', fourcc, 10, (width, height))

# Ler a aba específica "Calibracao" do arquivo Excel
cone1 = pd.read_excel('./data_3b/GPS 1.xlsx', sheet_name='Calibracao')
cone2 = pd.read_excel('./data_3b/GPS 2.xlsx', sheet_name='Calibracao')
cone3 = pd.read_excel('./data_3b/GPS 3.xlsx', sheet_name='Calibracao')
cone4 = pd.read_excel('./data_3b/GPS 4.xlsx', sheet_name='Calibracao')
cones = [cone1, cone2, cone3, cone4]

# Valores de latitude e longitude dos cones
lat_cone1 = cones[0].iloc[:, 1].mean(); log_cone1 = cones[0].iloc[:, 2].mean()
lat_cone2 = cones[1].iloc[:, 1].mean(); log_cone2 = cones[1].iloc[:, 2].mean()
lat_cone3 = cones[2].iloc[:, 1].mean(); log_cone3 = cones[2].iloc[:, 2].mean()
lat_cone4 = cones[3].iloc[:, 1].mean(); log_cone4 = cones[3].iloc[:, 2].mean()

lat_cones = [lat_cone1, lat_cone2, lat_cone3, lat_cone4]
log_cones = [log_cone1, log_cone2, log_cone3, log_cone4]

# Ler a aba específica "Suicidio" do arquivo Excel
jg1 = pd.read_excel('./data_3b/GPS 1.xlsx', sheet_name='Jogo 01')
jg2 = pd.read_excel('./data_3b/GPS 2.xlsx', sheet_name='Jogo 01')
jg3 = pd.read_excel('./data_3b/GPS 3.xlsx', sheet_name='Jogo 01')

jg5 = pd.read_excel('./data_3b/GPS 5.xlsx', sheet_name='Jogo 01')
jg6 = pd.read_excel('./data_3b/GPS 6.xlsx', sheet_name='Jogo 01')
jg7 = pd.read_excel('./data_3b/GPS 7.xlsx', sheet_name='Jogo 01')
jogadores=[jg1, jg2, jg3, jg5, jg6, jg7]
tamanho = min(
    len(jogadores[0].iloc[:, 1]),
    len(jogadores[1].iloc[:, 1]),
    len(jogadores[2].iloc[:, 1]),
    len(jogadores[3].iloc[:, 1]),
    len(jogadores[4].iloc[:, 1]),
    len(jogadores[5].iloc[:, 1])
)
print(tamanho)

# Valores de latitude e longitude dos cones
lat_jogador1 = jogadores[0].iloc[:, 1]; log_jogador1 = jogadores[0].iloc[:, 2]
lat_jogador2 = jogadores[1].iloc[:, 1]; log_jogador2 = jogadores[1].iloc[:, 2]
lat_jogador3 = jogadores[2].iloc[:, 1]; log_jogador3 = jogadores[2].iloc[:, 2]

lat_jogador5 = jogadores[3].iloc[:, 1]; log_jogador5 = jogadores[3].iloc[:, 2]
lat_jogador6 = jogadores[4].iloc[:, 1]; log_jogador6 = jogadores[4].iloc[:, 2]
lat_jogador7 = jogadores[5].iloc[:, 1]; log_jogador7 = jogadores[5].iloc[:, 2]

lat_jogadores = [lat_jogador1, lat_jogador2, lat_jogador3, lat_jogador5, lat_jogador6, lat_jogador7]
log_jogadores = [log_jogador1, log_jogador2, log_jogador3, log_jogador5, log_jogador6, log_jogador7]

#tamanho = min(jg1, jg2, jg3, jg5, jg6, jg7)

# Criar listas vazias para armazenar todas as coordenadas X e Y
coordenadas_x = []
coordenadas_y = []
cores = ["green", "blue", "black","purple", "pink", "orange"]

def print_jogador(lat, log):
    x, y = latlon_to_xy(lat, log)
    return x, y

def print_cones(lat, log):
    x, y = latlon_to_xy(lat, log)
    return x, y

for j in range(0, 1000):

    # Definir os limites dos eixos X e Y
    #plt.ylim(-346000, -345000)  # Delimita o eixo X entre 0 e 6
    # plt.xlim(-15, 25)  # Delimita o eixo Y entre 0 e 12

    for i in range(0, len(lat_cones)):
        x, y = print_cones(lat_cones[i], log_cones[i])
        plt.scatter(x, y, color="red")

    for i in range(0, len(lat_jogadores)):
        x, y = print_jogador(lat_jogadores[i][j], log_jogadores[i][j])
        plt.scatter(x, y, color=cores[i])

    plt.savefig('img.png')
    plt.close()

    imagem = cv2.imread('./img.png')
    # Rotacionar a imagem em 180 graus para acopanhar junto com o video
    imagem_rotacionada = cv2.rotate(imagem, cv2.ROTATE_180)

    # Escrever o frame combinado no vídeo de saída
    out.write(cv2.resize(imagem_rotacionada, (width, height)))

    # Mostrar o frame combinado em uma janela
    # cv2.imshow('Combined Video', imagem)

# Liberar os recursos
out.release()
cv2.destroyAllWindows()