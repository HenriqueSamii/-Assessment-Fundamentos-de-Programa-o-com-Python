#Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta),
#  toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
import pygame,random

larguraTela = 800
alturaTela = 600

tela  = pygame.display.set_mode([larguraTela,alturaTela])

pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

tamanho = 50

def quadrado_amarelo(X,Y):
    pygame.draw.rect(tela, YELLOW, [X, Y, tamanho,tamanho])

quadradosHolderArray = []

##### jogo runtime ####
treminou = False

while not treminou:
    pygame.display.update()
    tela.fill(BLACK)
    #Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            treminou = True
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.dict["button"] == 3):
            quadradosHolderArray.append((random.randint(0, larguraTela-tamanho), random.randint(0, alturaTela-tamanho)))
    
    for posicao in quadradosHolderArray:
        quadrado_amarelo(posicao[0],posicao[1])
    #print(quadradosHolderArray)
    clock.tick(50)

pygame.display.quit()