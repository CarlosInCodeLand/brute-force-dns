#!/bin/bash

cont=0

apresentacao() {
    clear
    echo -e "\033[01;32m-------------------\033[00;00m"
    echo -e "\033[01;31m   SUB DOMAINS   \033[00;00m"
    echo -e "\033[01;32m-------------------\033[00;00m"
}

entDados() {
    if [[ ! -f "$1" ]]; then
        echo "Usage: ./dns_scan.sh <common-dns-name.txt>"
        exit 1
    fi

    echo -ne "\033[01;34m\n#Dominio: \033[00;00m"
    read domain
    echo ""

    for i in $(cat "$1"); do
        ping -c 1 -W 2 "$i.$domain" > /dev/null 2>&1

        if [[ $? -eq 0 ]]; then
            echo "-> $i.$domain"
        fi

        cont=$((cont+1))

        if (( cont == 50 )); then
            echo -e "\033[01;35m-> 50% da lista verificado!\033[00;00m"
        fi
    done
}

apresentacao
entDados "$1"

