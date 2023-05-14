import pandas as pd
import numpy as np
from tkinter import *

from PIL import Image, ImageTk

from Jogador import *
from Metricas import *

class Interface:

    def __init__(self):
        self.tela = Tk()
        self.tela.title('Menu de opção')
        self.tela.geometry('600x600')
        self.tela.resizable(False, False)

        self.tela.mainloop()

Interface()

import tkinter as tk

def trocar_frames():
    frame1.pack_forget()
    frame2.pack()
    # Centralizando o Frame 2
    frame2.pack(fill='both', expand=True)

root = tk.Tk()
root.geometry('600x600')

# =====================================Criando o Frame 1
frame1 = tk.Frame(root)
frame1.pack()

# Adicionando um botão ao Frame 1
botao = tk.Button(frame1, text="Trocar para Frame 2", command=trocar_frames)
botao.pack(pady=20)

# =====================================Criando o Frame 2
frame2 = tk.Frame(root)

# Criando o contêiner para o Label "mensagem" com borda
container_mensagem = tk.Frame(frame2, borderwidth=1, relief="solid")
container_mensagem.pack(pady=20)

# Criando o Label "mensagem" dentro do contêiner
mensagem = tk.Label(container_mensagem, text="Bem-vindo ao Frame 2")
mensagem.pack(padx=10, pady=10)

# Criando os botões laterais no Frame 2
botao_esquerda = tk.Button(frame2, text="Botão Esquerda")
botao_esquerda.pack(side='left', padx=10)

botao_direita = tk.Button(frame2, text="Botão Direita")
botao_direita.pack(side='right', padx=10)


root.mainloop()

