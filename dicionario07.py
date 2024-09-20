# meu dic = {'chave' : 'valor'}
alunos = {'Maria' :888, 'João' :777, 'Ana' :555}
alunos['Maria'] = 444
print(alunos)
alunos['kiko'] = 222 # adicionr chave e valor
print(alunos)
alunos.pop("João") # remover chave e valor
for nome, matricula in alunos.items():
    print(f'Matrícula: {matrícula} nome {nome}')
    alunosCopia = alunos.copy()
    alunosCopia['Ana'] = 999
    print('dicionário alunos', alunos)
    print('dicionário alunosCopia', alunosCopia)