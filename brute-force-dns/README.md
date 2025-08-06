# DNS Brute Force

Este projeto contém um script em Python para realizar brute force de subdomínios em um domínio alvo, utilizando uma wordlist.

## Requisitos

- Python 3.x
- [colorama](https://pypi.org/project/colorama/)

Você pode instalar a dependência com:

```bash
pip install colorama
```

## Como usar

Execute o script passando o domínio alvo e o caminho para a wordlist de subdomínios:

```bash
python dns-brute-force.py <dominio> <wordlist>
```

- `<dominio>`: O domínio que você deseja testar (ex: exemplo.com)
- `<wordlist>`: Caminho para o arquivo de texto contendo os possíveis subdomínios (um por linha)

### Exemplo

```bash
python dns-brute-force.py exemplo.com wordlist.txt
```

O script irá tentar resolver cada subdomínio listado na wordlist para o domínio informado e mostrar os que forem encontrados.

## Saída esperada

- Subdomínios encontrados serão exibidos em azul e verde.
- Se os argumentos não forem passados corretamente, será exibida uma mensagem de uso.

## Observações

- O script ignora subdomínios que não resolvem (não existem).
- Certifique-se de ter permissão para realizar testes no domínio alvo.

---

Projeto para fins educacionais. 