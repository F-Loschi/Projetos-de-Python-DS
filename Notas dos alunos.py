#Notas de alunos
#Por Felipe Silva Loschi
#
#   Esse exercício veio do bom e velho Gustavo Bruno Tomas, ou para os íntimos, GPT.
#   Pedi pra ele se basear no exercício da avaliação de filmes e me dar algo no mesmo nível, com perguntas diferentes
#e dados base diferentes, pra poder continuar colocando em prova meu conhecimento da base de Python para DS
nomes = ['Alice', 'Bruno', 'Carla', 'Diego', 'Elisa']
materias = ['Matemática', 'Português', 'História', 'Geografia', 'Ciências']
notas = [
    [8.5, 7.0, 9.0, 6.5, 8.0],  # Notas de Alice
    [7.2, 8.4, 6.8, 9.1, 7.9],  # Notas de Bruno
    [9.0, 8.7, 7.5, 8.8, 8.3],  # Notas de Carla
    [6.5, 7.2, 8.1, 8.5, 7.3],  # Notas de Diego
    [8.1, 9.0, 7.6, 8.2, 9.1]   # Notas de Elisa
]
#Esse é mais complexo que o dos filmes
#
#Os objetivos:
#
# 1) Combinar essas informações num dicionário, onde a chave é o nome do aluno, e o valor é um novo dicionário que contém as matérias e as respectivas notas.
# 2) Permitir que o usuário consulte as notas de um aluno específico e exiba suas notas em todas as matérias.
# 3) Calcular a média das notas em cada matéria para descobrir em qual matéria os alunos tiveram o melhor desempenho geral.

# 1)
#
#Primeiro, vamos tentar colocar em um dicionário
alunos = {nomes[i] : {materias[j] : notas[i][j] for j in range(len(notas))} for i in range(len(notas))}
#   Minha solução foi colocar em um dicionário de dicionários, que a primeira chave é o nome do aluno e o valor é um
#dicionário em que as chaves são as matérias e os valores, a nota do aluno
#   Acho que a grande questão agora vai ser como que eu vou acessar isso, mas vamo em frente

#2)
#Tá, vamo tentar acessar isso usando o try-expect-finally pra tentar acessar com o nome de um aluno
try:
    nome = input('Qual o nome do aluno? ').capitalize().strip()
    info = alunos[nome]
except KeyError:
    print('Essa pessoa não está cadastrada')
else:
    #Se isso funcionar eu sou maluco
    for materia, nota in info.items():
        print(f"A nota do aluno na materia {materia} foi {nota}")
    #Eu não sou maluco, tive que fazer ajustes, mas deu certo!!!!
#Pô, que loucura, tinha esquecido completamente que podia usar duas coisas em um for pra iterar um dicionário, isso é
#extremamente útil

#3)
# Agora o filho chora e a mãe não vê
medias_materias = {materia: round(sum(alunos[aluno][materia] for aluno in alunos) / len(nomes), 2) for materia in materias}
#  Isso possivelmente vai dar certo, tô criando um dicionário com o nome da matéria como chave e a média como valor
#  Na média, tô acessando o dicionário aluno, dentro dele eu acesso o dionário materia e pego ele e vou somando com
#o dos outros alunos, depois arredondo e divido pelo número de nomes, pra fazer a média

# Vamos agora identificar a matéria com maior média
melhor_materia = max(medias_materias, key=medias_materias.get)
#Beleza, tô usando a função max pra pegar o maior dentro do dicionário
#comparando os valores de cada chave para ver qual foi o maior
print(f"A matéria com melhor desempenho geral foi {melhor_materia}, com média de {medias_materias[melhor_materia]:.2f}")
