import pygame
import SoundInputUtils
from pygame import rect

# Websites used:
# https://www.youtube.com/watch?v=abH2MSBdnWc
# https://www.youtube.com/watch?v=hrQU6zw1vIg&list=PLnqEPPFiEkRfapYiYlfD2pyIYGLyVY2WL&index=8

# Getting a background image
# Make sure image is the same width and height specified by pygame.display.set_mode()


# Clock (frames per second)
clock = pygame.time.Clock();

# Initialize the pygame
pygame.init()

# create the screen (width, height)
screen = pygame.display.set_mode((800, 640))

# Tile and Icon for game window
pygame.display.set_caption("Dino Run")
icon = pygame.image.load('base_images/001-dinosaur.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("Layers/4-BackgroundFar.png").convert_alpha()
background1 = pygame.image.load("Layers/3-BackgroundClose.png").convert_alpha()
background2 = pygame.image.load("Layers/5-Clouds.png").convert_alpha()
background3 = pygame.image.load("Layers/6-Sky.png").convert_alpha()
background4 = pygame.image.load("Layers/2-PlayerLayer.png").convert_alpha()
background5 = pygame.image.load("Layers/1-Foreground.png").convert_alpha()

# Scale down images
backW = 1920
backH = 640
background = pygame.transform.scale(background, (backW,backH))
background1 = pygame.transform.scale(background1, (backW,backH))
background2 = pygame.transform.scale(background2, (backW,backH))
background3 = pygame.transform.scale(background3, (backW,backH))
background4 = pygame.transform.scale(background4, (backW,backH))
background5 = pygame.transform.scale(background5, (backW,backH))

# Starting positions for all background layers
backX = 0
backY = 0
backVel = 0
backLayerX = 0
backLayerY = 0
backLayerVel = 0
backFgX = 0
backFgY = 0
backFgVel = 0
bgFarSpd = 0
bgCloseSpd = 0
cloudSpd = 0
skySpd = 0
playerLayerSpd = 0 
foregroundSpd = 0
l0 = 0
l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0

# Load cactus images
cactiW = 115
cactiH = 115
c1 = pygame.transform.scale(pygame.image.load("Cacti/cactus1.png").convert_alpha(), (cactiW, cactiH))
c2 = pygame.transform.scale(pygame.image.load("Cacti/cactus2.png").convert_alpha(), (cactiW, cactiH))
c3 = pygame.transform.scale(pygame.image.load("Cacti/cactus3.png").convert_alpha(), (cactiW, cactiH))
c4 = pygame.transform.scale(pygame.image.load("Cacti/cactus4.png").convert_alpha(), (cactiW, cactiH))
c5 = pygame.transform.scale(pygame.image.load("Cacti/cactus5.png").convert_alpha(), (cactiW, cactiH))
c6 = pygame.transform.scale(pygame.image.load("Cacti/cactus1.png").convert_alpha(), (cactiW, cactiH))
c7 = pygame.transform.scale(pygame.image.load("Cacti/cactus2.png").convert_alpha(), (cactiW, cactiH))
c8 = pygame.transform.scale(pygame.image.load("Cacti/cactus3.png").convert_alpha(), (cactiW, cactiH))
c9 = pygame.transform.scale(pygame.image.load("Cacti/cactus4.png").convert_alpha(), (cactiW, cactiH))
c10 = pygame.transform.scale(pygame.image.load("Cacti/cactus5.png").convert_alpha(), (cactiW, cactiH))
c11 = pygame.transform.scale(pygame.image.load("Cacti/cactus1.png").convert_alpha(), (cactiW, cactiH))
c12 = pygame.transform.scale(pygame.image.load("Cacti/cactus2.png").convert_alpha(), (cactiW, cactiH))
c13 = pygame.transform.scale(pygame.image.load("Cacti/cactus3.png").convert_alpha(), (cactiW, cactiH))
c14 = pygame.transform.scale(pygame.image.load("Cacti/cactus4.png").convert_alpha(), (cactiW, cactiH))
c15 = pygame.transform.scale(pygame.image.load("Cacti/cactus5.png").convert_alpha(), (cactiW, cactiH))

# Cacti positioning
cy = 460
cactusVel = 0
# obstacle 1
c1x = 600
# obstacle 2
c2x = 1000
c3x = 1025
# obstacle 3
c4x = 1425
c5x = 1400
# obstacle 4
c10x = 1800
# obstacle 5
c7x = 2200
c9x = 2225
# obstacle 6
c6x = 2600
# obstacle 7
c8x = 3000
# obstacle 8
c13x = 3400
c15x = 3425
# obstacle 9
c12x = 3800
c14x = 3820

# Player
playerX = 10
playerY = 415
playerX_change = 0
playerY_change = 0

# PlayerAnimation
dinoW = 175
dinoH = 175
d1 = pygame.transform.scale(pygame.image.load("Dino/dino1.png").convert_alpha(), (dinoW,dinoH))
d2 = pygame.transform.scale(pygame.image.load("Dino/dino2.png").convert_alpha(), (dinoW,dinoH))
d3 = pygame.transform.scale(pygame.image.load("Dino/dino3.png").convert_alpha(), (dinoW,dinoH))
d4 = pygame.transform.scale(pygame.image.load("Dino/dino4.png").convert_alpha(), (dinoW,dinoH))
d5 = pygame.transform.scale(pygame.image.load("Dino/dino5.png").convert_alpha(), (dinoW,dinoH))
d6 = pygame.transform.scale(pygame.image.load("Dino/dino6.png").convert_alpha(), (dinoW,dinoH))
d7 = pygame.transform.scale(pygame.image.load("Dino/dino7.png").convert_alpha(), (dinoW,dinoH))
d8 = pygame.transform.scale(pygame.image.load("Dino/dino8.png").convert_alpha(), (dinoW,dinoH))
dinoRun = [d1, d2, d3, d4, d5, d6, d7, d8]
runCount = 0

# Score
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_textX = 10
textX = 10
textY = 10
score_textY = 10
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
game_over_textX = 210
game_over_textY = 250



# Jumping
isJump = False
jumpCount = 10
jumpKeyboardControl = True

# Keep track of if the user is holding the click button (for button functionality)
currentlyHoldingClick = False

# Mic Utilities
MicInputUtils = SoundInputUtils.SoundInputUtils()


# Collision
collided = False
def collides(rect1, rect2, collision):
    if rect1.colliderect(rect2):
        collision = True
    return collision

# show score on screen
def show_score(x, y):
    score = score_font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

# show game over on screen
def game_over_text():
    score = game_over_font.render("Game Over", True, (0, 0, 0))
    screen.blit(score, (game_over_textX, game_over_textY))
def show_jumpControl(x,y):
    global jumpKeyboardControl
    jumpControlFont = pygame.font.Font('freesansbold.ttf',20)
    if jumpKeyboardControl == True:
        message = "Keyboard"
    else:
        message = "Mic Input"
    JumpControlText = jumpControlFont.render("Jump control: " + message, True, (0,0,0))
    screen.blit(JumpControlText, (x,y))

def changeJumpControl():
    global jumpKeyboardControl
    if jumpKeyboardControl == True:
        jumpKeyboardControl = False
        # Start recieving input from the mic
        MicInputUtils.openStream()
    else:
        jumpKeyboardControl = True
        # Stop recieving input from the mic
        MicInputUtils.closeStream()

def button(msg,x,y,w,h,ic,ac, action=None):
    global currentlyHoldingClick
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if currentlyHoldingClick == True and click[0] == 0: currentlyHoldingClick=False
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and currentlyHoldingClick==False and action !=None:
            currentlyHoldingClick = True
            action()
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf',17)
    textSurf = smallText.render(msg, True, (0,0,0))
    textRect = textSurf.get_rect()
    textRect.center = (x+int(w/2), y+int(h/2))
    screen.blit(textSurf, textRect)

def show_buttons():
    copperRed = (195, 124, 77)
    lightTan = (235, 204, 171)
    jumpControlBtn = button("Change Jump Control",550,10,200,50,copperRed, lightTan,changeJumpControl)

# player positioning and animation
def player(x, y, speed):
    global runCount
    
    if runCount == 16:
        runCount = 0
    screen.blit(dinoRun[int(runCount//2)], (int(x), int(y)))   # divide by 2 so that animation is a little slower
    if isJump == False:
        runCount += 1


# Game loop
running = True
while running:
    pygame.time.delay(25)
    # RGB values for screen
    screen.fill((0, 0, 0))
    # Background image (parallax effect)
    if backX == -1920:
        backX = 0
    if backLayerX == -1920:
        backLayerX = 0
    if backFgX == -1920:
        backFgX = 0
    if c1x == -3240:
        c1x = 600
    if c2x == -2840:
        c2x = 1000
    if c3x == -2815:
        c3x = 1025
    if c4x == -2415:
        c4x = 1425
    if c5x == -2440:
        c5x = 1400
    if c10x == -2040:
        c10x = 1800
    if c7x == -1640:
        c7x = 2200
    if c9x == -1615:
        c9x = 2225
    if c6x == -1240:
        c6x = 2600
    if c8x == -840:
        c8x = 3000
    if c13x == -440:
        c13x = 3400
    if c15x == -415:
        c15x = 3425
    if c12x == -40:
        c12x = 3800
    if c14x == -20:
        c14x = 3820
    if l0 == -1920:
        l0 = 0
    if l1 == -1920:
        l1 = 0
    if l2 == -1920:
        l2 = 0
    if l3 == -1920:
        l3 = 0
    if l4 == -1920:
        l4 = 0
    if l5 == -1920:
        l5 = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    # start jumping motion
    if not isJump:
        if jumpKeyboardControl:
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            # Listen to the mic input
            MicInputUtils.listen()
            # Determine if sound was made
            if MicInputUtils.madeSound():
                isJump = True
        # add animation code?
    else:
        if jumpCount >= -10:
            playerY -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False


    # Incorporate background movement
    backX += backVel
    backLayerX += backLayerVel
    c1x += cactusVel
    c2x += cactusVel
    c3x += cactusVel
    c4x += cactusVel
    c5x += cactusVel
    c6x += cactusVel
    c7x += cactusVel
    c8x += cactusVel
    c9x += cactusVel
    c10x += cactusVel
    c12x += cactusVel
    c13x += cactusVel
    c14x += cactusVel
    c15x += cactusVel
    backFgX += backFgVel
    l0 += bgFarSpd
    l1 += bgCloseSpd
    l2 += cloudSpd
    l3 += skySpd
    l4 += playerLayerSpd
    l5 += foregroundSpd

# Show background to screen
    screen.blit(background3, (l3, backY))
    screen.blit(background3, (l3 + 1920, backY))
    screen.blit(background, (l0, backY))
    screen.blit(background, (l0 + 1920, backY))
    screen.blit(background1, (l1, backY))
    screen.blit(background1, (l1 + 1920, backY))
    screen.blit(background4, (l4, backLayerY))
    screen.blit(background4, (l4 + 1920, backLayerY))
    screen.blit(background2, (l2, backY))
    screen.blit(background2, (l2 + 1920, backY))

# create rectangles to use for collision
    screen.blit(c1, (c1x, cy))
    c1_rect = pygame.Rect(c1x + 30, cy + 25, c1.get_width() - 60, c1.get_height() - 25)
    # pygame.draw.rect(screen,(0,0,0), c1_rect, 4)

    screen.blit(c2, (c2x, cy))
    screen.blit(c3, (c3x, cy))
    c2_rect = pygame.Rect(c2x + 40, cy + 35, c2.get_width() - 60, c2.get_height() - 35)
    # pygame.draw.rect(screen, (0, 0, 0), c2_rect, 4)

    screen.blit(c4, (c4x, cy))
    screen.blit(c5, (c5x, cy))
    c4_rect = pygame.Rect(c4x + 20, cy + 30, c4.get_width() - 70, c4.get_height() - 30)
    # pygame.draw.rect(screen, (0, 0, 0), c4_rect, 4)

    screen.blit(c6, (c6x, cy))
    c6_rect = pygame.Rect(c6x + 40, cy + 30, c6.get_width() - 80, c6.get_height() - 30)
    # pygame.draw.rect(screen, (0, 0, 0), c6_rect, 4)

    screen.blit(c7, (c7x, cy))
    screen.blit(c9, (c9x, cy))
    c7_rect = pygame.Rect(c7x + 40, cy + 45, c7.get_width() - 60, c7.get_height() - 45)
    # pygame.draw.rect(screen, (0, 0, 0), c7_rect, 4)

    screen.blit(c8, (c8x, cy))
    c8_rect = pygame.Rect(c8x + 40, cy + 30, c8.get_width() - 80, c8.get_height() - 30)
    # pygame.draw.rect(screen, (0, 0, 0), c8_rect, 4)

    screen.blit(c10, (c10x, cy))
    c10_rect = pygame.Rect(c10x + 40, cy + 30, c10.get_width() - 80, c10.get_height() - 30)
    # pygame.draw.rect(screen, (0, 0, 0), c10_rect, 4)

    screen.blit(c12, (c12x, cy))
    screen.blit(c14, (c14x, cy))
    c12_rect = pygame.Rect(c12x + 40, cy + 45, c12.get_width() - 60, c12.get_height() - 45)
    # pygame.draw.rect(screen, (0, 0, 0), c12_rect, 4)

    screen.blit(c13, (c13x, cy))
    screen.blit(c15, (c15x, cy))
    c13_rect = pygame.Rect(c13x + 40, cy + 30, c13.get_width() - 60, c13.get_height() - 30)
    # pygame.draw.rect(screen, (0, 0, 0), c13_rect, 4)

# display cacti to screen
    screen.blit(c1, (c1x + 3840,cy))
    screen.blit(c2, (c2x + 3840,cy))
    screen.blit(c3, (c3x + 3840,cy))
    screen.blit(c4, (c4x + 3840,cy))
    screen.blit(c5, (c5x + 3840,cy))
    screen.blit(c6, (c6x + 3840, cy))
    screen.blit(c7, (c7x + 3840, cy))
    screen.blit(c8, (c8x + 3840, cy))
    screen.blit(c9, (c9x + 3840, cy))
    screen.blit(c10, (c10x + 3840, cy))
    screen.blit(c12, (c12x + 3840, cy))
    screen.blit(c13, (c13x + 3840, cy))
    screen.blit(c14, (c14x + 3840, cy))
    screen.blit(c15, (c15x + 3840, cy))

    # check for collisions
    player_rect = pygame.Rect(playerX + 60, playerY + 50, d1.get_width() -90, d1.get_height() - 110)
    rectList = [c1_rect, c2_rect, c4_rect, c6_rect, c7_rect, c8_rect, c10_rect,c12_rect, c13_rect]
    for i in rectList:
        collided = collides(player_rect, i, collided)

    if not collided:
        player(playerX, playerY, 2)
        backVel = -4
        backLayerVel = -12
        cactusVel = -12
        backFgVel = -16
        bgFarSpd = -2
        bgCloseSpd = -4
        cloudSpd = -3
        skySpd = -4
        playerLayerSpd = -12
        foregroundSpd = -16
        score_value = score_value + 1

    # stop game if collided
    if collided:
        player(playerX,playerY, 100)
        game_over_text()
        backVel = 0
        backLayerVel = 0
        cactusVel = 0
        backFgVel = 0
        bgFarSpd = 0
        bgCloseSpd = 0
        cloudSpd = 0
        skySpd = 0
        playerLayerSpd = 0 
        foregroundSpd = 0

    screen.blit(background5, (l5, backLayerY))
    screen.blit(background5, (l5 + 1920, backLayerY))

    # Show score
    show_score(textX, textY)

    # Show buttons
    show_buttons()

    # Show what is controlling the jump
    show_jumpControl(textX, textY+30)
    
    pygame.display.update()

    # clock.tick(60)
