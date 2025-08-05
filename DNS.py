import socket
import sys
from colorama import init, Fore, Back, Style

init(autoreset=True)

if len(sys.argv) == 3:
    dominio = sys.argv[1]
    wordlist = sys.argv[2]
    with open(wordlist, 'r') as arquivo:
        bruteforce = arquivo.read().splitlines()
        print(Fore.BLUE +"Iniciando varredura . . .")
    for nome in bruteforce:
        DNS = nome + "." + dominio
        try:
            print(f'{Fore.LIGHTBLUE_EX + "Dominio Encontrado >>>> "}{Fore.GREEN +DNS + ": " + Fore.LIGHTGREEN_EX + Style.BRIGHT + socket.gethostbyname(DNS)}')
        except socket.gaierror:
            pass
else:
    print(Fore.RED + 'Modo de uso: python DNS.py <wordlist> <wordlist>')