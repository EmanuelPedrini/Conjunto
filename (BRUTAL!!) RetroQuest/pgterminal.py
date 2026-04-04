import pygame
import sys
import builtins

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RetroQuest")

font = pygame.font.SysFont("consolas", 20)
clock = pygame.time.Clock()

lines = []
current_input = ""

def tick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def draw():
    tick()
    screen.fill((0, 0, 0))

    y = 10
    for line in lines[-28:]:
        text = font.render(line, True, (255,255,255))
        screen.blit(text, (10, y))
        y += 22

    input_text = font.render("> " + current_input, True, (0,255,0))
    screen.blit(input_text, (10, HEIGHT - 30))

    pygame.display.flip()
    clock.tick(60)


def print(*args, sep=" ", end="\n"):
    text = sep.join(str(a) for a in args) + end
    lines.append(text.rstrip("\n"))
    draw()
    builtins.print(*args, sep=sep, end=end)


def input(prompt=""):
    global current_input

    if prompt:
        lines.append(prompt)

    current_input = ""

    while True:
        tick()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    value = current_input
                    lines.append("> " + current_input)
                    current_input = ""
                    draw()
                    return value

                elif event.key == pygame.K_BACKSPACE:
                    current_input = current_input[:-1]

                else:
                    current_input += event.unicode

        draw()