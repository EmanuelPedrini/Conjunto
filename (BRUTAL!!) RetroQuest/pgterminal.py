import pygame
import sys
import builtins

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Music/music1.mp3")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("RetroQuest")

font = pygame.font.SysFont("consolas", 20)
clock = pygame.time.Clock()

lines = []
current_input = ""
scroll_offset = 0
fullscreen = False


class Stdout:
    def write(self, text):
        global scroll_offset
        if text.strip() != "":
            lines.append(text.rstrip("\n"))
            scroll_offset = 0
        draw()

    def flush(self):
        pass


def draw():
    screen.fill((0, 0, 0))

    width, height = screen.get_size()

    line_height = 22
    input_area = 40

    max_lines = (height - input_area) // line_height

    start = max(0, len(lines) - max_lines - scroll_offset)
    end = start + max_lines

    y = 10
    for line in lines[start:end]:
        text = font.render(line, True, (255,255,255))
        screen.blit(text, (10, y))
        y += line_height

    pygame.draw.line(
        screen,
        (60, 60, 60),
        (0, height - input_area),
        (width, height - input_area)
    )

    input_text = font.render("> " + current_input, True, (0,255,0))
    screen.blit(input_text, (10, height - 30))

    pygame.display.flip()


def custom_input(prompt=""):
    global current_input, scroll_offset, screen, fullscreen

    if prompt:
        lines.append(prompt)

    current_input = ""

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE and not fullscreen:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)

            elif event.type == pygame.MOUSEWHEEL:
                # scroll invertido
                scroll_offset += event.y
                scroll_offset = max(0, min(scroll_offset, len(lines)))

            elif event.type == pygame.KEYDOWN:

                # fullscreen real
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen

                    if fullscreen:
                        screen = pygame.display.set_mode(
                            (0, 0),
                            pygame.FULLSCREEN
                        )
                    else:
                        screen = pygame.display.set_mode(
                            (WIDTH, HEIGHT),
                            pygame.RESIZABLE
                        )

                elif event.key == pygame.K_RETURN:
                    value = current_input
                    lines.append("> " + current_input)
                    current_input = ""
                    scroll_offset = 0
                    draw()
                    return value

                elif event.key == pygame.K_BACKSPACE:
                    current_input = current_input[:-1]

                else:
                    current_input += event.unicode

        draw()
        clock.tick(60)


sys.stdout = Stdout()
builtins.input = custom_input