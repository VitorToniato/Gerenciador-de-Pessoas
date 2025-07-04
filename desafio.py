
'''
Desafio: Gerenciador de Pessoas Aprimorado
Objetivo: Adicionar novas funcionalidades ao seu sistema de cadastro para torná-lo mais completo e interativo.
Requisitos:
Menu de Opções Expandido: Adicione as seguintes opções ao seu menu inicial:
[5] Remover pessoa por nome
Funcionalidade de Remoção:
Ao escolher a opção [5], o programa deve pedir ao usuário para digitar o nome da pessoa a ser removida.
Se encontrar a pessoa (pelo nome exato, também "case-insensitive"), ela deve ser removida da lista dados.
Exiba uma mensagem de sucesso ou de falha (caso a pessoa não seja encontrada).
Importante: Se houver nomes duplicados, você pode decidir se remove apenas o primeiro encontrado ou todos. Para simplificar, pode remover apenas o primeiro.
Reforço na Validação:
Garanta que, ao tentar buscar ou remover pessoas, o programa lide bem com a lista dados vazia.
Dicas para te ajudar:
Para a busca e remoção "case-insensitive", você pode converter tanto o nome digitado pelo usuário quanto os nomes armazenados na sua lista para minúsculas (ou maiúsculas) antes de comparar. Por exemplo: nome_digitado.lower() e p['nome'].lower().
Para remover um item de uma lista enquanto itera sobre ela, pode ser um pouco complicado. Uma estratégia comum é criar uma nova lista com os itens que você quer manter, ou iterar sobre uma cópia da lista se precisar remover elementos diretamente. Ou, ainda mais simples para este caso, usar um for loop com enumerate para ter o índice do item a ser removido e depois usar del dados[indice].
'''

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
                    maiores_idade.append(f'{p['nome']} tem {p['idade']} anos\n')
            media = soma_idade / len(dados)


            print(f'{len(dados)} foram cadastradas ao sistema.')
            print(f'A média de idade é de {media:.2f}')

            if maiores_idade:
                print(f'Pessoas maiores de 18 anos: { ', '. join(maiores_idade)}')
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
                        print(f'- Nome: {p['nome']},{p['idade']}')
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
                   print(f'[{i}] - Índice: {indice} | Nome: {p['nome']} | Idade: {p['idade']}')

                try:
                    verificacao = int(input('Digite o indice do nome que deseja remover: '))
                    if 0 <= verificacao < len(achados):
                        id_real = achados[verificacao][0]
                        p_real = achados[verificacao][1]
                        confirmacao = input(f'Tem certeza que deseja remover "{p_real['nome']}"(Indice Originnal: {id_real})? (S/N): ').lower()
                        if confirmacao == 's':
                            del dados[id_real]
                            print(f'Nome: {p_real['nome']} removido com sucesso!')
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