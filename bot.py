import os
import discord
import cohere
from dotenv import load_dotenv

load_dotenv()
cohere_client = cohere.Client(os.getenv('COHERE_API_KEY'))

intents = discord.Intents.default()
intents.message_content = True
discord_client = discord.Client(intents=intents)

@discord_client.event
async def on_ready():
    print(f'We have logged in as {discord_client.user}')

@discord_client.event
async def on_message(message):
    if discord_client.user.mentioned_in(message) and not message.author.bot:
        prompt = message.content.replace(f'<@{discord_client.user.id}>', '').strip()
        
        if prompt:
            try:
                response = cohere_client.generate(
                    model='command',
                    prompt=message.content,
                    max_tokens=500
                )
                print(response)
                reply = response.generations[0].text
                await message.channel.send(reply)
            except Exception as e:
                print(f"Error: {e}")
                await message.channel.send("Sorry, I encountered an error. Please try again later.")
        else:
            await message.channel.send("I'm here! You can ask me anything and I will try my best to respond.")

discord_client.run(os.getenv('DISCORD_BOT_TOKEN'))
