# brute-force-dns

Ferramentas para brute force e reconhecimento de subdomínios DNS.

## Estrutura da pasta

- `dns-brute-force.py`: Script em Python para brute force de subdomínios usando uma wordlist.
- `dns_scan.sh`: Script em Bash para varredura de subdomínios via ping.
- `common-dns-name.txt`: Wordlist de subdomínios comuns para uso nos scripts.
- `requirements.txt`: Dependências Python necessárias para rodar o script principal.
- `brute/`: Ambiente virtual Python (opcional, pode ser ignorado se não for usar o venv).

## Requisitos

- Python 3.x
- [colorama](https://pypi.org/project/colorama/) (instale com `pip install -r requirements.txt`)
- Bash (para rodar o script shell)

## Como usar

### Python (`dns-brute-force.py`)

```bash
python dns-brute-force.py <dominio> <wordlist>
```

- `<dominio>`: O domínio alvo (ex: exemplo.com)
- `<wordlist>`: Caminho para a wordlist de subdomínios (ex: common-dns-name.txt)

Exemplo:
```bash
python dns-brute-force.py exemplo.com common-dns-name.txt
```

### Bash (`dns_scan.sh`)

```bash
chmod +x dns_scan.sh
./dns_scan.sh common-dns-name.txt
```
O script solicitará o domínio alvo e fará a varredura via ping.

## Observações

- O script Python destaca subdomínios encontrados em cores.
- O script Bash mostra progresso a cada 50 subdomínios testados.
- Certifique-se de ter permissão para testar o domínio alvo.

---

Projeto para fins educacionais e experimentação. 