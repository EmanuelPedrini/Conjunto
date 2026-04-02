
globaldanger = 1
globaldangercalc = (0.5*(globaldanger + 1))
globaldangermathsoftcap= (1+(globaldanger*5/((globaldanger*5)+15)))
gamerunning = 1
bosscall = str("notcalled")
cents = 0
breeding = False

import time
import builtins

def slowprint(*args, sep=" ", end="\n", delay=0.02, line_delay=0.4, flush=True):
    text = sep.join(map(str, args)) + end
    
    for char in text:
        builtins._original_print(char, end="", flush=True)
        time.sleep(delay)
        
    time.sleep(line_delay)

# salva print original
builtins._original_print = builtins.print

# substitui globalmente
builtins.print = slowprint
