import discord
from discord.ext import commands

client = commands.Bot(command_prefix="*")

horoscopes = ["Aries :21 March – 20 April ; Courageous, determined, confident, enthusiastic, optimistic, honest, passionate.",
"Taurus:20 April – 21 May ;  Reliable, patient, practical, devoted, responsible, stable. ",
"Gemini:21 May – 21 June ; Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas",
"Cancer:21 June – 23 July ; tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive",
"Leo:July 23 – August 22 ; Creative, passionate, generous, warm-hearted, cheerful, humorous",
"Virgo:August 23 – September 22 ; Loyal, analytical, kind, hardworking, practical",
"Libra:September 23 – October 22 ; Cooperative, diplomatic, gracious, fair-minded, social",
"Scorpio:October 23 – November 21 ; Resourceful, brave, passionate, stubborn, a true friend",
"Sagittarius: November 22 – December 21 ;  Generous, idealistic, great sense of humor",
"Capricorn:December 22 – January 19 ; Responsible, disciplined, self-control, good managers",
"Aquaris:January 20 – February 18 ; Progressive, original, independent, humanitarian",
"Pisces: February 19 – March 20 ; Compassionate, artistic, intuitive, gentle, wise, musical"
]

@client.event
async def on_ready():
    print("I am ready for you")

@client.command()
async def horoscope(ctx,*,number):
	await ctx.send(horoscopes[int(number)-1])

@client.command()
async def horoscopesall(ctx):
	await ctx.send("--Aries :21 March – 20 April ; Courageous, determined, confident, enthusiastic, optimistic, honest, passionate.\n--Taurus:20 April – 21 May ;  Reliable, patient, practical, devoted, responsible, stable. ,\n--Gemini:21 May – 21 June ; Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas ,\n--Cancer:21 June – 23 July ; tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive , \n--Leo:July 23 – August 22 ; Creative, passionate, generous, warm-hearted, cheerful, humorous , \n--Virgo:August 23 – September 22 ; Loyal, analytical, kind, hardworking, practical , \n--Libra:September 23 – October 22 ; Cooperative, diplomatic, gracious, fair-minded, social ,\n--Scorpio:October 23 – November 21 ; Resourceful, brave, passionate, stubborn, a true friend,\n--Sagittarius: November 22 – December 21 ;  Generous, idealistic, great sense of humor,\n--Capricorn:December 22 – January 19 ; Responsible, disciplined, self-control, good managers,\n--Aquaris:January 20 – February 18 ; Progressive, original, independent, humanitarian,\n--Pisces: February 19 – March 20 ; Compassionate, artistic, intuitive, gentle, wise, musical")

@client.command()
async def hi(ctx):
    await ctx.send("hi How is it going?")

@client.command()
async def good(ctx):
	await ctx.send("well.\nhow old are you?")

@client.command()
async def bad(ctx):
	await ctx.send("I see.I have something for you...:)\npls enter here\nhttps://www.youtube.com/watch?v=uHKfrz65KSU")

@client.command()	
async def Iam(ctx):
	await ctx.send("the best age...") 







client.run("NzcxMDgzODYxMjc4ODUxMTEy.X5m9zg.uYOeulP137lzM-yPnvMgQ-bkYcw")
