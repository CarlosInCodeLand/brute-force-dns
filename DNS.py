import socket

dominio = input("alvo: ")
brute = ["ns1", "ns2", "ns3", "ns4", "www", "ftp", "mail", "intranet"]

for nome in brute:
    DNS = nome + "." + dominio
    try:
        print(DNS + ': ' + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass