import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RetroQuest")

font = pygame.font.SysFont("consolas", 20)
clock = pygame.time.Clock()

lines = []
current_input = ""


class Stdout:
    def write(self, text):
        if text.strip() != "":
            lines.append(text.rstrip("\n"))
        draw()

    def flush(self):
        pass


def draw():
    screen.fill((0, 0, 0))

    y = 10
    for line in lines[-28:]:
        text = font.render(line, True, (255,255,255))
        screen.blit(text, (10, y))
        y += 22

    input_text = font.render("> " + current_input, True, (0,255,0))
    screen.blit(input_text, (10, HEIGHT - 30))

    pygame.display.flip()


def input(prompt=""):
    global current_input

    if prompt:
        lines.append(prompt)

    current_input = ""

    while True:
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
        clock.tick(60)


sys.stdout = Stdout()