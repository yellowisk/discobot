from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Integration, app_commands
from responses import get_response

load_dotenv()
TOKEN: Final = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True #NQA
client: Client = Client(intents=intents)
tree = app_commands.CommandTree(client)

# SEND A MESSAGE
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Empty cuz intents were probably not enabled')
        return
    
    if user_message.startswith('!'):
        response: str = get_response(user_message[1:])
        await message.author.send(response)
        
    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)
        
@tree.command(name='hello')
async def hello(interaction: Integration) -> None:
    await interaction.response.send_message('Hello! How are you?')
    
@tree.command(name='speak')
@app_commands.describe(thing_to_say='The message to say', to_user='The user to say the message to')
async def speak(interaction: Integration, thing_to_say: str, to_user: str) -> None:
    await interaction.response.send_message(thing_to_say + ' para: ' + to_user)
    
@tree.command(name='send_to_user')
@app_commands.describe(message='The message to send', user='The user to send the message to')
async def send_to(interaction: Integration, message: str, user: str) -> None:
    guild = interaction.guild
    if guild is None:
        await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
        return
    
    member = guild.get_member_named(user)
    if member is None:
        await interaction.response.send_message(f"User '{user}' not found in this server.", ephemeral=True)
        return

    try:
        await member.send(message)
        await interaction.response.send_message(f"Message sent to {user}.", ephemeral=True)
    except Exception as e:
        print(e)
        await interaction.response.send_message("Failed to send message. Please check my permissions.", ephemeral=True)

    
        
# HANDLE THE STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')
    await tree.sync()
    
# HANDLE THE MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = message.author.name
    user_message: str = message.content
    channel: str = message.channel.name
    
    print(f'[{channel}] {username}: "{user_message}"')

    await send_message(message, message.content)

def main() -> None:
    client.run(token=TOKEN)
    
if __name__ == '__main__':
    main()