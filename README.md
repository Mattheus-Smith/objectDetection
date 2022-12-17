# yolov3-tf2-darknet
<p>Usar o YOLOv3 para fazer detecção de jogadores a partir de uma partida de futebol gravada.</p>

# Resumo
<p>Esse projeto usa como referência o YOLOv3-Darknet disponibilizado em [REFE 1] para fazer a detecção dos jogadores. Além de um banco de dados contendo as coordenadas dos jogadores extraídas de um gps que os mesmos usaram durante a gravação das partidas.</p>

<p>PARTE 1: É feita a detecção dos jogadores frame a frame a partir da rede pré-treinada. Com os objetos em questão detectados(jogadores) é aplicado uma máscara para distiguir os jogadores baseado na cor das suas camisa.</p>

<p>PARTE 2: Com o banco de dados contendo as coordenadas do GPS é possivel criar um mini mapa para fazer análise de posicionamento dos jogadores, para saber se eles estão executando as jogadas ou até mesmo descobrindo posições nao ocupadas pelos jogadores durante as jogadas.</p>

# Execução do Projeto
<p>No github do [REFE 1] ele mostra como executar os arquivos. Mas irei fazer o meu proprio tutorial de como usar os algoritmos.</p>

# Instalação
1. Criar um Ambiente Virtual
<p>É usado a biblioteca "virtualenv" para criar o ambiente virtual. Mas vc pode usar o "conda" também.</p>

```bash
virtualenv <nome do ambiente>

```

2.Ativar o Ambiente Virtual
```bash
source <nome do ambiente>/Scripts/activate

```

3.Desativar o Ambiente Virtual

```bash
deactivate

```

# Treinar

# Executar

# yolov3
-> excutar para qq foto ok ./venvYolo/Scripts/python.exe detect.py --image ./data/meme.jpg

-> executar codigo com webcam ok ./venvYolo/Scripts/python.exe detect_video.py --video 0

-> ler video (ta dando erro) ./venvYolo/Scripts/python.exe detect_video.py --video ./data/video.mp4 --weights ./checkpoints/yolov3.tf.index --tiny

-> ler video um video especifico com saida. E usa a opcao 1 (desenhar a partir da cor da camisa) ok ./venvYolo/Scripts/python.exe detect_video.py --video ./data/video.mp4 --output ./output.mp4 --opcao 1

