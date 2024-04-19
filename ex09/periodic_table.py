# Abrir o arquivo e ler seu conteúdo
with open("periodic_table.txt", "r") as file:
    data = file.readlines()

# Inicializar um dicionário para armazenar as informações dos elementos
elements_dict = {}

# Processar as informações de cada linha do arquivo
for line in data:
    # Dividir a linha em elementos separados
    elements = line.strip().split(", ")

    # Verificar se o formato da linha é o esperado
    if len(elements) != 1:
        print("Formato de linha incorreto:", line)
        continue

    # Extrair informações
    name, properties = elements[0].split(" = ")

    # Dividir as propriedades em uma lista
    properties_list = properties.split(", ")

    # Verificar se existem propriedades suficientes
    if len(properties_list) < 5:  # Alterado para 5
        print("Número insuficiente de propriedades:", line)
        continue

    # Extrair informações relevantes
    position = int(properties_list[0].split(":")[1])
    atomic_number = int(properties_list[1].split(":")[1])
    symbol = properties_list[2].split(":")[1]
    atomic_mass = float(properties_list[3].split(":")[1])

    # Tratar a propriedade 'electron' para garantir que seja um único número
    electrons = properties_list[4].split(":")[1].strip()

    # Armazenar as informações em um dicionário
    elements_dict[symbol] = {
        "name": name,
        "position": position,
        "atomic_number": atomic_number,
        "atomic_mass": atomic_mass,
        "electrons": electrons
    }

# Gerar o código HTML correspondente
html_code = "<table>\n"

for symbol, info in elements_dict.items():
    html_code += "<tr>\n"
    html_code += f"<td style='border: 1px solid black; padding:10px'>\n"
    html_code += f"<h4>{info['name']}</h4>\n"
    html_code += "<ul>\n"
    html_code += f"<li>Nº {info['atomic_number']}</li>\n"
    html_code += f"<li>{symbol}</li>\n"
    html_code += f"<li>{info['atomic_mass']}</li>\n"
    html_code += f"<li>{info['electrons']} elétrons</li>\n"
    html_code += "</ul>\n"
    html_code += "</td>\n"
    html_code += "</tr>\n"

html_code += "</table>"

# Escrever o código HTML em um arquivo
with open("periodic_table.html", "w") as html_file:
    html_file.write(html_code)

print("Arquivo periodic_table.html gerado com sucesso!")



