import discord

lv_access = {0: ["759250245740920873"], 1: [], 2:["317801961137242114"], 3:["326944300170608642"]}

async def fillLvs(guild):
    global lv_access
    members = guild.members
    ls = list(lv_access.values())
    skip = False
    for member in members:
        skip = False
        id = str(member.id)
        for item in ls:
            lis = list(item)
            if id in lis:
                skip = True
                break
        if skip:
            continue
        lv_access[1].append(id)

def get_access(id):
    global lv_access
    id = str(id)
    for key, val in lv_access.items():
        if id in val:
            return key
    return None

async def has_required_access(ctx, level):
    global lv_access
    user_id = str(ctx.author.id)
    ls = list(lv_access.values())
    ls = ls[level:]
    for lvl in ls:
        lv = list(lvl)
        if user_id in lv:
            return True
    await ctx.send("Access denied.")
    return False 

async def disabled(ctx):
    await ctx.send("This command is disabled")
    return False