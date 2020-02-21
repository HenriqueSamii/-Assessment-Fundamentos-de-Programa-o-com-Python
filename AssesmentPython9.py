#Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas,
#  ele movimente o círculo com o texto “clique” nas direções corretas. Caso colida com algum retângulo, o retângulo que participou da colisão deve desaparecer.
import pygame,random,math

larguraTela = 800
alturaTela = 600

tela  = pygame.display.set_mode([larguraTela,alturaTela])

pygame.font.init()
myfont = pygame.font.SysFont(None, 30)

pygame.mixer.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RANDOM_COLLOR = (random.randint(50, 250),random.randint(50, 250),random.randint(50, 250))

###### Quadrado Func ####

tamanho = 50

def criar_quadrado(posicao):
    pygame.draw.rect(tela, RANDOM_COLLOR,posicao)

#########################

##### circulo Func ######

reaioCirculo = 50
posicaoInicialCirculoX = larguraTela//2
posicaoInicialCirculoY = reaioCirculo

movimentoCirculo = 5

textsurface = myfont.render('Clique',False, BLACK)

def criar_circulo(X = posicaoInicialCirculoX,Y = posicaoInicialCirculoY):
    pygame.draw.circle(tela,WHITE,[X,Y],reaioCirculo)
    tela.blit(textsurface,[X-30,Y-10])

#########################

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            if posX >= posicaoInicialCirculoX-reaioCirculo and posX <= posicaoInicialCirculoX+reaioCirculo and posY >= posicaoInicialCirculoY-reaioCirculo and posY <= posicaoInicialCirculoY+reaioCirculo:
                if math.sqrt((posicaoInicialCirculoX-posX)**2+(posicaoInicialCirculoY-posY)**2) <= reaioCirculo and math.sqrt((posicaoInicialCirculoX-posX)**2+(posicaoInicialCirculoY-posY)**2) >= reaioCirculo*-1 :
                    newRect = pygame.Rect(random.randint(0, larguraTela-tamanho), random.randint(0, alturaTela-tamanho), tamanho, tamanho)
                    colizao = False
                    for oldRect in quadradosHolderArray:
                        if newRect.colliderect(oldRect):
                            quadradosHolderArray.remove(oldRect)
                            colizao = True
                    if not colizao:
                        quadradosHolderArray.append(newRect)
            for quadrado in quadradosHolderArray:
                for x in range(quadrado[0], quadrado[0]+tamanho+1):
                    for y in range(quadrado[1], quadrado[1]+tamanho+1):
                        if x >= posicaoInicialCirculoX-reaioCirculo and x <= posicaoInicialCirculoX+reaioCirculo and y >= posicaoInicialCirculoY-reaioCirculo and y <= posicaoInicialCirculoY+reaioCirculo:
                            if  quadrado in quadradosHolderArray:
                                quadradosHolderArray.remove(quadrado)
                                print("Novo quadrado tocou em botao")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if posicaoInicialCirculoY < alturaTela-reaioCirculo:
                    posicaoInicialCirculoY += movimentoCirculo
                    #print("moveu s")
            elif event.key == pygame.K_w:
                if posicaoInicialCirculoY > reaioCirculo:
                    posicaoInicialCirculoY -= movimentoCirculo
                    #print("moveu w")
            elif event.key == pygame.K_d:
                if posicaoInicialCirculoX < larguraTela-reaioCirculo:
                    posicaoInicialCirculoX += movimentoCirculo
            elif event.key == pygame.K_a:
                if posicaoInicialCirculoX > reaioCirculo:
                    posicaoInicialCirculoX -= movimentoCirculo
            for quadrado in quadradosHolderArray:
                for x in range(quadrado[0], quadrado[0]+tamanho+1):
                    for y in range(quadrado[1], quadrado[1]+tamanho+1):
                        if x >= posicaoInicialCirculoX-reaioCirculo and x <= posicaoInicialCirculoX+reaioCirculo and y >= posicaoInicialCirculoY-reaioCirculo and y <= posicaoInicialCirculoY+reaioCirculo:
                            if  quadrado in quadradosHolderArray:
                                quadradosHolderArray.remove(quadrado)
                                print("quadrado tocou em botao em movimento")
    
    for posicao in quadradosHolderArray:
        criar_quadrado(posicao)
        
    criar_circulo(posicaoInicialCirculoX,posicaoInicialCirculoY)

    clock.tick(50)
#######################

pygame.display.quit()