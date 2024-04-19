# my_sort.py

# Define um dicionário que contém os nomes dos músicos como chaves e seus anos de nascimento como valores associado

dicionario = {
    'Hendrix': '1942',
    'Allman': '1946',
    'King': '1925',
    'Clapton': '1945',
    'Johnson': '1911',
    'Berry': '1926',
    'Vaughan': '1954',
    'Cooder': '1947',
    'Page': '1944',
    'Richards': '1943',
    'Hammett': '1962',
    'Cobain': '1967',
    'Garcia': '1942',
    'Beck': '1944',
    'Santana': '1947',
    'Ramone': '1948',
    'White': '1975',
    'Frusciante': '1970',
    'Thompson': '1949',
    'Burton': '1939',
}

# Função para ordenar os músicos
def sort_musicians(dicionario):
    sorted_musicians = sorted(dicionario.items(), key=lambda x: (x[1], x[0]))
    for musician, _ in sorted_musicians:
        print(musician)

if __name__ == "__main__":
    sort_musicians(dicionario)




    # Primeiro, ordenamos o dicionário com base no ano de nascimento dos músicos
    # key=lambda x: (x[1], x[0]): AEsta linha ordena os itens do dicionário com base em uma chave personalizada. Usamos o lambda como chave de ordenação
    # A função lambda retorna uma tupla com o ano de nascimento (segundo elemento) seguido pelo nome do músico (primeiro elemento).
    # Isso garante que os músicos sejam ordenados primeiro pelo ano de nascimento e, em seguida, pelo nome
    # O loop for itera sobre os músicos ordenados e imprime apenas o nome de cada músico, um por linha, sem mostrar o ano de nascimento.
    # verifica se o script está sendo executado como o programa principal