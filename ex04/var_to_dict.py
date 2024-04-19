# -*- coding: utf-8 -*-


# Lista de pares de dados fornecida no enunciado
data = [
    ('Hendrix', '1942'),
    ('Allman', '1946'),
    ('King', '1925'),
    ('Clapton', '1945'),
    ('Johnson', '1911'),
    ('Berry', '1926'),
    ('Vaughan', '1954'),
    ('Cooder', '1947'),
    ('Page', '1944'),
    ('Richards', '1943'),
    ('Hammett', '1962'),
    ('Cobain', '1967'),
    ('Garcia', '1942'),
    ('Beck', '1944'),
    ('Santana', '1947'),
    ('Ramone', '1948'),
    ('White', '1975'),
    ('Frusciante', '1970'),
    ('Thompson', '1949'),
    ('Burton', '1939')
]

# Criar um dicionário vazio para armazenar os dados
musicos_dict = {}

# Percorrer a lista de pares de dados
for musico, year in data:
    # Inserir o par de dados no dicionário
    musicos_dict[year] = musico

# Exibir o dicionário
print("Dicionário:")
print(musicos_dict)

# -*- coding: utf-8 -*-: Um comentário especificando a codificação do arquivo como UTF-8.
# data = [...]: Define uma lista chamada `data` que contém tuplas (estrutura de dados que armazena uma lista)
# cada tupla representa um par de dados onde o primeiro elemento é o nome do músico e o segundo é o ano de nascimento
# musicos_dict = {}: Cria um dicionário vazio chamado `musicos_dict` para armazenar os dados convertidos
# for musico, year in data: Um loop `for` que itera sobre cada tupla na lista `data`, descompactando as tuplas em `musico` e `year`
# musicos_dict[year] = musico: Dentro do loop, atribui o nome do músico como valor e o ano como chave no dicionário `musicos_dict`
# print("Dicionário:")`: Imprime uma mensagem indicando o início da exibição do dicionário
# print(musicos_dict)`: Imprime o dicionário