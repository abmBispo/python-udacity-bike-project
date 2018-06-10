# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

raw_input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for row in data_list[:20]:
    print(row)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

raw_input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

# Modifiquei um pouco a saída da impressão para denotar espaços vazios no csv
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for row in data_list[:20]:
    if row[6]=='':
        print('NOT_FOUND')
    else:
        print(row[6])

raw_input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """Função para pegar uma coluna do csv e e jogar todos os seus valores numa lista nova
    Args:
        data_list (list): lista lida via csv para ser interpretada
        index (integer): qual coluna será transformada pela 
    Returns:
        column_list (list): uma lista das quantidades dos usuários do tipo "Male" e do tipo "Female".
    """
    column_list = [row[index] for row in data]
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = len([row[6] for row in data_list if row[6]=='Male'])
female = len([row[6] for row in data_list if row[6]=='Female'])

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Função para retornar qual é o maior gênero no data set
    Args:
        data_list (list): lista lida via csv para ser interpretada
    Returns:
        array (list): uma lista das quantidades dos usuários do tipo "Male" e do tipo "Female".
    """
    male = len([row[6] for row in data_list if row[6]=='Male'])
    female = len([row[6] for row in data_list if row[6]=='Female'])
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """Função para retornar qual é o maior gênero no data set
    Args:
        data_list (list): lista lida via csv para ser interpretada
    Returns:
        anwser (string): a resposta pode ser 'Masculino' ou 'Feminino'
    """
    male, famale = count_gender(data_list)
    if male > famale:
        answer = 'Masculino'
    else:
        answer = 'Feminino'
    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O genero mais popular na lista e: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Genero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Genero')
plt.show(block=True)

raw_input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o grafico!")

def most_popular_user_type(data_list):
    """Função para retornar a quantidade de cada tipo de usuário do data set passado via parâmetro (Subscriber ou Customer)
    Args:
        data_list (list): lista lida via csv para ser interpretada e pegar os valores da sexta coluna
    Returns:
        array (list): lista de duas posições que contém primeiro a quantidade de assinantes e depois a quantidade de clientes. 
    """
    male, famale = count_gender(data_list)
    if male > famale:
        answer = 'Masculino'
    else:
        answer = 'Feminino'
    return answer

def count_user_type(data_list):
    """Função para retornar a quantidade de cada tipo de usuário do data set passado via parâmetro (Subscriber ou Customer)
    Args:
        data_list (list): lista lida via csv para ser interpretada e pegar os valores da sexta coluna
    Returns:
        array (list): lista de duas posições que contém primeiro a quantidade de assinantes e depois a quantidade de clientes. 
    """
    subscriber = len([row[5] for row in data_list if row[5]=='Subscriber'])
    customer = len([row[5] for row in data_list if row[5]=='Customer'])
    return [subscriber, customer]

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -3)
types = ["Assinante", "Cliente"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de usuario')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo')
plt.show(block=True)


raw_input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão 
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Ha linhas com dados faltando. Pode ser muito bem observado na TAREFA 2, onde fiz questao de por uma flag `NOT_FOUND` para as colunas com valoresiguais ha '' (string vazia). Dessa forma, quando vamos contar, desconsideramos certos registros ja que nem todos possuem o valor válido ('Male', 'Famele')."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------


raw_input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)

def get_val(data,comparator = 'gt'):
    """Função para pegar ou o maior ou menor valor de uma lista com base no parâmetro 'comparator'.
    Args:
        data (list): lista de números para comparar.
        comparator (string): variável para diferenciar as comparações de maior ou menor (grater than ou less than).
    Returns:
        f_val (float): menor ou maior valor encontrado na lista com base no parâmetro de comparação. 
    """
    f_val = float(data[0])
    for val in data:
        if comparator == 'gt' and float(val) > f_val:
            f_val = float(val)
        elif comparator == 'lt' and float(val) < f_val:
            f_val = float(val)
    return f_val

def mean(data):
    """Função para achar a média dos valores numa lista
    Args:
        data (list): lista de números para comparar.
    Returns:
        mean (float): a média da lista de números.
    """
    return sum([float(val) for val in data if val != ''])/len(data)

def median(data):
    """Função para achar a mediana dos valores numa lista
    Args:
        data (list): lista de números para comparar.
    Returns:
        median (float): a mediana da lista de números.
    """
    data = sorted([float(val) for val in data if val != ''])
    data_len = len(data)
    index = (data_len - 1) // 2
    if data_len % 2 == 0:
        return float(data[index])
    else:
        return (float(data[index]) + float(data[index + 1]))/2.0

min_trip = get_val(trip_duration_list, 'lt')
max_trip = get_val(trip_duration_list, 'gt')
mean_trip = mean(trip_duration_list)
median_trip = median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Media: ", mean_trip, "Mediana: ", median_trip)


# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list,3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------


raw_input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
    # """
    #   Função de exemplo com anotações.
    #   Argumentos:
    #       param1: O primeiro parâmetro.
    #       param2: O segundo parâmetro.
    #   Retorna:
    #       Uma lista de valores x.
    #   """

raw_input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """Função para encontrar os tipos de itens na lista e para contar a quantidade de cada um.
    Args:
        column_list (list): lista de tipos para serem contados.
    Returns:
        item_types (list): lista de valores possíveis
        count_items (list): lista dos valores de quantidade para cada tipo encontrado
    """
    item_types = set(column_list)
    count_items = [column_list.count(type) for type in item_types]
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------