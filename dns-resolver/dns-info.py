import dns.resolver
import colorama

DOMINIO = 'google.com'

def ip():
    try:
        resposta = dns.resolver.resolve(DOMINIO, 'A')
        for ip in resposta:
            print(f'IP: {ip.to_text()}')
            ip_alvo = ip.to_text()
            return ip_alvo
    except:
        pass

def cname():
    try:
        resposta = dns.resolver.resolve(DOMINIO, 'CNAME')
        for name in resposta:
            print(f'CNAME: {name.target}')
            name_alvo = name.target
            return name
    except:
        pass

def ipv6():
    try:
        resposta = dns.resolver.resolve(DOMINIO, 'AAAA')
        for ipvs in resposta:
            print(f'IPv6: {ipvs.to_text()}')
            ipvseis = ipvs.to_text()
            return ipvseis
    except:
        pass

ipv6()