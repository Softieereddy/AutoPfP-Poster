from asyncore import loop
import random
import time
import discord
from discord.ext import commands

tostop = 0

intents = discord.Intents.all()

TOKEN = "MTA3NzExNTk3NjUwNTYyMjUyOA.Gc1T-z.LFf3yXkbWKOAu5ckNiojEpy5UIzOUiJaYSUwSA"
tecno = commands.Bot(command_prefix="r",intents=intents)

def randnum(fname):
    lines=open(fname).read().splitlines()
    return random.choice(lines)

@tecno.event
async def on_ready():
    print(f"Connected to {tecno.user}")
    print(f"Bot ID : {tecno.user.id}")
allowed = ["1028331742903402538,985054981910581288"]

@tecno.command()
async def stop(ctx):
  global tostop
  if ctx.author.id == 1028331742903402538 or ctx.author.id == 1064338256830943292:
    tostop += 1
    await ctx.reply("**✅ Succesfully Stopped AutoPfP**")
  else:
    await ctx.reply("unauthorised")

@tecno.command()
async def sendpfps(ctx):
    global tostop
    if ctx.author.id == 1028331742903402538 or ctx.author.id == 1064338256830943292:
        tostop = 0
        await ctx.reply("**✅ Successfully Started AutoPfP**")
        while tostop == 0:
            
            embed = discord.Embed(title = f"Autopfp",description = "",color = 0x6509f5)
            embed.set_image(url = randnum('scraped.txt'))
            embed.set_footer(text =  "discord.gg/kimdzz")
            await ctx.send(embed=embed)
            time.sleep(3)
    else:
        await ctx.send("unauthorised")

tecno.run(TOKEN)