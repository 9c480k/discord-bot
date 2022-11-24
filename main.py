import os
import discord
import requests

token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_image():
  response = requests.get("https://api.thecatapi.com/v1/images/search")

  
@client.event
async def on_ready():
  print(f"logged in as {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user or message.content[0:2] != "m!": 
    return

  command = message.content[2:]

  if command[0:4] == "spam" and command[5:] != "" and command[4] == " ":
    returnMessage = []
    for i in range(300):
      returnMessage.append(command[5:])

    returnMessage = "\n".join(returnMessage)
    length = len(command[5:]) + 2
    
    while len(returnMessage) > 2000:
      remainder = (2000 // length) * length
      await message.channel.send(returnMessage[:remainder -1])
      
      returnMessage = returnMessage[remainder:] 
      
      if len(returnMessage) <= 2: 
        return

    await message.channel.send(returnMessage)
    
  elif command == "" or command == " ":
    await message.channel.send("command not received")

  elif command == "cat":
    await message.channel.send("yes")
    


client.run(token)