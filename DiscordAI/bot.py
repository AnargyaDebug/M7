import discord
from discord.ext import commands
from ClassificationModel.model import get_class

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

def get_img():
    img = "input/test.png"
    return img

@bot.command()
async def input_image(ctx):
    url = get_img()
    await ctx.send(url)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(get_class(model_path="./ClassificationModel/keras_model.h5", labels_path="ClassificationModel/labels.txt", image_path=f"./{file_name}"))
    else:
        await ctx.send("You forgot to upload the image >:(")
