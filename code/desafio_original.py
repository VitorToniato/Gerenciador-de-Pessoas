import json

#  aviso de alteração, adicionar def.

print('==========================')
print('|   CADASTRO DE PESSOAS  |')
print('|   OPÇÕES DE ESCOLHA    |')
print('|   [1] Cadastra pessoa  |')
print('|   [2] Verificações     |')
print('|   [3] Buscar pessoa    |')
print('|   [4] Remover Pessoa   |')
print('|   [5] Sair do Sistema  |')
print('==========================')
'\n'
dados = []

while True:
    try:
        escolha = int(input('Escolha qual opção você quer: '))
    except ValueError:
        print('Entrada Inválida, digite um números.')
        continue

    match escolha:

        case 1:
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

        # verificações e ações
        case 2:
            if not dados:
                print('Nenhuma pessoa cadastrada ainda.\n')
                continue
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
            else:
                print(f'Não há pessoas maiores de 18 anos cadastradas.')
            print()
    

        # pesquisa de nomes.
        case 3:
            while True:
                pesquisa = input('Digite o nome que deseja pesquisa: ')
                pesquisaM = pesquisa.lower()
                achados = []

                for p in dados:
                    nome_pessoas = p['nome']; nome_pessoasM = nome_pessoas.lower()

                    if pesquisaM in nome_pessoasM:
                        achados.append(p)
                if achados:
                    print('Nomes encontrados:')
                    for p in achados:
                        print(f'- Nome: {p['nome']}, Idade: {p['idade']} anos.')
                    nova_pesq = input('Deseja fazer uma nova pesquisa? S/N')
                    if nova_pesq.lower() == 'S'.lower():
                        continue
                    else:
                        break
                else:
                    print(f'Nenhum nome encontrado com {pesquisaM}')
                    break

        # opção de remover um nome.           
        case 4:
            nome_remove = input('Digite o nome que deseja remover do Sistema: ')
            achados = []

            for indice, p in enumerate(dados):
                if 'nome' in  p:

                    if nome_remove.lower() in p['nome'].lower():
                        achados.append((indice, p))
            
            if achados:
                print('Nomes encontrados: ')
                for i, (indice, nome_achado) in enumerate(achados):
                   print(f'[{i}] - Índice: {indice} | Nome: {nome_achado['nome']} | Idade: {nome_achado['idade']}')

                try:
                    verificacao = int(input('Digite o indice do nome que deseja remover: '))
                    if 0 <= verificacao < len(achados):
                        id_real = achados[verificacao][0]
                        p_real = achados[verificacao][1]

                        confirmacao = input(f'Tem certeza que deseja remover "{p_real['nome']}"(Indice Originnal: {id_real})? (S/N): ').lower()
                        if confirmacao == 's':
                            del dados[id_real]
                            print(f'Nome: {p_real['nome']} removido com sucesso!')
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
                novo_remove_resposta = input('Deseja remover algum outro nome do sistema? (S/N): ').lower().strip()
                if novo_remove_resposta == 's':
                    continue # Sai do loop interno e continua o loop principal (volta para 'Digite o nome...')
                elif novo_remove_resposta == 'n':
                    break # Sai do loop interno
                else:
                    print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")

            else:
                print(f'Nenhum nome encontrado com {nome_remove}')
                break
                
            
        # opção de sair do programa.      
        case 5:
            print('Saindo do Programa. Até mais!')
            break