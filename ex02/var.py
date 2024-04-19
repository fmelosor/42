def my_var():
    # Declarando as variáveis
    var1 = 42  #class int representa numero inteiro em Python
    var2 = "42" #class str representa strings 
    var3 = "quarante-deux" 
    var4 = 42.0 #class float representa numeros flutuantes (inteiro e fracao)
    var5 = True # class bool representa valores booleanos (Verdadeiro ou Falso - True ou False)
    var6 = [42] #class list representa uma lista
    var7 = {42: 42} #class dict representa um dicionario
    var8 = (42,) #class tuple representa uma coleção ordenada e imutavel de itens
    var9 = set() #class set representa conjuntos (colecao nao ordenada e sem elementos duplicados)

  # Imprima as variaveis junto com os seus tipos
    print(f"{var1} has a type {type(var1)}")
    print(f"{var2} has a type {type(var2)}")
    print(f"{var3} has a type {type(var3)}")
    print(f"{var4} has a type {type(var4)}")
    print(f"{var5} has a type {type(var5)}")
    print(f"{var6} has a type {type(var6)}")
    print(f"{var7} has a type {type(var7)}")
    print(f"{var8} has a type {type(var8)}")
    print(f"{var9} has a type {type(var9)}")

if __name__ == '__main__':
    my_var()

# verifica se o script está sendo executado como o programa principal (`if __name__ == '__main__':`)
# se sim, chama a função `my_var()`, que executa todo o código dentro dela