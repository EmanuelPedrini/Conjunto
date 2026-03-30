from colorama import Fore, Style, init
init()

def rainbow(text):
    cores = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE,
        Fore.MAGENTA
    ]

    resultado = ""
    for i, letra in enumerate(text):
        resultado += cores[i % len(cores)] + letra

    return resultado + Style.RESET_ALL

import time

def red(text):
    return Fore.RED + text + Style.RESET_ALL

def green(text):
    return Fore.GREEN + text + Style.RESET_ALL

def yellow(text):
    return Fore.YELLOW + text + Style.RESET_ALL

def blue(text):
    return Fore.BLUE + text + Style.RESET_ALL

def magenta(text):
    return Fore.MAGENTA + text + Style.RESET_ALL

def cyan(text):
    return Fore.CYAN + text + Style.RESET_ALL

def white(text):
    return Fore.WHITE + text + Style.RESET_ALL

def black(text):
    return Fore.BLACK + text + Style.RESET_ALL

def light_red(text):
    return Fore.LIGHTRED_EX + text + Style.RESET_ALL

def light_green(text):
    return Fore.LIGHTGREEN_EX + text + Style.RESET_ALL

def light_yellow(text):
    return Fore.LIGHTYELLOW_EX + text + Style.RESET_ALL

def light_blue(text):
    return Fore.LIGHTBLUE_EX + text + Style.RESET_ALL

def light_magenta(text):
    return Fore.LIGHTMAGENTA_EX + text + Style.RESET_ALL

def light_cyan(text):
    return Fore.LIGHTCYAN_EX + text + Style.RESET_ALL

def pink(text):
    return Fore.LIGHTMAGENTA_EX + text + Style.RESET_ALL