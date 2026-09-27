import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Você logou como {bot.user}')

@bot.command()
async def poluição(ctx):
    await ctx.send('Os Melhores Carros Híbridos/Elétricos São: \n'
          '╰ `BYD Sealion 7 AWD`\n'
          '╰ `BYD Seal`\n'
          '╰ `Volvo EX30`\n'
          '╰ `GWM Haval H6 PHEV`\n'
          '╰ `Toyota Corolla Hybrid`'
          )

@bot.command()
async def carros(ctx):
    await ctx.send('Os Carros Que Menos Poluem Sem Ser Elétricos São: \n'
                   '╰ `Chevrolet Onix 1.0`\n'
                   '╰ `Chevrolet Onix Plus 1.0`\n'
                   '╰ `Volkswagen Polo 1.0 MPI`\n' 
                   '╰ `Volkswagen Tera 1.0 MPI`\n'
                   '╰ `Renault Kwid 1.0`')

@bot.command()
async def poluição_adultos(ctx):
    await ctx.send('> 🚌 **Usar transporte público:** reduzir a quantidade de carros nas ruas.\n'
        '> 🚗 **Fazer caronas:** diminuir o número de veículos circulando.\n'
        '> 💡 **Economizar energia:** evitar desperdícios de eletricidade.\n'
        '> ♻️ **Separar resíduos:** facilitar a reciclagem e o descarte correto.\n'
        '> 🛒 **Consumir conscientemente:** comprar apenas o necessário e evitar desperdícios.\n'
        '> 🌱 **Apoiar empresas sustentáveis:** incentivar práticas que reduzam impactos ambientais.')

@bot.command()
async def poluição_adolescentes(ctx):
    await ctx.send('> ♻️ **Reciclar:** separar corretamente o lixo.\n'
        '> 🚲 **Usar bicicleta:** diminuir o uso de veículos em trajetos curtos.\n'
        '> 🛍️ **Evitar descartáveis:** reduzir o consumo de plásticos de uso único.\n'
        '> 🌳 **Plantar árvores:** contribuir para melhorar a qualidade do ar.\n'
        '> 📱 **Divulgar conscientização:** compartilhar informações e campanhas ambientais.\n'
        '> 🏫 **Participar de projetos:** ajudar em ações ambientais na escola e na comunidade.')

bot.run('SEU_TOKEN_AQUI')