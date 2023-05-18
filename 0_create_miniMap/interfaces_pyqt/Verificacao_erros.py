from Informacoes import *

def erro_qtde_jgs(info):
    tam1 = 0; tam2 = 0

    for i in range(0,4):
        if (info.equipe1[i] != ""):
            tam1+=1

    for i in range(0,4):
        if (info.equipe2[i] != ""):
            tam2+=1

    if(tam1 != tam2):
        print("Quantidade de jogadores da equipe diferentes")
        return True
    else:
        return False

def erro_qtde_opcoes(info):

    opc1 = info.opcao_gps
    opc2 = info.opcao_camera
    opc3 = info.opcao_gps_camera

    if (opc1 and opc2 and opc3):
        print("Tem 3 opcões selecionadas, Selecione apenas 1")
        return True
    if (opc1 and opc2):
        print("Tem 2 opcões selecionadas, Selecione apenas 1")
        return True
    if (opc1 and opc3):
        print("Tem 2 opcões selecionadas, Selecione apenas 1")
        return True
    if (opc2 and opc3):
        print("Tem 2 opcões selecionadas, Selecione apenas 1")
        return True
    else:
        return False