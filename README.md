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

## Explicações para desenvolvimento
### async
O `async` é uma palavra-chave em Python que define funções assíncronas. Funções assíncronas permitem que o programa execute outras tarefas enquanto espera por operações demoradas, como os acessos a API do Discord que estamos fazendo.

### await
O `await` é utilizado dentro de funções assíncronas para esperar pela conclusão de uma função assíncrona. Quando ela é concluída o resto do código embaixo dela na função continua.

### Intents do Discord
`Intents` no Discord definem quais eventos seu bot receber. O Discord requer que os bots definam explicitamente os eventos que desejam monitorar, como mensagens, reações ou entradas/saídas de membros.

### Anotações (@) em Python 
As anotações (ou "decorators") são funções que podem modificar o comportamento de outras funções ou métodos. Em Python, elas são indicadas pelo símbolo `@` e usadas em bibliotecas como a Discord.py.


## Como mandar mensagems
Para mandar mensagens privadas para o bot, basta adicionar o prefixo `!` antes da mensagem.
Para mandar mensagens para o bot no canal, basta mandar a mensagem normalmente.

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
