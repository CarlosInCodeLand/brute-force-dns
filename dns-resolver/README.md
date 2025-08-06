# DNS Info Resolver (Em Progresso)

Este projeto contém um script em Python para consultar diferentes tipos de registros DNS de um domínio, como A, CNAME, AAAA (IPv6) e PTR (reverso).

⚠️ **Projeto em desenvolvimento!** Algumas funcionalidades podem não estar finalizadas ou podem ser alteradas.

## Requisitos

- Python 3.x
- [dnspython](https://pypi.org/project/dnspython/)
- [colorama](https://pypi.org/project/colorama/)

Instale as dependências com:

```bash
pip install dnspython colorama
```

## Como usar

O script está configurado para consultar o domínio `google.com` por padrão, mas você pode alterar a variável `DOMINIO` no início do arquivo para o domínio desejado.

Execute o script normalmente:

```bash
python dns-info.py
```

## Funções disponíveis

- `ip(dominio)`: Retorna os endereços IPv4 (A) do domínio.
- `cname(dominio)`: Retorna os registros CNAME do domínio.
- `ipv6(dominio)`: Retorna os endereços IPv6 (AAAA) do domínio.
- `ptr(dominio)`: Retorna o registro PTR (reverso) do domínio.

## Observações

- O script imprime mensagens de erro caso algum registro não seja encontrado ou ocorra falha na consulta.
- O projeto está em progresso e pode receber melhorias e novas funcionalidades.

---

Projeto para fins educacionais e experimentação. 