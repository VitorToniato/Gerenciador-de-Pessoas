# Gerenciador-de-Pessoas-

Gerenciador de Pessoas Aprimorado

Descrição do Projeto
Este é um sistema simples, mas robusto, para o gerenciamento de informações de pessoas, desenvolvido em Python. Ele permite aos usuários cadastrar novas pessoas com nome e idade, visualizar estatísticas sobre os cadastros (como número total de pessoas e média de idade, além de listar maiores de 18 anos), buscar pessoas por parte do nome e remover registros específicos. O sistema é operado via console, oferecendo uma interface de menu interativa e intuitiva.
Gerienciador de Pessoas feito em Linguagem Python

Arquivo 'desafio_original.py' é o meu código original.

Arquivo 'desafio.2.0_para_comparação.py' é o código com melhorias onde pedi para a ia Gemini do Google para corrigir, já que ele que me passo esse desafio. E também pedi para ele me passar como tava a minha lógica e meu pontos positivos e negativos. Logo em seguida pedidi para me passar alguns pontos de melhorias e feedbacks para melhorar meu código e as melhorias estão contidas nesse arquivo.

O projeto foi desenvolvido como um desafio de programação para aprimorar habilidades em manipulação de listas, dicionários, tratamento de erros e lógica de controle de fluxo (while, for, match case).

Funcionalidades
O sistema oferece as seguintes opções principais no menu:

[1] Cadastrar Pessoa: Permite adicionar um novo registro com nome e idade. Inclui validação para garantir que a idade seja um número positivo.

[2] Verificações: Exibe estatísticas sobre as pessoas cadastradas, incluindo:

O número total de pessoas no sistema.

A média de idade das pessoas cadastradas.

Uma lista de todas as pessoas maiores de 18 anos.

[3] Buscar Pessoa: Permite pesquisar pessoas por parte do nome (busca "case-insensitive", ou seja, não diferencia maiúsculas de minúsculas). Exibe todos os resultados encontrados e oferece a opção de realizar novas buscas.

[4] Remover Pessoa: Permite remover um ou mais registros de pessoas com base no nome. O sistema lista todas as ocorrências de um nome pesquisado, permitindo ao usuário escolher qual registro remover através de um índice, e solicita confirmação antes da remoção definitiva.

[5] Sair do Sistema: Encerra a execução do programa.

Tecnologias Utilizadas
Linguagem: Python 3.x

Como Rodar o Projeto
Para executar este sistema em sua máquina, siga os passos abaixo:

Pré-requisitos: Certifique-se de ter o Python 3.x instalado em seu computador. Você pode baixá-lo em python.org.

Baixar o Código:

Você pode clonar este repositório usando Git:

Bash

git clone <https://github.com/VitorToniato/Gerenciador-de-Pessoas-.git>
Ou baixar o arquivo gerenciador_pessoas.py (ou o nome que você deu ao seu arquivo principal) diretamente.

Executar o Programa:

Abra o terminal (ou Prompt de Comando/PowerShell no Windows, Terminal no Linux/macOS).

Navegue até o diretório onde você salvou o arquivo do projeto.

Execute o comando:

Bash

python gerenciador_pessoas.py
(Substitua gerenciador_pessoas.py pelo nome do seu arquivo, se for diferente).

Interação: O programa será iniciado e exibirá o menu de opções. Siga as instruções no console para interagir com o sistema.

Estrutura do Código
O código é estruturado de forma modular e clara, utilizando:

while True: Para manter o sistema rodando até que o usuário decida sair.

match case: Para organizar as diferentes opções do menu de forma eficiente e legível (requer Python 3.10+).

Listas de Dicionários: Os dados das pessoas são armazenados em uma lista (dados), onde cada pessoa é um dicionário contendo 'nome' e 'idade'.

Tratamento de Exceções (try-except): Para lidar com entradas inválidas do usuário, garantindo a robustez do sistema.

Funções: Uma função dedicada (exibir_menu()) é usada para apresentar as opções, promovendo a reutilização de código.

Contribuição
Contribuições são bem-vindas! Se você tiver ideias para melhorias, novas funcionalidades ou quiser corrigir algum bug, sinta-se à vontade para:

Fazer um fork (ramificação) do repositório.

Criar uma nova branch (ramo) para sua funcionalidade (git checkout -b minha-nova-feature).

Implementar suas mudanças.

Fazer um commit (git commit -m "Adiciona nova funcionalidade X").

Enviar suas mudanças para o fork (git push origin minha-nova-feature).

Abrir um Pull Request.

Autor
@https://github.com/VitorToniato

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes. 