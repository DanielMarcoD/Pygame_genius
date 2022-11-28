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