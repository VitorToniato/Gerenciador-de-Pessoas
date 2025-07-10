import json

dic = []

repetir = int(input('Digite quantos nomes deseja inserir: '))


for i in range(1, repetir + 1):
    nome = input('Digite o nome que deseja inserir: ')
    idade = input('Digite sua idade')

    dic.append({
        'Nome': nome, 
        'Idade': idade
        
        })
    
json_data = json.dumps(dic)

with open('Teste com Json/pessoas.json', 'w') as arquivos:
    json.dump(dic, arquivos, indent=4)



print(json_data)
print()