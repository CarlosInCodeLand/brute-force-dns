import dns.resolver
import dns.reversename
import colorama
import sys

colorama.init(autoreset=True)

def ip(dominio):
    try:
        resposta = dns.resolver.resolve(dominio, 'A')
        return [ip.to_text() for ip in resposta]
    except Exception as e:
        print(colorama.Fore.RED + f"[Erro IP] {e}")
        return []

def cname(dominio):
    try:
        resposta = dns.resolver.resolve(dominio, 'CNAME')
        return [rdata.target.to_text() for rdata in resposta]
    except Exception as e:
        print(colorama.Fore.YELLOW + f"[Aviso CNAME] {e}")
        return []

def ipv6(dominio):
    try:
        resposta = dns.resolver.resolve(dominio, 'AAAA')
        return [rdata.to_text() for rdata in resposta]
    except Exception as e:
        print(colorama.Fore.YELLOW + f"[Aviso IPv6] {e}")
        return[]

def ptr(ip_alvo):
    try:
        reverso = dns.reversename.from_address(ip_alvo)
        resposta = dns.resolver.resolve(reverso, 'PTR')
        return [ptrval.to_text() for ptrval in resposta]
    except Exception as e:
        print(colorama.Fore.YELLOW + f"[Aviso PTR] {e}")
        return []

if __name__ == "__main__":

    if len(sys.argv) == 2:
        
        dominio = sys.argv[1]
        ips = ip(dominio)
        cnames = cname(dominio)
        ipv6s = ipv6(dominio)

        if ips:
            for ip in ips:
                print(colorama.Fore.GREEN + f"IP: {ip}")
                ptrss = ptr(ip)
                if ptrss:
                    for ptrs in ptrss:
                        print(colorama.Fore.CYAN + f"PTR: {ptrs}")
        else:
            print(colorama.Fore.REd + "Nenhum IP encontrado")

        if ipv6s:
            for ipv6 in ipv6s:
                print(colorama.Fore.GREEN + f"IPv6: {ipv6}")
        else:
            print(colorama.Fore.RED + "Nenhum IPv6 encontrado")

        if cnames:
            for cname in cnames:
                print(colorama.Fore.GREEN + f"CNAME: {cname}")
        else:
            print(colorama.Fore.RED + "Nenhum cname encontrado")

    else:
        print(colorama.Fore.BLUE + """
=====================================
==============DNS INFO===============
=============MODO DE USO=============
======python3 dns-info <DOMINIO>=====
=====================================
""")