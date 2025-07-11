import json

dados= []

repetir = int(input('Digite quantos nomes deseja inserir: '))


for i in range(1, repetir + 1):
    nome = input('Digite o nome que deseja inserir: ')
    idade = input('Digite sua idade')

    try:
        with open('Teste com Json/pessoas.json', 'r') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError: # caso o arquivo estiver vazio ou invalido.
                dados = []
    except FileNotFoundError:  # caso o arquivo não exista
        dados = []

    
    novo_object = {'Nome': nome, 'Idade': idade}

    # verificação se é lista ou dicionario.

    if isinstance(dados, list):  #  função embutida que verifica se o objeto especificado é uma instância da classe ou de uma subclasse da classe especificada no segundo argumento

        dados.append(novo_object)
    elif isinstance(dados, dict): #  função embutida que verifica se o objeto especificado é uma instância da classe ou de uma subclasse da classe especificada no segundo argumento
        if 'pessoas' not in dados:
            dados['pessoas'] = []
        dados['pessoas'].append(novo_object)
    else:
        print('Formato de arquivo invalido.')
    
    
    with open ('Teste com Json/pessoas.json', 'w') as f:
        json.dump(dados, f, indent = 4)


# usar o códgio acima, passa lo para o código original.


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
                    nova_pesq = input('Deseja fazer uma nova pesquisa? S/N')
                    if nova_pesq.lower() == 'S'.lower():
                        continue
                    else:
                        break
                else:
                    print(f'Nenhum nome encontrado com {pesquisaM}')
                    break


print(dados)
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