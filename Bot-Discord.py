import discord
from discord.ext  import commands


intents = discord.Intents().all()
bot = commands.Bot(command_prefix="$", intents=intents)

intents.message_content = True
intents.guilds = True
intents.members = True

# message de connexion
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

# Deconnexion du bot
@bot.command(name="exit")
async def exit(ctx):

    reponse = "Bot déconnecté. Bye Bye !"
    await ctx.reply(reponse)
    await bot.close()

    print(f"Réponse à message {ctx.message.id} : {reponse}")

# fonction de test
@bot.command(name="coucou")
async def bonjour(ctx):

    reponse = f"Ça va, {ctx.message.author.name} ?"
    await ctx.reply(reponse)

    # print(f"Réponse à message {ctx.message.id} : {reponse}")

@bot.command(name="somme")
async def somme(ctx,val1:int,val2:int):

    reponse = f"{val1} + {val2} = {val1+val2}"
    await ctx.reply(reponse)

    # print(f"Réponse à message {ctx.message.id} : {reponse}")


bot.run("TOKEN") # Rentrer son token