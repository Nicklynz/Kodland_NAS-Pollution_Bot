import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def fakta(ctx):
    facts = ['91% populasi dunia menghirup udara yang terpolusi setiap hari',
             'Setidaknya 1 dari 10 orang meninggal karena penyakit terkait polusi udara',
             'Polusi udara merupakan ancaman lebih besar terhadap harapan hidup dibandingkan merokok, hiv atau perang',
             'Polusi udara menimbulkan kerugian ekonomi hampir $3 triliun, setara dengan 3,3% GDB dunia',
             'Polusi udara berkontribusi pada penyebaran covid-19',
             ]
    fact = random.choice(facts)
    await ctx.send(f'Fakta : {fact}')

@bot.command()
async def mitos(ctx):
    myths = ['Pengharum ruangan meningkatkan kualitas udara.\nApa yang mereka lakukan adalah membantu menyamarkan bau dengan menutupinya dengan wewangian lain.',
             'Jamur hanya menjadi masalah di iklim lembab.\nJamur dapat berkembang di lingkungan dalam ruangan mana pun dengan tingkat kelembapan tinggi.',
             'Alergi adalah indikator utama kualitas udara dalam ruangan yang buruk.\nMeskipun alergi dapat diperburuk oleh kualitas udara dalam ruangan yang buruk, alergi bukanlah satu-satunya indikator terbaik.',
             'Polusi udara hanya menjadi masalah di perkotaan.\nPolusi udara dalam ruangan dapat menjadi masalah di mana pun lokasinya.',
             'Produk pembersih berlabel “hijau” aman. \nBeberapa produk “ramah lingkungan” masih mengandung bahan kimia berbahaya, termasuk VOC.',
             'Alat pembersih udara menghilangkan semua polutan udara dalam ruangan.\nMeskipun alat pembersih udara dapat mengurangi polutan udara tertentu dalam ruangan, alat ini tidak menghilangkan semua polutan.',
             'Kualitas udara dalam ruangan bukanlah masalah kesehatan yang signifikan.\nKualitas udara dalam ruangan yang buruk berkontribusi terhadap 4,3 juta kematian dini di seluruh dunia setiap tahunnya.'
             ]
    myth = random.choice(myths)
    await ctx.send(f'Mitos : {myth}')

@bot.command()
async def something(ctx):
    test = 0

    

bot.run("TOKEN")
