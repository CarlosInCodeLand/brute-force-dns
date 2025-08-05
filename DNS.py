import socket
import sys

if len(sys.argv) == 3:
    dominio = sys.argv[1]
    wordlist = sys.argv[2]
    with open(wordlist, 'r') as arquivo:
        bruteforce = arquivo.read().splitlines()
    for nome in bruteforce:
        DNS = nome + "." + dominio
        try:
            print(DNS + ': ' + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass
else:
    print('Modo de uso: python DNS.py <wordlist> <wordlist>')