# DNS Info Resolver

Este projeto é um utilitário em Python para consultar rapidamente registros DNS de qualquer domínio, exibindo resultados de forma colorida e amigável no terminal.

## Funcionalidades

- Consulta registros:
  - **A** (IPv4)
  - **AAAA** (IPv6)
  - **CNAME**
  - **PTR** (reverso, a partir de cada IP encontrado)
- Saída colorida para facilitar a visualização dos resultados e avisos.
- Mensagens claras caso algum registro não seja encontrado.

## Requisitos

- Python 3.x
- [dnspython](https://pypi.org/project/dnspython/)
- [colorama](https://pypi.org/project/colorama/)

Instale as dependências com:

```bash
pip install dnspython colorama
```

## Como usar

Execute o script passando o domínio desejado como argumento:

```bash
python3 dns-info.py <DOMINIO>
```

Exemplo:

```bash
python3 dns-info.py globo.com
```

## O que o script faz

- Mostra todos os endereços IPv4 e, para cada um, tenta mostrar o PTR (reverso).
- Mostra todos os endereços IPv6, se existirem.
- Mostra todos os registros CNAME, se existirem.
- Exibe mensagens amigáveis caso algum tipo de registro não seja encontrado.

## Observações

- O script imprime avisos apenas para erros inesperados. Se um registro não existir, apenas informa "Nenhum ... encontrado".
- O projeto está em desenvolvimento e pode receber melhorias.

---

Projeto para fins educacionais e experimentação. 