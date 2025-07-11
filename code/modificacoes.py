import json

print('==========================')
print('|   CADASTRO DE PESSOAS  |')
print('|   OPÇÕES DE ESCOLHA    |')
print('|   [1] Cadastra pessoa  |')
print('|   [2] Verificações     |')
print('|   [3] Buscar pessoa    |')
print('|   [4] Remover Pessoa   |')
print('|   [5] Sair do Sistema  |')
print('==========================')


# carregamento de dados.

try:
    with open('Dados/dados.json', 'r') as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError: # caso o arquivo estiver vazio ou invalido.
            dados = []
except FileNotFoundError:  # caso o arquivo não exista
            dados = []

def escolha():
    while True:
        try:
            escolha = int(input('Escolha qual opção você quer: '))
        except ValueError:
            print('Entrada Inválida, digite um números.')
            continue

        match escolha:
            case 1:
                cadastro() 
            case 2:
                verificacao()
            case 3:
                buscar_pessoas()
            case 4:
                remove_pessoas()
            case 5:
                salvar_arquivos()
            case 6:
                carregar_arquivos()
                pass
            case 7:
                sair_e_salvar()
             
# case 1
def cadastro():
    

    while True:
        nome = input('Digite o nome da pessoa que deseja inserir: ')
        try:
            idade = int(input('Digite a idade da pessoa: '))
            if idade < 0:
                print('Idade não pode ser negativo. Tente novamente!')
                continue
        except ValueError:
                print('Idade Inválida. Por favor, digite um número!')
                continue
        
        dados.append({'Nome': nome,
                      'Idade': idade})
       
    
        novo = input('Deseja cadastrar uma nova pessoa? S/N ')
        if novo.lower() == 'S'.lower():
            continue
        else:
            break

            
        

        # cod original
        '''
        print('CADASTRO')
        nome = input('Digite um nome: ')
        try:
            idade = int(input('Digite a idade da pessoa: '))
            if idade < 0:
                print('Idade não pode ser negativo. Tente novamente!')
                continue
        except ValueError:
                print('Idade Inválida. Por favor, digite um número!')
                continue

        dados.append({'nome': nome, 'idade': idade})
        print('Pessoas cadastrada !\n')

        novo = input('Deseja cadasra uma nova pessoa? S/N ')

        if novo.lower() == 'S'.lower():
            continue
        else:
            break
        '''
# case 2
def verificacao():

        while True:
         
            print('VERIFICAÇÕES')
            if not dados:
                print('Nenhuma pessoa cadastrada ainda.\n')
                print('Cadastre alguma pessoa para fazer as seguintes orientações.')

            soma_idade = 0
            maiores_idade = []

            for p in dados:
                soma_idade += p['idade']
                if p['idade'] >= 18:
                    maiores_idade.append(f'\n{p['nome']} tem {p['idade']} anos')
            media = soma_idade / len(dados)
                


            print(f'{len(dados)} pessoas foram cadastradas ao sistema.')
            print(f'A média de idade é de {media:.2f}')

            if maiores_idade:
                print(f'Pessoas maiores de 18 anos: { ' '. join(maiores_idade)}')
                break
            else:
                print(f'Não há pessoas maiores de 18 anos cadastradas.')
                break
        print()

def buscar_pessoas():
    pass


def remove_pessoas():
    pass

def salvar_arquivos():
    with open ('Dados/dados.json', 'w') as f:
        json.dump(dados, f, indent = 4)

    print('Dados salvo com sucesso!')


def carregar_arquivos():
    pass


def sair_e_salvar():
    pass

escolha()