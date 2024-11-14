import os
import cohere
import discord
from dotenv import load_dotenv

import search

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
                response = search.search_rules(prompt)
                if len(response)>0:
                    for result in response:
                        reply = "## " + result["title"] + "\n"
                        reply += result["text"]
                        print(reply)
                        await message.channel.send(reply)
                else:
                    response = cohere_client.generate(
                        model='command',
                        prompt=message.content,
                        max_tokens=500
                    )
                    print(response)
                    reply = response.generations[0].text
                    await message.channel.send(reply)
                    # await message.channel.send("I don't have enough information on the given query.")
            except Exception as e:
                print(f"Error: {e}")
                await message.channel.send("Sorry, I encountered an error. Please try again later.")
        else:
            await message.channel.send("I'm here! You can ask me anything and I will try my best to respond.")

discord_client.run(os.getenv('DISCORD_BOT_TOKEN'))
