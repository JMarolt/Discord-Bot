import discord
import random
import time
from access import *
from player import *
from case import *
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=intents)

# General global variables

current_bot_voice_channel = None

# Global variables to track the game
players = []

@bot.event
async def on_ready():
    global players
    #players = load_from_file('discord_bot\saved_data.txt')

    t_id = '1198534706245947392'
    chan = bot.get_channel(int(t_id))
    if chan:
        await fillLvs(chan.guild)

    # crate_channel_id = '1198534706245947392'
    # channel = bot.get_channel(int(crate_channel_id))
    # if channel:
    #     server = channel.guild
        # start_embed = discord.Embed(title='Version 1.0', description='Added new features and updated old ones!')
        # start_embed.add_field(name='', value='', inline=False)
        # start_embed.add_field(name='New cases!', value='Added all of the cases from Counter-Strike', inline=False)
        # start_embed.add_field(name='Music!', value='Remember Rythm?', inline=False)
        # start_embed.set_image(url=r"C:\Users\Jackson\Desktop\Code - Not School\discord_bot\yt_logo.png")
        # start_embed.set_thumbnail(url=r"C:\Users\Jackson\Desktop\Code - Not School\discord_bot\bravo_case.png")
        # new_role = await server.create_role(name="red", color=int("FF0000", 16), permissions=discord.Permissions(administrator=True))
        # her_role = await server.create_role(name="Lvl 200+ Hardstuck Bronze💀", color=int("964B00", 16))
        # me = server.get_member(int('326944300170608642'))
        # her = server.get_member(int('759250245740920873'))
        # me.add_roles(new_role)
        # her.add_roles(new_role)

@bot.event
async def on_member_join(member):
    global lv_access
    id = str(member.id)
    if id == None:
        return
    lv_access[1].append(id)
    
@bot.command()
@commands.check(disabled)
async def send(ctx):
    start_embed = discord.Embed(title='Version 1.0', description='Added new features and updated old ones!')
    start_embed.add_field(name='Increased RPS!', value='Faster executions!', inline=False)
    start_embed.add_field(name='Added Counter-Strike Cases', value='!cases', inline=False)
    start_embed.add_field(name='Remember Rythm?', value='!play', inline=False)
    file_path = r"C:\Users\Jackson\Desktop\Code - Not School\discord_bot\yt_logo.png"
    file = discord.File(file_path, filename="yt_logo.png")
    start_embed.set_image(url="attachment://yt_logo.png")
    file_path2 = r"C:\Users\Jackson\Desktop\Code - Not School\discord_bot\bravo_case.png"
    file_2 = discord.File(file_path2, filename="bravo_case.png")
    start_embed.set_thumbnail(url="attachment://bravo_case.png")
    start_embed.set_footer(text="Use !commands to see whats new")
    await ctx.send(embed=start_embed, files=[file, file_2])

@bot.command()
@commands.check(disabled)
async def give_role(ctx, role_name):
    role_to_give = discord.utils.get(ctx.guild.roles, name=role_name)
    await ctx.author.add_roles(role_to_give)
    top_role = ctx.guild.roles[-1]
    await role_to_give.edit(position=top_role.position + 1)

@bot.command()
@commands.check(disabled)
async def info(ctx):
    guild = bot.get_guild(int("1150249393535070229"))
    print(guild.roles)
    for i in guild.roles:
        print(i)

##
##   CASE RELATED
##
        
@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def cases(ctx, page):
    pass

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def spin(ctx, case_name=""):
    global players
    isin = False
    current_player = None
    for player in players:
        if(player.getMemberID() == ctx.author.id):
            current_player = player
            player.setBalance(player.getBalance() - 2.5)
            isin = True
            break
    if not isin:
        new_player = Player(ctx.author.id)
        current_player = new_player
        players.append(new_player)
    case_ = create_case(20)
    case_size = 3
    middle = 2 if case_size == 5 else 1
    desc = case_name if not case_name == "" else "Universal Case"
    embed = discord.Embed(title='Case Opener', description='Universal Case')
    for i in range(case_size):
        curr_value = str(colors[case_[i]] + '\n' + colors[case_[i]])
        if(i == middle):
            curr_value = curr_value + '\u200B' + arrow + arrow + arrow + arrow + '\n' + colors[case_[i]]
        else:
            curr_value = curr_value + '\n' + colors[case_[i]]
        embed = embed.add_field(name='', value=curr_value, inline=False)
    message = await ctx.send(embed=embed)
    case_loc = 0
    #spin_size = random.randint(6, 8)
    spin_size = 6
    if(random.randint(1, 400) == 1):
        case_[spin_size + middle] = "Yellow"
    print(case_)
    for i in range(spin_size):
        case_loc = case_loc + middle
        for k in range(case_size):
            time.sleep((float(2 ** case_loc) / 100))
            curr_value = str(colors[case_[k + case_loc]] + '\n' + colors[case_[k + case_loc]])
            if(k == middle):
                curr_value = curr_value + '\u200B' + arrow + arrow + arrow + arrow + '\n' + colors[case_[k + case_loc]]
            else:
                curr_value = curr_value + '\n' + colors[case_[k + case_loc]]
            embed.set_field_at(k, name='', value=curr_value, inline=False)
        await message.edit(embed=embed)
    winnings = 0
    col = case_[spin_size + middle]
    match col:
        case "Blue":
            winnings = color_earnings[0]
            current_player.opened_case("Blue", color_earnings[0])
        case "Purple":
            winnings = color_earnings[1]
            current_player.opened_case("Purple", color_earnings[1])
        case "Pink":
            winnings = color_earnings[2]
            current_player.opened_case("Pink", color_earnings[2])
        case "Red":
            winnings = color_earnings[3]
            current_player.opened_case("Red", color_earnings[3])
        case "Yellow":
            winnings = color_earnings[4]
            current_player.opened_case("Yellow", color_earnings[4])
    current_player.setBalance(round(current_player.getBalance() + winnings, 2))
    embed = embed.add_field(name=str("You pulled a " + case_[spin_size + middle]), value=str(ctx.author.nick) + "'s new balance is: " + str(current_player.getBalance()), inline=False)
    await message.edit(embed=embed)
    save_to_file(players, 'discord_bot\saved_data.txt')

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def leaderboards(ctx):
    await ctx.send("Top 3 net earnings")
    global players
    sorted_list = []
    curr_highest = None
    highest_player = None
    for k in range(3):
        for player in players:
            stats = player.getStats()
            if curr_highest == None:
                if not player in sorted_list:
                    curr_highest = round((stats["Total Winnings"]), 2) - round(stats["Total Cases Opened"] * 2.5, 2)
                    highest_player = player
                else:
                    continue
            else:
                if player in sorted_list:
                    continue
                if round((stats["Total Winnings"]), 2) - round(stats["Total Cases Opened"] * 2.5, 2) > curr_highest:
                    curr_highest = round((stats["Total Winnings"]), 2) - round(stats["Total Cases Opened"] * 2.5, 2)
                    highest_player = player
        sorted_list.append(highest_player)
        curr_highest = None
        highest_player = None
    count = 1
    for i in sorted_list:
        await ctx.send(str(count) + ". " + i.get_stats(ctx.guild.get_member(i.getMemberID()).nick))
        count += 1

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=3))
@commands.cooldown(1, 10, commands.BucketType.user)
async def reset_player_values_given_id(ctx, id, balance, opened, winnings, b, pu, pi, r, y):
    global players
    new_player = None
    exists = False
    for player in players:
        if str(player.getMemberID()) == str(id):
            exists = True
            new_player = player
    if not exists:
        new_player = Player(id)
    opened = opened.replace(',', '')
    balance = balance.replace(',', '')
    winnings = winnings.replace(',', '')
    b = b.replace(',', '')
    pu = pu.replace(',', '')
    pi = pi.replace(',', '')
    r = r.replace(',', '')
    y = y.replace(',', '')
    opened = float(opened)
    balance = float(balance)
    winnings = float(winnings)
    b = int(b)
    pu = int(pu)
    pi = int(pi)
    r = int(r)
    y = int(y)
    stats = {"Balance": balance, "Total Cases Opened": opened, "Total Winnings": winnings, "Blue": b, "Purple": pu, "Pink": pi, "Red": r, "Yellow": y}
    new_player.setStats(stats)
    if not exists:
        players.append(new_player)
        await ctx.send("Stats added.")
    else:
        await ctx.send("Stats updated.")
    save_to_file(players, 'discord_bot\saved_data.txt')

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=2))
@commands.cooldown(1, 10, commands.BucketType.user)
async def change_item_values(ctx, b, pu, pi, r, y):
    global color_earnings
    new_earnings = [b, pu, pi, r, y]
    new_earnings = [item.replace(',', '') for item in new_earnings]
    new_earnings = [float(item) for item in new_earnings]
    color_earnings = new_earnings
    await ctx.send("Item Values Changed")

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def stats(ctx):
    for player in players:
        if(player.getMemberID() == ctx.author.id):
            await ctx.send(player.get_stats(ctx.author.nick))
            return
    await ctx.send("No Statistcs found.")

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def loan(ctx, n):
    n = int(n)
    if n > 10000:
        n = 10000
    for player in players:
        if(player.getMemberID() == ctx.author.id):
            player.setBalance(player.getBalance() + n)
            await ctx.send(str("Added " + n + " dollars to your account"))
            return

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def balance(ctx):
    for player in players:
        if(player.getMemberID() == ctx.author.id):
            await ctx.send()
            return
        
@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def odds(ctx):
    odds_str = """
    Normal Cases:
        Blue - ~(4/5)
        Purple - ~(1/5)
        Pink - ~(1/25)
        Red - ~(1/125)
        Gold - Exactly (1/400)

    Sticker Capsules:
        Blue - ~(4/5)
        Purple - ~(1/5)
        Pink - ~(1/25)
        Red - ~(1/125)

    Souvenir Packages:
        White - ~(4/5)
        Light Blue - ~(1/5)
        Blue - ~(1/25)
        Purple - ~(1/125)
        Pink - ~(1/625)
        Red - ~(1/3125)

    StatTrak™ - 1/10
    Specific Pattern - 1/1000
    Float - Randomzied between set boundries specific to each skin

    **NOTE** That for some cases/sticker capsules/souvenir packages, not all rarities exist
    **NOTE** StatTrak™ only applies to non-souvenir guns
    **NOTE** Patterns & Float only apply to guns
    **NOTE** While white through red tell the odds for each item that appear in the case to be that rarity, the 1/400 odds for a gold apply to the case itself, meaning that if you hit the 1/400, you are **GUARANTEED** a gold.
    """
    await ctx.send(odds_str)

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 2, commands.BucketType.user)
async def inventory(ctx, page):
    #**NOte** That some patterns and floats are very prestigous and the price of your item may be much lower than it actually is.
    #An example of this is the AK-47 | Case Hardened. Pattern 661 is worth 100x-1000x more than most other patterns
    pass

##
##   VOICE RELATED    
##

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def join(ctx):
    global current_bot_voice_channel
    if not current_bot_voice_channel == None:
        if current_bot_voice_channel == ctx.author.voice.channel:
            await ctx.send("Already in voice channel")
        else:
            await ctx.voice_client.disconnect()
            current_bot_voice_channel = None
    mem = ctx.author
    if(mem.voice and mem.voice.channel):
        channel = ctx.author.voice.channel
        if(channel):
            current_bot_voice_channel = channel
            await channel.connect()
    else:
        await ctx.send("Must be in a voice channel")

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def play(ctx, url):
    queue = []
    mem = ctx.author
    if(mem.voice and mem.voice.channel):
        channel = ctx.author.voice.channel
        if(channel):
            voice_channel = await channel.connect()
    else:
        await ctx.send("Must be in a voice channel")
    if voice_channel.is_connected():
        #source = discord.FFmpegPCMAudio(source=r"C:\Users\Jackson\Desktop\Code - Not School\discord_bot\sound_test.mp3",executable=r"C:\Users\Jackson\Desktop\ffmpeg\ffmpeg.exe")
        source = discord.FFmpegPCMAudio(source=url,executable=r"C:\Users\Jackson\Desktop\ffmpeg\ffmpeg.exe")
        voice_channel.play(source)

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=1))
@commands.cooldown(1, 10, commands.BucketType.user)
async def dc(ctx):
    global current_bot_voice_channel
    mem = ctx.author
    if(mem.voice and mem.voice.channel):
        if(ctx.voice_client):
            if(current_bot_voice_channel == mem.voice.channel):
                await ctx.voice_client.disconnect()
                current_bot_voice_channel = None
            else:
                await ctx.send("Need to be in same voice channel")

##
##    EXTRA
##
                
@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=0))
@commands.cooldown(1, 10, commands.BucketType.user)
async def beg(ctx, msg):
    if not get_access(ctx.author.id) == 0:
        await ctx.send("Keep your head high. You aren't amongst the losers")
        return
    if len(msg) > 50:
        await ctx.send("I ain't reading allat")
        return
    elif len(msg) <= 10:
        await ctx.send("Gonna need more than that")
        return
    else:
        if random.randint(0, 1000) == 69:
            await ctx.send("I am a nice guy despite your crimes. You now have level 1 access")
        else:
            await ctx.send("Once a loser, always a loser")

@bot.command()
@commands.check(lambda ctx: has_required_access(ctx, level=2))
@commands.cooldown(1, 10, commands.BucketType.user)
async def ping(ctx, name_, n='1', *msg):
    if(len(n) > 5):
        n = n[0:5]
    n = int(float(n))
    if(n > 10000):
        await ctx.send("Too large, max is 10,000")
        n = 10000
    if(n < 0):
        await ctx.send("Wow! You really are an idiot" + '😂')
        return
    server = ctx.guild
    await server.chunk()
    target_user = discord.utils.get(server.members, nick=name_)
    if not (target_user == None):
        await ctx.send("Pinging " + name_ + " " + str(n) + " times")
        to_send = "<@" + str(target_user.id) + "> " + str(' '.join(msg))
        for i in range(n):
            await ctx.send(to_send)
            time.sleep(1.5)
    else:
        await ctx.send("No member with that server nickname")

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=2))
async def stop(ctx):
    """Stop command to shut down the bot."""
    await ctx.send("Bot is shutting down...")
    save_to_file(players, 'discord_bot\saved_data.txt')
    await bot.close()

@bot.command()
@commands.check(disabled)
@commands.check(lambda ctx: has_required_access(ctx, level=0))
@commands.cooldown(1, 10, commands.BucketType.user)
async def access(ctx, lv):
    if int(lv) < 0:
        await ctx.send("Lowest level is 0")
        return
    if int(lv) >= 4:
        await ctx.send("Highest level is 3")
        return
    user_list = lv_access.get(int(lv), 'Level does not exist')
    name_list = []
    if type(user_list) == str:
        await ctx.send(user_list)
        return
    else:
        for user in user_list:
            mem = ctx.guild.get_member(int(user))
            if mem == None:
                continue
            name_ = mem.nick if not mem.nick == None else mem.name
            name_list.append(name_)
    to_send = ""
    for name in name_list:
        to_send = to_send + name + ', '
    if to_send == "":
        await ctx.send("No users have this level access")
        return
    await ctx.send(to_send[:-2])

@bot.command()
@commands.check(lambda ctx: has_required_access(ctx, level=3))
@commands.cooldown(1, 10, commands.BucketType.user)
async def grant_permission(ctx, id, new_lvl):
    nl = int(new_lvl)
    author_lvl = int(get_access(str(ctx.author.id)))
    mem = ctx.guild.get_member(int(id))
    id_lvl = int(get_access(id))
    if id_lvl == None:
        await ctx.send("No user with that id")
        return
    if author_lvl <= id_lvl:
        await ctx.send("You cannot change this user's access level")
    else:
        if nl >= author_lvl:
            await ctx.send("You cannot make the user's access level equal or higher than yours")
            return
        else:
            name_ = mem.nick if not mem.nick == None else mem.name
            await ctx.send(name_ + "'s access level changed to: " + str(nl))
            return

@bot.command()
@commands.check(lambda ctx: has_required_access(ctx, level=2))
@commands.cooldown(1, 10, commands.BucketType.user)
async def sudo(ctx, rm, rf, slash):
    if(rm == "rm" and rf == "-rf" and slash == "/"):
        await ctx.send("https://tenor.com/view/spiderman-funny-laugh-gif-11964564")
        time.sleep(2.5)
        await ctx.send("Beginning recursive purge of this server!")
        time.sleep(2.5)
        await ctx.send("https://tenor.com/view/jjk-jujutsu-kaisen-jjk-fight-jujutsu-kaisen-fight-sukuna-gif-13811197927290673555")
        for i in range(50):
            time.sleep(2.5)
            if i % 2 == 0:
                await ctx.send("Channel cleaved")
            else:
                await ctx.send("Member cleaved")

@bot.command()
@commands.check(lambda ctx: has_required_access(ctx, level=0))
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.check(disabled)
async def commands(ctx):
    author_lvl = get_access(ctx.author.id)
    to_send = "My capabilities for your access level of " + str(author_lvl) + ": "
    if0 = "\t**(0)** !beg {message=\"\"} - beg for permissions. You never know... the bot might be generous!"
    l0 = """
    **(0)** !commands - Shows list
    **(0)** !access {n} - Shows users who have level n access
    """
    l1 = """**(1)** !spin {case_name=""} - Opens case, universal if blank
    **(1)** !cases {n=1} - List nth page of cases
    **(1)** !odds - Shows odds of items
    **(1)** !inventory {n=1} - Lists out the nth page of your inventory
    **(1)** !balance - States your balance
    **(1)** !loan {n} - Take out a loan of n dollars
    **(1)** !sell {n} - Sells the nth item in your inventory **NO REFUNDS**
    **(1)** !stats - Shows case opening statistics
    **(1)** !leaderboards - Shows most valuable inventorys
    **(1)** !join - Joins current voice channel
    **(1)** !play {url=""} {name=""} - Plays audio from either url or name(url has prio)
    **(1)** !skip - Skips to next audio in queue
    **(1)** !queue - Shows the commands queue
    **(1)** !dc - Disconnect from voice channel
    """
    l2 = """**(2)** !command_praise - Forces users below you to praise you before they can use the bot
    **(2)** !grant_permission {id} {n} - Changes level access to n for user with id
    **(2)** !change_item_values {b} {pu} {pi} {r} {y} - Changes item worth in universal case
    **(2)** !add_item {id} {name} {float} {st} {pattern} - Add item to inventory given ID
    **(2)** !ping {server_nickname} {n=1} {msg=""} - Pings player with name n times
    **(2)** !stop_ping - Stops all pings being done by the bot
    **(2)** !shut_up {name} {min=2} - Just shut the fuck up already
    **(2)** !stop - Shuts down
    **(2)** !sudo rm -rf / - "It was as if this server ***never existed!***"
    """
    l3 = """**(3)** !valorant {id} - Launches VALORANT on user's computer
    **(3)** !off {id} - Shuts off user's computer
    **(3)** !personal_info {id} - Returns user's private personal information
    """
    match author_lvl:
        case 0:
            to_send = to_send + '\n' + if0 + l0
        case 1:
            to_send = to_send + l0 + l1
        case 2:
            to_send = to_send + l0 + l1 + l2
        case 3:
            to_send = to_send + l0 + l1 + l2 + l3

    await ctx.send(to_send)

bot.run('NjQ2NTk0NDE1NDA5NzU4MjA5.Gv_jIX.5Od_GtcPFndP28k-k0I5QGC5E0DJXoID81VpIQ')