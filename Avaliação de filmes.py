# Nomes dos clientes que avaliaram o filme
nomes = [
    'Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo',
    'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia',
    'Karen', 'Leonardo', 'Marina', 'Nicolas', 'Olivia',
    'Paulo', 'Rafaela', 'Sofia', 'Thiago', 'Vanessa'
]

# Gêneros dos clientes
generos = [
    'F', 'M', 'M', 'F', 'M',
    'F', 'M', 'F', 'M', 'F',
    'F', 'M', 'F', 'M', 'F',
    'M', 'F', 'F', 'M', 'F'
]

# Notas dadas pelos clientes para o filme
notas = [
    8.5, 7.0, 9.2, 6.8, 7.5,
    8.0, 6.5, 9.0, 7.8, 8.2,
    5.9, 7.3, 6.4, 8.7, 9.1,
    7.6, 6.9, 8.8, 7.2, 8.4
]

# Demanda 01 - Combinando as informações dos clientes em um dicionário
#   Vamos criar o dicionário baseando a chave como o nome do cliente e o valor como uma lista que tem o gênero e a nota da pessoa
#   Aqui eu vou usar list comprehension, porque se usar só um for, ele vai calcular e substituir os valores a cada vez
#que ele calcular, a não ser que eu use um .append() pra criar uma lista de dicionários, mas não é isso que ele quer
clientes = {nomes[i]: [generos[i], notas[i]] for i in range(len(nomes))}

#E vamos, por fim, tentar pegar as informações de uma pessoa pela chave para ver se funcionou
try:
    #Vamos primeiro tratar a entrada para ficar no formato em que os nomes estão
    nome = input('Digite o nome do cliente: ').capitalize().strip()
    info = clientes[nome]
except TypeError as erro:
    #Esperando que alguém digite o nome de uma pessoa errado ou algo estranho
    print('Esse pessoa não está cadastrada')
finally:
    #Por fim, vamos mostrar as informações da pessoa se ela estiver cadastrada
    print(f"Cliente {nome} é {info[0]} e sua nota é {info[1]}")

# Demanda 02 - Descobrir qual público (masc. ou femi.) gostou mais do filme
#Vamos primeiro definir uma função para calcular a média
def media_por_genero(lista:list) -> float:
    return round(sum(lista) / len(lista),2)
#Perfeito, agora vamos criar duas listas diferentes para cada gênero, contendo as notas de cada um
notaM = [info[1] for info in clientes.values() if info[0] == 'M']
notaF = [info[1] for info in clientes.values() if info[0] == 'F']
#Perfeito, agora só passar para a função e verificar qual gostou mais
notafF = media_por_genero(notaF)
notafM = media_por_genero(notaM)
if notafF>notafM:
    print(f"A nota final das mulheres foi maior, com uma média de: {notafF}")
elif notafM>notafF:
    print(f"A nota final dos homens foi maior, com uma média de: {notafM}")
else:
    print(f"A nota final de ambos foi a mesma, com uma média de: {notafM}")
