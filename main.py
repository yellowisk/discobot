from os import getenv
from dotenv import load_dotenv
from discord import Intents, Client, Message, Integration, app_commands
from respostas import obter_resposta


load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')


intents = Intents.default()
intents.message_content = True # Necessário para receber mensagens
intents.members = True # Necessário para acessar membros do servidor
cliente: Client = Client(intents=intents)
arvore = app_commands.CommandTree(cliente)


# Função para enviar mensagens
async def send_message(mensagem: Message, mensagem_do_usuario):
    if not mensagem_do_usuario:
        print('Mensagem vazia')
        return
    
    if mensagem_do_usuario.startswith('!'):
        resposta = obter_resposta(mensagem_do_usuario[1:])
        await mensagem.author.send(resposta)
        
    try:
        resposta = obter_resposta(mensagem_do_usuario)
        await mensagem.channel.send(resposta)
    except Exception as e:
        print(e)


@arvore.command(name='hello')
async def hello(interacao: Integration):
    await interacao.response.send_message('Hello, worlds!')


@arvore.command(name='speak')
@app_commands.describe(o_que_dizer='O que dizer')
async def speak(interacao: Integration, o_que_dizer: str):
    await interacao.response.send_message(o_que_dizer)


@arvore.command(name='enviar_para')
@app_commands.describe(mensagem='Mensagem a ser enviada', usuario='Usuário a receber a mensagem')
async def send_to(interacao: Integration, mensagem: str, usuario: str):
    guild = interacao.guild
    if guild is None:
        await interacao.response.send_message("Esse comando só pode ser usado em servidores.", ephemeral=True)
        return
    
    membro = guild.get_member_named(usuario)
    if membro is None:
        await interacao.response.send_message(f"Usuário {usuario} não encontrado.", ephemeral=True)
        return

    try:
        await membro.send(mensagem)
        await interacao.response.send_message(f"Mensagem enviada para {usuario}.", ephemeral=True)
    except Exception as e:
        print(e)
        await interacao.response.send_message(f"Erro ao enviar mensagem para {usuario}. Cheque minhas permissões.", ephemeral=True)

@arvore.command(name='matematica')
@app_commands.describe(numero1='Primeiro número', operacao='Operação matemática', numero2='Segundo número')
async def matematica(interacao: Integration, numero1: int, operacao: str, numero2: int):
    return # Implementar função
    
@arvore.command(name='ordenar_numeros')
@app_commands.describe(numeros='Números a serem ordenados')
async def ordenar_numeros(interacao: Integration, numeros: str):
    return # Implementar função


# CONECTAR AO DISCORD
@cliente.event
async def on_ready():
    print(f'{cliente.user} se conectou ao Discord!')
    await arvore.sync()

  
# GERENCIAR MENSAGENS
@cliente.event
async def on_message(mensagem):
    if mensagem.author == cliente.user:
        return
    
    username = mensagem.author.name
    mensagem_do_usuario = mensagem.content
    canal = mensagem.channel.name
    
    print(f'[{canal}] {username}: {mensagem_do_usuario}')

    await send_message(mensagem, mensagem.content)


def main():
    cliente.run(token=TOKEN)


if __name__ == '__main__':
    main()