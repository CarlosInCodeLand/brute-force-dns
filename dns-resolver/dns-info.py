import dns.resolver
import dns.reversename
import colorama

DOMINIO = 'google.com'

def ip(dominio):
    try:
        resposta = dns.resolver.resolve(dominio, 'A')
        return [ip.to_text() for ip in resposta]
    except Exception as e:
        print(f"[Erro IP] {e}")
        return []

def cname(dominio):
    try:
        resposta = dns.resolver.resolve(dominio, 'CNAME')
        return [rdata.target.to_text() for rdata in resposta]
    except Exception as e:
        print(f"[Erro CNAME] {e}")
        return []

def ipv6(dominio):
    try:
        resposta = dns.resolver.resolve(dominio, 'AAAA')
        return [rdata.to_text() for rdata in resposta]
    except Exception as e:
        print(f"[Erro PTR] {e}")
        return[]

def ptr(dominio):
    try:
        ip_alvo = ip(dominio)[0]
        reverso = dns.reversename.from_address(ip_alvo)
        resposta = dns.resolver.resolve(reverso, 'PTR')
        return [ptrval.to_text() for ptrval in resposta]
    except Exception as e:
        print(f"[Erro PTR] {e}")
        return []


