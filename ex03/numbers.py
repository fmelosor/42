# -*- coding: utf-8 -*-

# Abre o arquivo numbers.txt 
# o r significa que é modo leitura

with open('numbers.txt', 'r') as file:
    
    # Lê o conteúdo do arquivo
    conteudo = file.read()

print(conteudo)

# Substitui as vírgulas por quebras de linha
conteudo = conteudo.replace(',', '\n')

# Exibe os números um por linha
print(conteudo)


#-*- coding: utf-8 -*-` especifica a codificação do arquivo como UTF-8, permitindo o uso de caracteres especiais
# with open('numbers.txt', 'r') as file:`: Esta linha abre o arquivo 'numbers.txt' em modo de leitura (`'r'`)
# o Wiht garante que o arquivo seja fechado automaticamente após o término do bloco de código
# print(conteudo): Esta linha imprime o conteúdo do arquivo, ou seja, todos os números separados por vírgulas
# conteudo = conteudo.replace(',', '\n')`: Esta linha substitui todas as vírgulas no conteúdo pelo caractere de quebra de linha (`'\n'`). 
# Assim, cada número será exibido em uma linha separada.
# print(conteudo)`: Esta linha imprime o conteúdo após a substituição das vírgulas por quebras de linha, resultando na exibição dos números um por linha