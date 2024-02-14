import discord
import asyncio
import llama_cpp
import os
import requests


# Replace these values with your actual Discord application details
your_discord_client_id = '914748460861894677'
your_discord_bot_token = 'OTE0NzQ4NDYwODYxODk0Njc3.GwiRDQ.Cgnkvt07j3z_aQHTykEKOvxfF_VQw_sesNdvw4'

# Create Intents
intents = discord.Intents.all()

# Creating the Discord Client with Intents
client = discord.Client(intents=intents)

# Replace 'path/to/model' with the actual path to your Llama model
model_path = "Model"

n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.
n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.

# Make sure the model path is correct for your system!
llm = llama_cpp.Llama(
    model_path=model_path,
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    verbose=True,  # Verbose is required to pass to the callback manager
)

# Define a function for sending messages to Discord channels
async def send_message(channel_id, message):
    channel = client.get_channel(int(channel_id))
    await channel.send(message)

# Define a function for prompting AI using Llama.cpp
async def prompt_ai(prompt):
    return llm.create_chat_completion(messages=[{"role": "user", "content": prompt}])

# Discord Bot Event: on_ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('------')

# Discord Bot Event: on_message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ask '):
        # Extract the prompt from the message content
        prompt = message.content[len('!ask '):].strip()

        # Prompt AI using Llama.cpp
        ai_response = await prompt_ai(prompt)

        # Extract the content of the assistant's message
        assistant_message = ai_response['choices'][0]['message']['content']

        # Send the AI response back to the Discord channel
        await send_message(message.channel.id, f"{assistant_message}")

        # Add the received message to your processing logic
        received_message = message.content
        # Process the received message here (add your logic)
        print(f"Received message: {received_message}")

# Run the Discord bot
client.run(your_discord_bot_token)
