import socket
import sys

if len(sys.argv) == 2:
    dominio = sys.argv[1]
    brute = ["ns1", "ns2", "ns3", "ns4", "www", "ftp", "mail", "intranet"]

    for nome in brute:
        DNS = nome + "." + dominio
        try:
            print(DNS + ': ' + socket.gethostbyname(DNS))
        except socket.gaierror:
            pass
else:
    print('Modo de uso: python DNS.py <dominio>')