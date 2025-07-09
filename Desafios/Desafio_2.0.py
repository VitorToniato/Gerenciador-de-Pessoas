'''

Desafio: Persistência de Dados (Gerenciador de Pessoas com Arquivos)

Objetivo

Modificar seu sistema de gerenciamento de pessoas para que ele possa salvar os dados em um arquivo e carregá-los ao iniciar, garantindo que as informações persistam entre as sessões do programa.

Requisitos

Novas Opções no Menu:

Adicione uma nova opção ao seu menu inicial:

[6] Salvar Dados

[7] Carregar Dados

A opção [5] Sair do Sistema deve ser mantida, mas com uma alteração importante (veja abaixo).

Funcionalidade de Salvar Dados (Opção 6):

Quando o usuário escolher esta opção, o programa deve salvar a lista dados em um arquivo.

Sugestão de formato: JSON (JavaScript Object Notation) é ideal para isso, pois é fácil de ler e Python tem módulos nativos para trabalhar com ele. O nome do arquivo pode ser pessoas.json.

Exiba uma mensagem de sucesso ou falha após a tentativa de salvamento.

Dica: O módulo json em Python possui json.dump() para escrever dados Python em um arquivo JSON.

Funcionalidade de Carregar Dados (Opção 7):

Quando o usuário escolher esta opção, o programa deve tentar carregar os dados do arquivo pessoas.json (ou o nome que você escolheu).

Se o arquivo não existir, exiba uma mensagem informando que não há dados para carregar e que a lista está vazia.

Se o arquivo existir, carregue os dados na sua lista dados.

Exiba uma mensagem de sucesso ou falha.

Importante: Ao carregar, os dados existentes na lista dados (se houver) devem ser substituídos pelos dados do arquivo.

Dica: O módulo json possui json.load() para ler dados de um arquivo JSON para Python.

Carregamento Automático ao Iniciar:

Quando o programa iniciar, ele deve tentar carregar automaticamente os dados do arquivo pessoas.json.

Se o arquivo existir, os dados serão carregados e o programa começará com as informações anteriores.

Se o arquivo não existir, o programa deve iniciar com a lista dados vazia, como tem sido até agora.

Esta operação inicial deve ser "silenciosa", sem pedir ao usuário explicitamente para carregar, apenas informando se carregou algo ou se a lista está vazia.

Perguntar para Salvar ao Sair (Opção 5):

Antes de o programa realmente sair (quando o usuário escolher a opção [5]), ele deve perguntar ao usuário se ele deseja salvar os dados atuais.

Se o usuário confirmar, o programa deve chamar a funcionalidade de salvar dados antes de encerrar.

Se o usuário negar, o programa simplesmente encerra.

Se o usuário digitar uma resposta inválida (nem 's' nem 'n'), você pode pedir novamente ou simplesmente não salvar e sair.

'''