# -*- coding: utf-8 -*-

# Dicionários de estados e cidades capitais - neste trecho estou definindo dois dicionarios em Python
# dicionário de estados, que estou chamando de "states"
# dicionário de capitais, que estou chamando de capital_cities

states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

#print("Dicionário de estados:")
#print(states)

#print("\nDicionário de cidades capitais:")
#print(capital_cities)

# A função `get_state(capital)`: Recebe uma cidade capital como argumento e itera (percorre os elementos) sobre os itens do dicionário `capital_cities` 
# utilizando o método `items()` e retorna uma lista de tuplas com a chave e o valor
# O método retorna uma visualização dos pares chave-valor no dicionário
# Para cada par de estado e cidade capital, verifica se a cidade capital fornecida corresponde à cidade capital no dicionário.
# Se corresponder, retorna o estado correspondente; caso contrário, retorna "Capital desconhecida".

def get_state(capital):
    for state, capital_city in capital_cities.items():
        if capital_city == capital:
            return state
    return "Capital desconhecida"

# importa o módulo `sys` para lidar com os argumentos da linha de comando
# verifica se o número de argumentos é válido - sendo o nome do script e o segundo sendo a capital fornecida
# Se houver apenas um argumento, exibe uma mensagem solicitando ao usuário que forneça uma capital como argumento
# Se houver mais de dois argumentos, exibe uma mensagem solicitando ao usuário que forneça apenas uma capital como argumento.

def main():
    import sys
    # Verificar se o número de argumentos é válido
    if len(sys.argv) == 2:
        capital = sys.argv[1]
        # Obter o estado correspondente e exibir na saída padrão
        state = get_state(capital)
        print(state)
    elif len(sys.argv) == 1:
        print("Por favor, forneça uma capital como argumento.")
    else:
        print("Por favor, forneça apenas uma capital como argumento.")

#a linha if __name__ == "__main__": main() verifica se o script está sendo executado diretamente (em vez de ser importado como um módulo em outro script)
        
if __name__ == "__main__":
    main()


