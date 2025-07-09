import json

dic = []

repetir = int(input('Digite quantos nomes deseja inserir: '))


for i in range(1, repetir + 1):
    nome = input('Digite o nome que deseja inserir: ')

    dic.append({
        'Nome': nome
        
        })
    

with open('Teste com Json/pessoas.json', 'w') as arquivos:
    json.dump(dic, arquivos)

print()