# -*- coding: utf-8 -*-

# Dicionários de estados e cidades capitais
from ast import Expression


states = {
    "Oregon":"OR",
    "Alabama":"AL",
    "New Jersey":"NJ",
    "Colorado":"CO"
}

capital_cities = {
    "OR":"Salem",
    "AL":"Montgomery",
    "NJ":"Trenton",
    "CO":"Denver"
}


#print("Dicionário de estados:")
#print(states)

#print("\nDicionário de cidades capitais:")
#print(capital_cities)

# def chama a funcao que ira detectar a cidade ou estado. entre pararenteses define o parâmeto da função, que chamamos de expressao

# Limpa cleaned_expression limpa a expressao removendo espaços extras e convertendo para minúsculas. 
    # Strip é um método de string que remove os espaços em branco. 
    # Lower é um método string que converte todas as letras em minúsculas 
    
    # Verificar se a expressão é uma capital
   

    # Verificar se a expressão é um estado
  

    # Se não for uma capital nem um estado, tentar encontrar correspondência removendo espaços extras
        # split() divide a expressão em uma lista de substrings, separadas por espaços
        # "".join() junta essas substrings sem espaços, criando assim uma versão da expressão sem espaços extras.
        # values() retorna os valores associados às chaves do dicionário, enquanto keys() retorna as próprias chaves do dicionário

    def detect_city_or_state(expression):
    # Limpa a expressão, removendo espaços extras e convertendo para minúsculas
    cleaned_expression = Expression.strip().lower()

    print("Expressão limpa:", cleaned_expression)

    # Verifica se a expressão é uma capital
    if cleaned_expression in capital_cities.values():
        print("Expressão encontrada como capital")
        return "capital"

    # Verifica se a expressão é um estado
    elif cleaned_expression in states.keys():
        print("Expressão encontrada como estado")
        return "estado"

    # Se não for uma capital nem um estado, tenta encontrar correspondência removendo espaços extras
    else:
        # Remove os espaços extras da expressão
        cleaned_expression_no_space = "".join(cleaned_expression.split())
        print("Expressão sem espaços extras:", cleaned_expression_no_space)
        
        # Verifica se a expressão (sem espaços extras) é uma capital
        if cleaned_expression_no_space in capital_cities.values():
            print("Expressão sem espaços extras encontrada como capital")
            return "capital"
        
        # Verifica se a expressão (sem espaços extras) é um estado
        elif cleaned_expression_no_space in states.keys():
            print("Expressão sem espaços extras encontrada como estado")
            return "estado"
        
        # Se não for uma capital nem um estado, retorna "nenhum"
        else:
            print("Expressão não correspondente")
            return "nenhum"


#importa o módulo sys que dá acesso a algumas variáveis do sistema

    # Verificar se foi fornecido o número correto de argumentos
    # sys.argv é uma lista ista que contém os argumentos fornecidos na linha de comando quando o script é executado
    # len etermina o comprimento ou a quantidade de itens em um objeto, dependendo do tipo do objeto fornecido como argumento
    # !=2 verifica se o número de argumentos fornecido não é igual a 2
    # sys.argv é uma lista que contém os argumentos passados para o script
    # Iterar (percorrer cada elemento e realizar alguma operaçao) sobre as expressões e determinar se são capitais, estados ou nenhum deles
    # for é um loop (executar um trenho do código repetidamente até que uma condicao seja atendida)
        
        def main():
                import sys

    # Verifica se foi fornecido o número correto de argumentos
        if len(sys.argv) != 2:
            print("Erro: Por favor, forneça uma única string como argumento.")
            return

    # Obtém a string de argumento fornecida
    
    arg_string = sys.argv[1]

    # Divide a string de argumento em expressões separadas por vírgula
    expressions = [exp.strip().lower() for exp in arg_string.split(',')]

    # Itera sobre as expressões e determina se são capitais, estados ou nenhum deles
        for expression in expressions:
        if expression == "":
            continue  # Ignora expressões vazias
        elif "," in expression:
            continue  # Ignora expressões com vírgula adicional
        else:
            # Chama a função detect_city_or_state para determinar o tipo da expressão
            result = detect_city_or_state(expression)
            if result == "capital":
                # Se for uma capital, encontra o estado correspondente e imprime a mensagem
                state = [key for key, value in capital_cities.items() if value == expression][0]
                print(f"{expression.capitalize()} é a capital de {state.upper()}")
            elif result == "estado":
                # Se for um estado, encontra a capital correspondente e imprime a mensagem
                capital = capital_cities[[k for k, v in states.items() if v == expression][0]]
                print(f"{expression.capitalize()} é a capital de {capital}")
            else:
                # Se não for uma capital nem um estado, imprime uma mensagem informando isso
                print(f"{expression.capitalize()} não é uma capital nem um estado")

   

    # no bloco acima estou verificando se a variavel result é uma capital. se for verdadeiro, executa a linha do código. 
    # depois encontramos o estado associado dessa capital.


    #o último bloco verifica se o script está sendo executado diretamente (em vez de ser importado como um módulo em outro script) e, se for o caso, 
    #chama a função main() para iniciar a execução do código principal do script. 
    #Isso permite que o script seja reutilizável e importável em outros scripts sem que o código dentro de main() seja executado quando importado.