import random, pygame, time
from pygame.locals import *
from tkinter import *

pygame.init()
tempo = pygame.time.Clock()
texto_inicio_fonte = pygame.font.SysFont('Arial', 80)
options_fonte = pygame.font.SysFont('Arial', 40)                  
status_fonte = pygame.font.SysFont('Calibri', 15)               

tela_inicial = pygame.display.set_mode((500, 530), 0, 32)           
pygame.display.set_caption("DOC")                            
tela_icone = pygame.image.load('assets/logo2.png')                       
pygame.display.set_icon(tela_icone)
status_bar = pygame.Surface((tela_inicial.get_width(), 30))       
status_bar.fill((0, 0, 0))                                

tela_de_fundo = pygame.image.load('assets/DOC.png')                     
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
amarelo = pygame.draw.polygon(tela_inicial, AMARELO, ((409, 315), (263, 315), (263, 159)))
vermelha = pygame.draw.polygon(tela_inicial, VERMELHO, ((80, 345), (230, 346), (230, 495)))
azul = pygame.draw.polygon(tela_inicial, AZUL, ((411, 345), (265, 347), (263, 495)))

# Textos
texto_comeco = texto_inicio_fonte.render('Jogar', True, (255, 255, 255))   
texto = ' '

points = 0                                                    
seq_colors = []                                            
game = False

def choose_color():
    verde_light = {'cor': VERDE, 'posicao': ((81, 317), (230, 317), (230, 169)), 'som': sons['som_do']}
    amarelo_light = {'cor': AMARELO, 'posicao': ((409, 315), (263, 315), (263, 168)), 'som': sons['som_fa']}
    azul_light = {'cor': AZUL, 'posicao': ((411, 345), (264, 346), (263, 495)), 'som': sons['som_mi']}
    vermelho_light = {'cor': VERMELHO, 'posicao': ((80, 345), (230, 346), (230, 495)), 'som': sons['som_re']}

    colors = [verde_light, amarelo_light, vermelho_light, azul_light]
    return random.choice(colors)
game= True    
while game:
    

    for evento in pygame.event.get():
        if evento.type == QUIT:
            quit()


        if game:
            
            points = 0                                          
            seq_colors = []                                
            continue
        else:
            quit()

    pygame.display.update()
    tempo.tick(27)
