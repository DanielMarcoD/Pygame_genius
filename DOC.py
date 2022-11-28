import random, pygame, time
from pygame.locals import *
from tkinter import *

pygame.init()
tempo = pygame.time.Clock()
texto_inicio_fonte = pygame.font.SysFont('Arial', 80)
options_fonte = pygame.font.SysFont('Arial', 40)                  # Fonte para as opções
status_fonte = pygame.font.SysFont('Calibri', 15)               # Fonte para a barra de status

tela_inicial = pygame.display.set_mode((500, 530), 0, 32)           # Janela
pygame.display.set_caption("DOC")                            # Titulo da janela
tela_icone = pygame.image.load('assets/logo2.png')                       # Imagem do icone do jogo
pygame.display.set_icon(tela_icone)
status_bar = pygame.Surface((tela_inicial.get_width(), 30))       # Barra de status
status_bar.fill((0, 0, 0))                                # Cor da barra de status

tela_de_fundo = pygame.image.load('assets/DOC.png')                     # Imagem de fundo
tela_jogo = pygame.image.load('assets/Fundo.png')

# Cores
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
AZUL = (50, 190, 255)
BRANCO = (255, 255, 255)

# Sons
sons = {'som_do': 'sons/do.wav', 'som_re': 'sons/re.wav', 'som_mi': 'sons/mi.wav', 'som_fa': 'sons/fa.wav',
        'perdeu': 'sons/perdeu_jogo.wav', 'clique': 'sons/clique.wav'}

# Poligonos que detectam a escolha com o clique do mouse
verde = pygame.draw.polygon(tela_inicial, VERDE, ((81, 317), (230, 317), (230, 159)))
amarelo = pygame.draw.polygon(tela_inicial, AMARELO, ((409, 315), (263, 315), (263, 168)))
vermelha = pygame.draw.polygon(tela_inicial, VERMELHO, ((80, 345), (230, 346), (230, 495)))
azul = pygame.draw.polygon(tela_inicial, AZUL, ((411, 345), (265, 347), (263, 495)))

# Textos
texto_comeco = texto_inicio_fonte.render('Jogar', True, (255, 255, 255))   # Texto do botao começar
texto = ' '

points = 0                                                      # Pontuação
seq_colors = []                                            # Sequencia de cores que vao piscar
game = False

game_ranking = {'pontos': '', 'nome': ''}                       # Armazena quem esta no ranking
player_name = '' 