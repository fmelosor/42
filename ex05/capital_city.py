# -*- coding: utf-8 -*- #Serve para ler os caracteres especiais*

# Dicionários de estados e cidades capitais
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

def get_capital(state):

    # Verificar se o estado está no dicionário de estados 
    # Recebe um estado como argumento e verifica se ele está presente no dicionário de estados
    # Se estiver, retorna a cidade capital correspondente
    # caso contrário, retorna "Cidade desconhecida"
    # e o estado não estiver no dicionário de estados, retorna "Estado desconhecido"
    # get = obter. É a função que o DEF estã chamando. 
    # Entre () está o parâmetro dado. O parâmetro é uma variável que aceita um valor específico quando a função é chamada

    if state in states:
        # Obter a abreviação do estado
        abbreviation = states[state]
        # Verificar se a abreviação está no dicionário de cidades capitais
        if abbreviation in capital_cities:
            # Retornar a capital correspondente
            return capital_cities[abbreviation]
        else:
            return "Cidade desconhecida"
   
# importa o módulo `sys` para lidar com os argumentos da linha de comando
def main():
    import sys

    # Verificar se o número de argumentos é válido
    # Se houver apenas um argumento, exibe uma mensagem solicitando ao usuário que forneça um estado como argumento
    # Se houver mais de dois argumentos, exibe uma mensagem solicitando ao usuário que forneça apenas um estado como argumento

    if len(sys.argv) == 2:
        state = sys.argv[1]
        # Obter a cidade capital e exibir na saída padrão
        capital = get_capital(state)
        print(capital)
    elif len(sys.argv) == 1:
        print("Por favor, forneça um estado como argumento.")
    else:
        print("Por favor, forneça apenas um estado como argumento.")

if __name__ == "__main__":
    main()


# a linha if __name__ == "__main__": main() 
# verifica se o script está sendo executado como o programa principal. Se sim, chama a função `main()`, que executa todo o código dentro dela. 
