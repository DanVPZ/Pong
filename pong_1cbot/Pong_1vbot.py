import pygame
import random
import sys
import time


def end_game(status):

    screen.fill(bg_color)
    screen.blit(status, (screen_width / 2 - 195, screen_height / 2 - 65))
    pygame.display.update()
    clock.tick(10)
    time.sleep(5)
    sys.exit()

def score_check():
    
    if player_score == 3:
        end_game(winner_text)
    elif opponent_score == 3:
        end_game(loser_text)

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    if ball.top > screen_height - 30 or ball.top < 0:
        ball_speed_y *= -1
    elif ball.right > screen_width - 0:
        ball_speed_x = 5
        ball_speed_y = 5
        ball_restart()
        opponent_score += 1
    elif ball.left < 0:
        ball_speed_x = 5
        ball_speed_y = 5
        ball_restart()
        player_score += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        while abs(ball_speed_x) < 15:
            ball_speed_x *= 1.07
            ball_speed_y *= 1.07
            break


def opponent_animation():
    global opponent_speed
    while ball.x < screen_width / 2 + 150:
        if ball.y - 70 > opponent.y - 15:
            opponent_speed = 5.8
        else:
            opponent_speed = -5.8
        break
    

def player_animation():
    global win_color, lose_color, light_grey, player_color, opponent_color
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    elif player.bottom >= screen_height:
        player.bottom = screen_height
    
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    elif opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    if player_score > opponent_score:
        player_color = win_color
        opponent_color = lose_color
    elif player_score < opponent_score:
        player_color = lose_color
        opponent_color = win_color
    else:
        player_color = light_grey
        opponent_color = light_grey


def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))


pygame.init()
clock = pygame.time.Clock()

screen_width = 1050
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Score
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)
big_font = pygame.font.Font('freesansbold.ttf', 80)

# Colors
bg_color = pygame.Color('grey12')
light_grey = (220, 220, 220)
win_color = pygame.Color("green")
lose_color = pygame.Color("red")
player_color = light_grey
opponent_color = light_grey

winner_text = big_font.render("Has ganado :D", False, light_grey)
loser_text = big_font.render("Has perdido :(", True, light_grey)

# Game variables
ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
opponent_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Animacion y Colisiones
    ball_animation()
    opponent_animation()
    player_animation()
    player.y += player_speed
    opponent.y += opponent_speed

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, opponent_color, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    player_text = basic_font.render(f'{player_score}', False, player_color)
    screen.blit(player_text, (560, 25))

    opponent_text = basic_font.render(f'{opponent_score}', False, opponent_color)
    screen.blit(opponent_text, (475, 25))

    score_check()

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
