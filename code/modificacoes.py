import json
import os

def menu():

    print('==========================')
    print('|   OPÇÕES DE ESCOLHA    |')
    print('|   CADASTRO DE PESSOAS  |')
    print('|   [1] Cadastra Pessoa  |')
    print('|   [2] Verificações     |')
    print('|   [3] Buscar Pessoas   |')
    print('|   [4] Remover Pessoas  |')
    print('|   [5] Salvar Arquivos  |')
    print('|   [6] Carregar Arquivos|')
    print('|   [7] Salvar e Sair    |')
    print('==========================')


# carregamento de dados.
caminho_arquivo = 'Dados/dados.json'
diretorio_dados = os.path.dirname(caminho_arquivo)
if not os.path.exists(diretorio_dados):
    os.makedirs(diretorio_dados)

try:
    with open(caminho_arquivo, 'r') as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError: # caso o arquivo estiver vazio ou invalido.
            dados = []
except FileNotFoundError:  # caso o arquivo não exista
            dados = []

def escolha():
    while True:
        menu()
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

            case 7:
                if not sair_e_salvar(): # Se retornar False
                    break # Sai do loop 'while True' em escolha()
             
# case 1
def cadastro():
    print()
    print('CADASTRO')
    global dados

    while True:
        nome = input('Digite o nome da pessoa que deseja inserir: ').strip()
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
       
    
        novo = input('Deseja cadastrar uma nova pessoa? S/N ').strip()
        if novo.lower() == 'S'.lower():
            continue
        else:
            break
        
# case 2

def verificacao():  
    print()
    print('VERIFICAÇÕES')
    if not dados:
        print('Nenhuma pessoa cadastrada ainda.')
        print('Cadastre alguma pessoa primeiro.')
        return

    soma_idade = 0
    maiores_idade = []

    for p in dados:
        soma_idade += p['Idade']
        if p['Idade'] >= 18:
            maiores_idade.append(f'\n{p['Nome']} tem {p['Idade']} anos')
    media = soma_idade / len(dados) if dados else 0
                


    print(f'{len(dados)} pessoas foram cadastradas ao sistema.')
    print(f'A média de idade é de {media:.2f}')
    if maiores_idade:
        print(f'Pessoas maiores de 18 anos: { ' '. join(maiores_idade)}')
           
    else:
        print(f'Não há pessoas maiores de 18 anos cadastradas.')
    print()

def buscar_pessoas():
    print()
    print('PESQUISA')
    if not dados:
        print('Nenhuma pessoa cadastrada ainda.')
        print('Cadastre alguma pessoa primeiro.')
        return
    
    while True:
        pesquisa = input('Digite o nome que deseja pesquisa: ')
        pesquisaM = pesquisa.lower().strip()
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
        nova_pesq = input('Deseja fazer uma nova pesquisa? S/N').strip()
        if nova_pesq.lower() == 'S'.lower():
            continue
        else:
            break    

def remove_pessoas():
    print()
    print('REMOVAÇÃO DE DADOS')
    if not dados:
        print('Nenhuma pessoa cadastrada ainda.')
        print('Cadastre alguma pessoa primeiro.')
        return
    
    while True:
        nome_remove = input('Digite o nome que deseja remover do Sistema: ').strip()
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

                    confirmacao = input(f'Tem certeza que deseja remover "{p_real['Nome']}"(Indice Originnal: {id_real})? (S/N): ').lower().strip()
                    if confirmacao == 's':
                        del dados[id_real]
                        print(f'Nome: {p_real['Nome']} removido com sucesso!')
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
                if novo_remove_resposta == 's'.lower():
                    continue # Sai do loop interno e continua o loop principal (volta para 'Digite o nome...')
                else:
                    break # Sai do loop interno
        except ValueError:
                print('Resposta inválida. Por favor, digite S para sim ou N para não.')
       

            

# salvar dados 5 !!

def salvar_arquivos():
    print()
    try:
        with open (caminho_arquivo, 'w') as f:  # salva os dados no arquivo json
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
    global dados
    try:
        with open(caminho_arquivo, 'r') as f:
            dados = json.load(f)
            print('Dados carregados com sucesso!!')
        
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Dados inválido.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar Dados {e}")
        

# sair e salvar 7


def sair_e_salvar():
    salvar_arquivos()
    print('Saindo do Sistema...')
    return False



    # codigo saindo do sistema.

escolha()