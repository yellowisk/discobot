from os import getenv
from dotenv import load_dotenv
from discord import Intents, Client, Message, Integration, app_commands
from respostas import obter_resposta
from discobot.hard_coded_funcs import por_promocao, por_nome, por_nota, por_genero, gen_mensagem
from asyncio import run

intents = Intents.default()
cliente: Client = Client(intents=intents)
arvore = app_commands.CommandTree(cliente)


# Função para enviar mensagens
async def enviar_mensagem(mensagem: Message, mensagem_do_usuario):
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
    await interacao.response.send_message('Hello, Worlds!')

@arvore.command(name='jogos_por_genero')
@app_commands.describe(genre='Gênero do jogo')
async def jogos_por_genero(interacao: Integration, genre: str):
    jogos = por_genero(genre)
    mensagem = gen_mensagem(jogos)
    await interacao.response.send_message(mensagem)
    
@arvore.command(name='jogos_em_promocao')
@app_commands.describe(promocao='Se o jogo está em promoção')
async def jogos_em_promocao(interacao: Integration, promocao: bool):
    jogos = por_promocao(promocao)
    mensagem = gen_mensagem(jogos)
    await interacao.response.send_message(mensagem)
    
@arvore.command(name='jogo_por_nome')
@app_commands.describe(nome='Nome do jogo')
async def jogo_por_nome(interacao: Integration, nome: str):
    jogos = por_nome(nome)
    mensagem = gen_mensagem(jogos)
    await interacao.response.send_message(mensagem)
    
@arvore.command(name='jogos_por_nota')
@app_commands.describe(nota_min='Nota mínima', nota_max='Nota máxima')
async def jogos_por_nota(interacao: Integration, nota_min: float, nota_max: float):
    jogos = por_nota(nota_min, nota_max)
    mensagem = gen_mensagem(jogos)
    await interacao.response.send_message(mensagem)


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

    await enviar_mensagem(mensagem, mensagem.content)


def main():
    TOKEN = getenv('DISCORD_TOKEN')
    cliente.run(token=TOKEN)


if __name__ == '__main__':
    load_dotenv()
    run(main())