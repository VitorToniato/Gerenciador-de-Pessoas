'''

Desafio: Gerenciador de Pessoas Aprimorado

Objetivo: Adicionar novas funcionalidades ao seu sistema de cadastro para torná-lo mais completo e interativo.

Requisitos:



Menu de Opções Expandido: Adicione as seguintes opções ao seu menu inicial:

[4] Buscar pessoa por nome

[5] Remover pessoa por nome

Funcionalidade de Busca:

Ao escolher a opção [4], o programa deve pedir ao usuário para digitar um nome (ou parte de um nome).

Em seguida, ele deve exibir todas as pessoas cadastradas cujo nome contenha o texto digitado (a busca deve ser "case-insensitive", ou seja, não diferenciar maiúsculas de minúsculas).

Se nenhuma pessoa for encontrada, uma mensagem apropriada deve ser exibida.

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

Se precisar de alguma dica ao longo do caminho, é só perguntar! Boa sorte!

'''