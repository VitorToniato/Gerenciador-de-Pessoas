import json

print('==========================')
print('|   CADASTRO DE PESSOAS  |')
print('|   OPÇÕES DE ESCOLHA    |')
print('|   [1] Cadastra Pessoa  |')
print('|   [2] Verificações     |')
print('|   [3] Buscar Pessoas   |')
print('|   [4] Remover Pessoas  |')
print('|   [5] Salvar Arquivos  |')
print('|   [6] Carregar Arquivos|')
print('|   [5] Salvar e Sair    |')
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
                soma_idade += p['Idade']
                if p['Idade'] >= 18:
                    maiores_idade.append(f'\n{p['Nome']} tem {p['Idade']} anos')
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
    while True:
        pesquisa = input('Digite o nome que deseja pesquisa: ')
        pesquisaM = pesquisa.lower()
        achados = []

        for p in dados:
            nome_pessoas = p['Nome']; nome_pessoasM = nome_pessoas.lower()

            if pesquisaM in nome_pessoasM:
                achados.append(p)
                
        if achados:
            print('Nomes encontrados:')
            for p in achados:
                print(f'- Nome: {p['Nome']}, Idade: {p['Idade']} anos.')
                
        else:
            print(f'Nenhum nome encontrado com {pesquisaM}')
            break
        nova_pesq = input('Deseja fazer uma nova pesquisa? S/N')
        if nova_pesq.lower() == 'S'.lower():
            continue
        else:
            break    

def remove_pessoas():
    while True:
        nome_remove = input('Digite o nome que deseja remover do Sistema: ')
        achados = []

        for indice, p in enumerate(dados):
            if 'Nome' in  p:

                if nome_remove.lower() in p['Nome'].lower():
                        achados.append((indice, p))
    
        if achados:
            print('Nomes encontrados: ')
            for i, (indice, nome_achado) in enumerate(achados):
                print(f'[{i}] - Índice: {indice} | Nome: {nome_achado['Nome']} | Idade: {nome_achado['Idade']}')

            try:
                verificacao = int(input('Digite o indice do nome que deseja remover: '))
                if 0 <= verificacao < len(achados):
                    id_real = achados[verificacao][0]
                    p_real = achados[verificacao][1]

                    confirmacao = input(f'Tem certeza que deseja remover "{p_real['Nome']}"(Indice Originnal: {id_real})? (S/N): ').lower()
                    if confirmacao == 's':
                        del dados[id_real]
                        print(f'Nome: {p_real['Nome']} removido com sucesso!')
                        print(dados) 
                    else:
                        print('Remoção cancelada.')
                else:
                    print('Número inválido. Por favor, digite um número que esteja na lista dos itens encontrados.')

            except ValueError:
                print('Error de digitação, digite apenas números, por favor!')
                continue
            except IndexError:
                print('Número inválido. Por favor, digite um número que esteja na lista dos itens encontrados.')
                continue
        else:
            print(f'Nenhum nome encontrado com {nome_remove}')
            break
        try:
            novo_remove_resposta = input('Deseja remover algum outro nome do sistema? (S/N): ').lower().strip()
        except ValueError:
            if novo_remove_resposta != 's'.lower() or novo_remove_resposta != 'n'.lower():
                print('Resposta inválida. Por favor, digite S para sim ou N para não.')
            if novo_remove_resposta == 's':
                continue # Sai do loop interno e continua o loop principal (volta para 'Digite o nome...')
            else:
                break # Sai do loop interno

            

# salvar dados 5 !!

def salvar_arquivos():
    try:
        with open ('Dados/dados.json', 'w') as f:  # salva os dados no arquivo json
            json.dump(dados, f, indent = 4)

        print('Dados salvo com sucesso!')
    except (FileNotFoundError, OSError) as e:  # Captura exceções relacionadas à não existência do arquivo ou problemas de sistema de arquivos.
        print(f"Erro ao salvar o arquivo: {e}")

    except json.JSONDecodeError as e: #  Captura erros específicos de codificação JSON, como dados inválidos.
        print(f"Erro ao codificar os dados como JSON: {e}")

    except Exception as e:  #  Captura qualquer outra exceção não tratada, fornecendo um tratamento genérico.
        print(f"Ocorreu um erro inesperado: {e}")

# carregar dados 6
def carregar_arquivos():
     with open('Dados/dados.json', 'r') as f:
         print('Dados salvo com sucesso!!')

         print('Infelizmente não há dados para carregar a lista está vazia.')
# sair e salvar 7

def sair_e_salvar():
 
    try:
        with open ('Dados/dados.json', 'w') as f:  # salva os dados no arquivo json
            json.dump(dados, f, indent = 4)

    except (FileNotFoundError, OSError) as e:
        print(f"Erro ao salvar o arquivo: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao codificar os dados como JSON: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    pass
    # codigo saindo do sistema.

escolha()