import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


pygame.init()
# define variables for game

#size of our window

screen_width=400
screen_height=400

size = (screen_width,screen_height)
#distance from the edge of the window
screen = pygame.display.set_mode(size)
#name of the game
pygame.display.set_caption("pong game")
PADDLE_BUFFER = 10

done = False

#size of our paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50

#size our ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

ballXpos = screen_width / 2
paddle1Ypos = 200
paddle2Ypos = 200
#speed of our paddle & ball
PADDLE1_SPEED = 0.2
BALL_X_SPEED = 3/10
BALL_Y_SPEED = 2

WHITE = (255,255,255)
BLACK = (0,0,0)

direction = 0

#initialize our screen

def green():
    pygame.draw.rect(screen, GREEN, [100, 100, 20, 25])



def drawBall(ballXpos, ballYpos):
    ball = pygame.Rect(ballXpos,ballYpos,10,10)
    #print ball
    pygame.draw.rect(screen,WHITE,ball)


def drawPaddle1(paddle1Ypos):
                paddle1 = pygame.Rect(PADDLE_BUFFER, paddle1Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
                pygame.draw.rect(screen,WHITE,paddle1)

print screen_width - PADDLE_BUFFER - PADDLE_WIDTH

def drawPaddle2(paddle2Ypos):
                 paddle2 = pygame.Rect(screen_width - PADDLE_BUFFER - PADDLE_WIDTH, paddle2Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
                 pygame.draw.rect(screen,WHITE,paddle2)



def updateBall(ballYpos):
    ballYpos += 0.25
    return ballYpos


def updatePaddle1():
    return 1



while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    #green()
    drawBall(ballXpos,25)
    #ballXpos += 0.25
    #print ballXpos
    # draw paddle one
    drawPaddle1(paddle1Ypos)
    #print paddle1Ypos
   

    if direction == 0:
        paddle1Ypos -= PADDLE1_SPEED
    if direction == 1:
        paddle1Ypos += PADDLE1_SPEED

    # hit detection when x <= 0
    if  paddle1Ypos <= 0:
        paddle1Ypos = 0


    if (screen_height - paddle1Ypos  < PADDLE_HEIGHT):
        paddle1Ypos = screen_height -  PADDLE_HEIGHT
        direction = 0


    #ball = pygame.Rect(ballXpos,0,10,10)
    #print ball
    #pygame.draw.rect(screen,WHITE,ball)
    ballXpos += 0.2
        
    print screen_height - PADDLE_HEIGHT    
    print screen_height - PADDLE_HEIGHT < PADDLE_HEIGHT
   
        
        
  
        
        
 
        
        
    # draw paddle two
    drawPaddle2(paddle2Ypos)
    pygame.display.flip()
    #paddle2Ypos += 0.05

    if direction == 0:
        paddle2Ypos -= PADDLE1_SPEED
    if direction == 1:
        paddle2Ypos += PADDLE1_SPEED

    if (paddle2Ypos) <= 0:
        paddle2Ypos = 0
        direction = 1
        

    if (screen_height - paddle2Ypos  < PADDLE_HEIGHT):
        paddle2Ypos = screen_height -  PADDLE_HEIGHT
        direction = 0
        


        



pygame.quit()

      
