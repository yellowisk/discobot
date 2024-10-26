Esse projeto é destinado ao ensino de programação em Python para alunos do projeto "Olá, Mundos!" da Conpec.

Neste projeto, os alunos desenvolveram um bot do Discord que realiza ações simples, como responder a mensagens e executar comandos.

## Como rodar o projeto
1. Clone o repositório
2. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
DISCORD_TOKEN
```
3. Preencha o arquivo `.env` com o token do seu bot do Discord
4. Execute o arquivo `main.py`

## Comandos
- `/hello`: O bot responde com "Hello, Worlds!"
- `/speak <texto>`: O bot repete o texto passado como argumento
- `/enviar_para <mensagem> <usuario>`: O bot envia uma mensagem para o usuário mencionado
- `/matematica <operacao> <numero1> <numero2>`: O bot realiza a operação matemática passada como argumento com os números passados como argumento
- `/ordenar <numeros>`: O bot ordena os números passados como argumento
- `/sortear <numeros>`: O bot sorteia um número entre os números passados como argumento
- `/jokenpo <jogada>`: O bot joga jokenpo com o usuário
- `/moeda`: O bot joga cara ou coroa
- `/dado <numero>`: O bot joga um dado de 6 faces ou de um número de faces passado como argumento
- `/ping`: O bot responde com "Pong!"
- `/help`: O bot responde com a lista de comandos disponíveis
