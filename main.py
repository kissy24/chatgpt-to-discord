import openai
import discord
from discord.ext import commands

DISCORD_TOKEN = "your-discord-bot-token"
OPENAI_API_KEY = "your-openai-api-key"

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

# OpenAI APIキーの設定
openai.api_key = OPENAI_API_KEY


async def chat_gpt(prompt):
    model_engine = "text-davinci-002"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="chat")
async def chat(ctx, *, user_prompt):
    prompt = f"{user_prompt}"

    try:
        response = await chat_gpt(prompt)
        await ctx.send(response)
    except Exception as e:
        print(e)
        await ctx.send("エラーが発生しました。")


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
