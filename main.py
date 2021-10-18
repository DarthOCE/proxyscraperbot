import requests
import discord
from discord import Embed, File
from discord.ext import commands

token = ""

client = commands.Bot(command_prefix='+')
client.remove_command('help')


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"+help"))
    
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements to execute this command")

@client.command()
async def help(ctx):
    embed = Embed(title="All Commands", description="A simple proxy scraper bot")
    embed.add_field(name="+help", value="Displays all available commands", inline=False)
    embed.add_field(name="+proxyhelp", value="Shows proxy commands", inline=False)
    embed.add_field(name="+adminhelp", value="Shows Admin Commands", inline=False)
    embed.add_field(name="+premiumhelp", value="UHQ Proxys for cloud members, updates daily", inline=False)
    embed.set_footer(text="Hosted by DarthOCE#8832")
    await ctx.send(embed=embed)

@client.command()
async def proxyhelp(ctx):
    embed = Embed(title="Proxy Commands", description="A simple proxy scraper bot")
    embed.add_field(name="+help", value="Displays all available commands", inline=False)
    embed.add_field(name="+http", value="Sends fresh http proxy list", inline=False)
    embed.add_field(name="+https", value="Sends fresh https proxy list", inline=False)
    embed.add_field(name="+socks4", value="Sends fresh socks4 proxy list", inline=False)
    embed.add_field(name="+socks5", value="Sends fresh socsk5 proxy list", inline=False)
    embed.add_field(name="+all", value="Sends fresh http, https, socks4 and socks5 proxy list", inline=False)
    embed.add_field(name="+premiumhelp", value="UHQ Proxys for cloud members, updates daily", inline=False)
    embed.set_footer(text="Hosted by DarthOCE#8832")
    await ctx.send(embed=embed)
    
@client.command()
async def adminhelp(ctx):
    embed = Embed(title="Admin Commands", description="A simple proxy scraper bot")
    embed.add_field(name="+ban", value="Bans a member", inline=False)
    embed.add_field(name="+unban", value="Unbans a member", inline=False)
    embed.add_field(name="+kick", value="Kicks a member", inline=False)
    embed.set_footer(text="Hosted by DarthOCE#8832")
    await ctx.send(embed=embed)


@client.command()
async def http(ctx):
    f = open("Data/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send(file=File("Data/http-proxies.txt"))
    await ctx.send("Proxys sent to you DM'S! if you did not recive them make sure your direct messages are turned on! For higher cpm use a proxy checker to check the proxys!")

@client.command()
async def https(ctx):
    f = open("Data/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send(file=File("Data/https-proxies.txt"))
    await ctx.send("Proxys sent to you DM'S! if you did not recive them make sure your direct messages are turned on! For higher cpm use a proxy checker to check the proxys!")

@client.command()
async def socks4(ctx):
    f = open("Data/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send(file=File("Data/socks4-proxies.txt"))
    await ctx.send("Proxys sent to you DM'S! if you did not recive them make sure your direct messages are turned on! For higher cpm use a proxy checker to check the proxys!")

@client.command()
async def socks5(ctx):
    f = open("Data/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send(file=File("Data/socks5-proxies.txt"))
    await ctx.send("Proxys sent to you DM'S! if you did not recive them make sure your direct messages are turned on! For higher cpm use a proxy checker to check the proxys!")

@client.command()
async def all(ctx):
    f = open("Data/all-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.author.send(file=File("Data/all-proxies.txt"))
    await ctx.send("Proxys sent to you DM'S! if you did not recive them make sure your direct messages are turned on! For higher cpm use a proxy checker to check the proxys!")
    
@client.command()
async def rep(ctx):
    await ctx.send('Thanks for the vouch!')
    
@client.command()
async def vouch(ctx):
    await ctx.send('Thanks for the vouch!')
    
@client.command()
async def premiumhelp(ctx):
    embed = Embed(title="Premium Commands", description="Commands for cloud memebers")
    embed.add_field(name="+cloudhttps", value="Sends UHQ HTTPS proxy list", inline=False)
    embed.add_field(name="+cloudsocks4", value="Sends UHQ SOCKS4 proxy list", inline=False)
    embed.add_field(name="+cloudsocks5", value="Sends UHQ SOCKS5 proxy list", inline=False)
    embed.add_field(name="+ipvanish", value="Sends UHQ Ipvanish proxy list", inline=False)
    embed.set_footer(text="Hosted by DarthOCE#8832")
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role('Spikes Elite', 'Spikes Basic')
async def ipvanish(ctx):
    await ctx.author.send(file=File("Data/ipvanish.txt"))
    await ctx.send("Proxys sent to you DM'S! For higher cpm use a proxy checker to check the proxys!")

@client.command()
@commands.has_any_role('Spikes Elite', 'Spikes Basic')
async def cloudhttps(ctx):
    await ctx.author.send(file=File("Data/cloudhttps.txt"))
    await ctx.send("Proxys sent to you DM'S! For higher cpm use a proxy checker to check the proxys!")

@client.command()
@commands.has_any_role('Spikes Elite', 'Spikes Basic')
async def cloudsocks4(ctx):
    await ctx.author.send(file=File("Data/cloudsocks4.txt"))
    await ctx.send("Proxys sent to you DM'S! For higher cpm use a proxy checker to check the proxys!")

@client.command()
@commands.has_any_role('Spikes Elite', 'Spikes Basic')
async def cloudsocks5(ctx):
    await ctx.author.send(file=File("Data/cloudsocks5.txt"))
    await ctx.send("Proxys sent to you DM'S! For higher cpm use a proxy checker to check the proxys!")
    
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed = Embed(title="Banned")
    embed.add_field(f"Banned {user.mention}")
    embed.set_footer(text=f"Banned by {user.author}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)
    
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = Embed(title="Unbanned")
            embed.add_field(f"Unbanned {user.mention}")
            embed.set_footer(text=f"Unbanned by {user.author}")
            return
        
        
snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None
        
        
@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")
       






          
client.run(token)
