#!/bin/bash

# Verifica se o usuário forneceu um URL bit.ly como argumento
if [ -z "$1" ]; then
    echo "Por favor, forneça um URL bit.ly"
    exit 1
fi

# Usa curl para obter a URL real do link bit.ly
real_url=$(curl -s -L -o /dev/null -w %{url_effective} "$1")

# Exibe a URL real
echo "$real_url"


#o comando !/bin/bash: Esta linha é conhecida como shebang. Ela é usada para especificar qual interpretador de shell deve ser usado para executar o script. 
#No caso desta linha, #!/bin/bash indica que o script deve ser interpretado pelo bash, que é um interpretador de shell comum em sistemas Unix e Linux.

# if [ -z "$1" ]; then: Esta linha inicia uma estrutura condicional (if) no shell script. 
# verifica se o primeiro argumento passado para o script (indicado por $1) está vazio (-z). 
# Se estiver vazio, ou seja, se o usuário não fornecer nenhum argumento ao executar o script, o bloco de código dentro do if será executado.
# echo pede para o usuário fornecer a url encurtada, se o primeiro argumento estiver vazio
# exit 1: Esta linha encerra a execução do script 
# No shell script, o fi é uma palavra-chave que marca o fim de uma estrutura condicional iniciada com if
# curl é uma ferramenta de linha de comando utilizada para transferir dados para ou de um servidor, usando um dos protocolos suportados (HTTP, HTTPS, FTP, etc.).