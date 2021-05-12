import discord
import python_weather
import asyncio

client = discord.Client()
wc = python_weather.Client(format=python_weather.METRIC)

string = 'Leeds'

PREFIX = "."

@client.event
async def on_ready():
    print("Bot started up.")


@client.event
async def on_message(message):
    
    c = message.content

    if c.startswith(PREFIX):

        c = c.replace(PREFIX,'')

        if c.startswith("weather"):

            c = c.replace('weather','')

            try:
                weather = await wc.find(c)
            except:
                await message.channel.send('Could not find location! :(')
                return

            index = 0
            text = ""

            for forcast in weather.forecast:

                index += 1
                
                

                number_table = {
                    1:':one:',
                    2:':two:',
                    3:':three:',
                    4:':four:',
                    5:':five:'
                }

                emote_table = {
                    "cloudy":":cloud:",
                    "rain":":cloud_rain:",
                    "light rain":":cloud_rain:",
                    "partly sunny":":white_sun_small_cloud:",
                    "rain showers":":cloud_rain:",
                    "mostly cloudy":":white_sun_cloud:",
                    "partly cloudy":":white_sun_small_cloud:",
                    "mostly sunny":":white_sun_small_cloud:",
                    "sunny":":sunny:",
                    "clear":":sunny:"
                }

                # format



                text = text + number_table[index] + " " + forcast.day + " " + emote_table[forcast.sky_text.lower()] + " " + forcast.sky_text + " - " + "Average: ***{}*** - ".format(str(forcast.temperature)) + "Low: ***{}*** - ".format(str(forcast.low)) + "High: ***{}***".format(str(forcast.high)) + "\n\n" 

            await message.channel.send(embed=discord.Embed(title='Weather in {}'.format(c.strip().title()),description=text))


client.run('ODQyMDIyMzMzMzUwMjgxMjM2.YJvQaA.FcUhOo71_uv6a4QkKe7Fh4KFggc')