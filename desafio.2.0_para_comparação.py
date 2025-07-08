def exibir_menu():
    """Exibe o menu de opções do sistema de cadastro de pessoas."""
    print('==========================')
    print('|   CADASTRO DE PESSOAS  |')
    print('|   OPÇÕES DE ESCOLHA    |')
    print('|   [1] Cadastrar pessoa |')
    print('|   [2] Verificações     |')
    print('|   [3] Buscar pessoa    |')
    print('|   [4] Remover Pessoa   |')
    print('|   [5] Sair do Sistema  |')
    print('==========================')

dados = [] # Lista para armazenar os dados das pessoas

while True:
    exibir_menu() # Exibe o menu a cada iteração do loop principal
    try:
        escolha = int(input('Escolha qual opção você quer: '))
    except ValueError:
        print('Entrada Inválida. Por favor, digite um número.')
        continue # Volta para o início do loop principal para pedir a escolha novamente

    match escolha:
        case 1: # Cadastrar pessoa
            nome = input('Digite um nome: ').strip()
            while True: # Loop para garantir que a idade seja válida
                try:
                    idade = int(input('Digite a idade da pessoa: '))
                    if idade < 0:
                        print('Idade não pode ser negativa. Tente novamente!')
                        continue # Pede a idade novamente
                    break # Sai do loop da idade se for válida
                except ValueError:
                    print('Idade Inválida. Por favor, digite um número inteiro!')
            
            dados.append({'nome': nome, 'idade': idade})
            print('Pessoa cadastrada com sucesso!\n')

        case 2: # Verificações e ações
            if not dados:
                print('Nenhuma pessoa cadastrada ainda.\n')
                continue # Volta para o menu principal
            
            soma_idade = 0
            maiores_idade = []

            for p in dados:
                soma_idade += p['idade']
                if p['idade'] >= 18:
                    maiores_idade.append(f'\n{p['nome']} tem {p['idade']} anos')
            
            media = soma_idade / len(dados) if dados else 0 # Evita divisão por zero se dados ficar vazio entre operações

            print(f'{len(dados)} pessoas foram cadastradas no sistema.')
            print(f'A média de idade é de {media:.2f} anos.')

            if maiores_idade:
                print(f'Pessoas maiores de 18 anos: {' '.join(maiores_idade)}')
            else:
                print('Não há pessoas maiores de 18 anos cadastradas.')
            print()

        case 3: # Buscar pessoa por nome
            if not dados:
                print('Nenhuma pessoa cadastrada ainda para buscar.\n')
                continue # Volta para o menu principal

            while True: # Loop para permitir múltiplas buscas ou sair da funcionalidade
                pesquisa = input('Digite o nome que deseja pesquisar: ').lower().strip()
                achados = []

                for p in dados:
                    if pesquisa in p['nome'].lower():
                        achados.append(p)

                if achados:
                    print('\nNomes encontrados:')
                    for p in achados:
                        print(f'- Nome: {p['nome']}, Idade: {p['idade']} anos.')
                    
                    # Pergunta se quer fazer nova pesquisa e valida a resposta
                    while True:
                        nova_pesquisa_resposta = input('\nDeseja fazer uma nova pesquisa? (S/N): ').lower().strip()
                        if nova_pesquisa_resposta == 's':
                            break # Sai deste loop e volta para o início do 'while True' de busca
                        elif nova_pesquisa_resposta == 'n':
                            break # Sai deste loop e do 'while True' de busca
                        else:
                            print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
                    
                    if nova_pesquisa_resposta == 'n':
                        break # Sai do loop 'while True' da busca e volta para o menu principal
                else:
                    print(f'\nNenhum nome encontrado que contenha "{pesquisa}".')
                    # Pergunta se quer tentar outra pesquisa e valida a resposta
                    while True:
                        tentar_outra = input('Deseja tentar outra pesquisa? (S/N): ').lower().strip()
                        if tentar_outra == 's':
                            break # Sai deste loop e volta para o início do 'while True' de busca
                        elif tentar_outra == 'n':
                            break # Sai deste loop e do 'while True' de busca
                        else:
                            print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
                    
                    if tentar_outra == 'n':
                        break # Sai do loop 'while True' da busca e volta para o menu principal

        case 4: # Remover pessoa por nome
            if not dados:
                print('Nenhuma pessoa cadastrada ainda para remover.\n')
                continue # Volta para o menu principal

            while True: # Loop para permitir múltiplas remoções ou sair da funcionalidade
                nome_remove = input('Digite o nome da pessoa que deseja remover: ').lower().strip()
                achados = []

                # Coleta todas as ocorrências do nome (case-insensitive) e seus índices originais
                for indice, p in enumerate(dados):
                    if nome_remove in p['nome'].lower():
                        achados.append((indice, p)) # Armazena (índice original, dicionário da pessoa)
                
                if achados:
                    print('\nNomes encontrados:')
                    for i, (original_idx, pessoa_encontrada) in enumerate(achados):
                        # i é o índice na lista 'achados', original_idx é o índice na lista 'dados'
                        print(f'[{i}] - Nome: {pessoa_encontrada['nome']}, Idade: {pessoa_encontrada['idade']} anos. (Índice Original na lista: {original_idx})')

                    try:
                        while True: # Loop para garantir que um índice válido seja digitado
                            verificacao = int(input('Digite o número [] da pessoa que deseja remover: '))
                            
                            if 0 <= verificacao < len(achados):
                                id_real = achados[verificacao][0] # Pega o índice original da lista 'dados'
                                p_real = achados[verificacao][1] # Pega o dicionário da pessoa

                                while True: # Loop para validar a confirmação S/N
                                    confirmacao = input(f'Tem certeza que deseja remover "{p_real['nome']}"? (S/N): ').lower().strip()
                                    if confirmacao == 's':
                                        del dados[id_real]
                                        print(f'"{p_real['nome']}" removido com sucesso!')
                                        break # Sai do loop de confirmação
                                    elif confirmacao == 'n':
                                        print('Remoção cancelada.')
                                        break # Sai do loop de confirmação
                                    else:
                                        print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
                                
                                break # Sai do loop de validação do índice 'verificacao'
                            else:
                                print('Número inválido. Por favor, digite um número que esteja na lista dos itens encontrados.')
                                # Não quebra, continua o loop para pedir o índice novamente
                    
                    except ValueError:
                        print('Erro de digitação. Por favor, digite apenas números para o índice.')
                        # Não quebra, continua o loop 'while True' de remoção para tentar novamente
                    
                    # Após tentar remover (seja com sucesso, cancelado ou erro de input), pergunta se quer remover outro
                    while True: # Loop para validar a resposta S/N
                        novo_remove_resposta = input('\nDeseja remover algum outro nome do sistema? (S/N): ').lower().strip()
                        if novo_remove_resposta == 's':
                            break # Sai deste loop e volta para o início do 'while True' de remoção
                        elif novo_remove_resposta == 'n':
                            break # Sai deste loop e do 'while True' de remoção
                        else:
                            print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
                    
                    if novo_remove_resposta == 'n':
                        break # Sai do loop 'while True' da remoção e volta para o menu principal

                else: # Se 'achados' estiver vazio, ou seja, nenhum nome encontrado com a pesquisa
                    print(f'\nNenhum nome encontrado que contenha "{nome_remove}".')
                    while True: # Loop para validar a resposta S/N
                        continuar_remocao = input('Deseja tentar remover outro nome? (S/N): ').lower().strip()
                        if continuar_remocao == 's':
                            break # Sai deste loop e volta para o início do 'while True' de remoção
                        elif continuar_remocao == 'n':
                            break # Sai deste loop e do 'while True' de remoção
                        else:
                            print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
                    
                    if continuar_remocao == 'n':
                        break # Sai do loop 'while True' da remoção e volta para o menu principal
        
        case 5: # Sair do programa
            print('Saindo do Programa. Até mais!')
            break # Sai do loop principal, encerrando o programa
        
        case _: # Opção inválida
            print('Opção inválida. Por favor, escolha uma opção entre 1 e 5.\n')