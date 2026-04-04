import pygame
import sys
import builtins
import time
PRINT_DELAY = 0.2

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Music/music2.mp3")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("KIMERAHALLA")

font = pygame.font.Font("Fonts/font2.ttf", 20)
clock = pygame.time.Clock()

lines = []
current_input = ""
scroll_offset = 0
fullscreen = False

# área da imagem
image_surface = None
IMAGE_HEIGHT = 300


class Stdout:
    def write(self, text):
        global scroll_offset
        if text.strip() != "":
            lines.append(text.rstrip("\n"))
            scroll_offset = 0
        draw()
        time.sleep(PRINT_DELAY)

    def flush(self):
        pass


def draw():
    screen.fill((0, 0, 0))

    width, height = screen.get_size()

    # ---------- IMAGEM SUPERIOR ----------
    if image_surface:
        img = pygame.transform.scale(image_surface, (width, IMAGE_HEIGHT))
        screen.blit(img, (0, 0))

    pygame.draw.line(
        screen,
        (80,80,80),
        (0, IMAGE_HEIGHT),
        (width, IMAGE_HEIGHT)
    )

    # ---------- TERMINAL ----------
    line_height = 22
    input_area = 40

    usable_height = height - IMAGE_HEIGHT
    max_lines = (usable_height - input_area) // line_height

    start = max(0, len(lines) - max_lines - scroll_offset)
    end = start + max_lines

    y = IMAGE_HEIGHT + 10
    for line in lines[start:end]:
        text = font.render(line, False, (0,255,110))
        screen.blit(text, (10, y))
        y += line_height

    pygame.draw.line(
        screen,
        (60, 60, 60),
        (0, height - input_area),
        (width, height - input_area)
    )

    input_text = font.render("" + current_input, True, (255,255,255))
    screen.blit(input_text, (10, height - 30))

    pygame.display.flip()


def set_image(path):
    global image_surface
    image_surface = pygame.image.load(path).convert_alpha()
    draw()


def clear_image():
    global image_surface
    image_surface = None
    draw()


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
                    lines.append("" + current_input)
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