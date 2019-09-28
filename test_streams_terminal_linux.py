# python3 test_streams_terminal_linux.py 1> salida 2> error
# tail -f salida, tail -f error
# python3 test_streams_terminal_linux.py 1>> salida 2>> error
# python3 test_streams_terminal_linux.py > todo.log 2>&1

import time
import sys

def main():
    i = 1
    num = int(input('Escribe un número: '))
    while(True):
        if(i % num == 0):
            print(f'El {i} es múltiplo de {num}, todo cool', flush=True)
        else:
            print(f'NO!! ALARMA: El {i} NO es múltiplo de {num}', file=sys.stderr, flush=True)
        i += 1
        time.sleep(1)

if __name__ == "__main__":
    main()