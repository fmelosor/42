# -*- coding: utf-8 -*-

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

print("Dicionário de estados:")
print(states)

print("\nDicionário de cidades capitais:")
print(capital_cities)

def detect_city_or_state(expression):

    cleaned_expression = expression.strip().lower()

    print("Expressão limpa:", cleaned_expression)

    if cleaned_expression in capital_cities.values():
        print("Expressão encontrada como capital")
        return "capital"
    elif cleaned_expression in states.keys():
        print("Expressão encontrada como estado")
        return "estado"
    else:
        cleaned_expression_no_space = "".join(cleaned_expression.split())
        print("Expressão sem espaços extras:", cleaned_expression_no_space)

        if cleaned_expression_no_space in capital_cities.values():
            print("Expressão sem espaços extras encontrada como capital")
            return "capital"
        elif cleaned_expression_no_space in states.keys():
            print("Expressão sem espaços extras encontrada como estado")
            return "estado"
        else:
            print("Expressão não correspondente")
            return "nenhum"


