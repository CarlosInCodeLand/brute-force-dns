# DNS Brute Force

Este projeto é um script simples em Python para realizar brute force de subdomínios em um domínio alvo, utilizando uma wordlist.

## Requisitos

- Python 3.11 ou superior
- [colorama](https://pypi.org/project/colorama/)

Você pode instalar as dependências usando o pip:

```bash
pip install colorama
```

## Como usar

Execute o script passando o domínio alvo e o caminho para a wordlist de subdomínios:

```bash
python DNS.py <dominio> <wordlist>
```

- `<dominio>`: O domínio que você deseja testar (ex: exemplo.com)
- `<wordlist>`: Caminho para o arquivo de texto contendo os possíveis subdomínios (um por linha)

### Exemplo

```bash
python DNS.py exemplo.com dns-name-common.txt
```

O script irá tentar resolver cada subdomínio listado na wordlist para o domínio informado e mostrar os que forem encontrados.

## Saída esperada

- Subdomínios encontrados serão exibidos em azul e verde.
- Se nenhum argumento for passado, será exibida uma mensagem de uso.

## Observações

- O script ignora subdomínios que não resolvem (não existem).
- Certifique-se de ter permissão para realizar testes no domínio alvo.

---

Projeto para fins educacionais. 