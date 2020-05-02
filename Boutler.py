import discord
import random

debug_channel_id = 706200778205036544
rollen_channel_id = 706170659667181598
rollen_message = """Hallo auf diesem Discord Server. Diese Nachricht ist dazu da, um Rollen zu verteilen, 
mit denen du Zutritt zu den entsprechenden Channels hast. 
Außerdem können andere oLaFs sich so an die entsprechnenden Fachleute wenden mit @rolle.

Bitte reagiere auf diese Nachricht mit :snake: um Python-Coder zu werden,
mit :copyright: um C++-Coder zu werden, mit :a: um Arduino-Fachmann zu werden, 
mit :m: um Mindstormer zu werden und mit :cat: um Scratch-Fachmann zu werden.

Wenn du die Reaktion entfernst verlierst du die Rolle.
Es kann sein, dass aus Wartungsgründen diese Nachricht ersetzt wird und deine Reaktionen verschwinden und 
du erneut darauf reagieren musst um beides zu "synchronieren", deine Rollen verlierst du dabei nicht!"""

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep Bop. Ich diene dem oLaF. Bop Beep.")
        debug_channel = client.get_channel(debug_channel_id)
        await debug_channel.send("Ich habe mich eingeloggt. Beep Bop. Ich diene dem oLaF. Bop Beep.")

        rollen_channel = client.get_channel(rollen_channel_id)
        rollen_message_dc = await rollen_channel.send(rollen_message)

        print(str(rollen_message_dc))

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print(str(message.channel.id))

        if message.author == client.user:
            return #bei eigener nachricht nichts machen

        if message.content.startswith("Hello Boutler"):
            await message.channel.send("Hello " + str(message.author).split('#')[0] + ". I'm watching you.")
            await message.author.send("Hello " + str(message.author).split('#')[0] + ". I'm watching you.")

        # leaderboard neu berechnen mit history
        if str(message.content) == "$create_leaderboard" and str(message.author) == "zer0se7ense7en#4074":
            messages = await message.channel.history(limit=100).flatten()
            for i in messages:
                print(i.content)

        if message.content.startswith("pls porn"):
            ergebnis = random.randrange(0,2)
            print(ergebnis)
            ergebnis = 0
            if ergebnis is 1:
                await message.delete() # delete gif?!?!?!
                await message.channel.send(
                    "Diese Nachricht wurde gelöscht durch Big Brother!" + "Anzeige ist raus!\nSchäm dich " +
                    str(message.author).split('#')[0] + " !")
                await message.author.send(
                    "Du hast etwas böses getan! Da ich ein Bot bin, habe ich keine Ahnung was du getan hast, aber es war wahrscheinlich nicht gut!\nJetzt stecke 50ct in die Schäm-Dich-Box\n\n\tBig Brother over and out,\n\tIch diene Spandau!")

            else:  #randomizin?!?!
                await message.add_reaction('🤨')  #U+1F928
                await message.add_reaction('🔞')  #U+1F51E
                await message.add_reaction('🍑')  #U+1F351
        """
    async def on_reaction_add(self, reaction, user, rollen_message_dc):
        Arduino_role = discord.utils.get(user.guild.roles, name="Arduino")
        Cplusplus_role = discord.utils.get(user.guild.roles, name="C++")
        Python_role = discord.utils.get(user.guild.roles, name="Python")
        Mindstorm_role = discord.utils.get(user.guild.roles, name="Mindstormer")
        Scratch_role = discord.utils.get(user.guild.roles, name="Scratch")

        if reaction.message.id == rollen_message_dc.id:
            print("the reaction belonged to my rollen_message")
            print(reaction.emoji)
            if str(reaction.emoji) == ":a:":
                print("emoji was desktop a ")
                await user.add_roles(Arduino_role)
            if str(reaction.emoji) == "©️":
                print("emoji was copyright ")
                await user.add_roles(Cplusplus_role)
            if str(reaction.emoji) == ":snake:":
                print("emoji was snake ")
                await user.add_roles(Python_role)
            if str(reaction.emoji) == ":m:":
                print("emoji was m ")
                await user.add_roles(Mindstorm_role)
            if str(reaction.emoji) == ":cat:":
                print("emoji was cat ")
                await user.add_roles(Scratch_role)

    async def on_reaction_remove(self, reaction, user, rollen_message_dc):
        Arduino_role = discord.utils.get(user.guild.roles, name="Arduino")
        Cplusplus_role = discord.utils.get(user.guild.roles, name="C++")
        Python_role = discord.utils.get(user.guild.roles, name="Python")
        Mindstorm_role = discord.utils.get(user.guild.roles, name="Mindstormer")
        Scratch_role = discord.utils.get(user.guild.roles, name="Scratch")


        if reaction.message.id == rollen_message_dc.id:
            print("the reaction belonged to my rollen_message")
            print(reaction.emoji)
            if str(reaction.emoji) == ":a:":
                print("emoji was desktop a ")
            await user.add_roles(Arduino_role)
            if str(reaction.emoji) == "©️":
                print("emoji was copyright ")
                await user.add_roles(Cplusplus_role)
            if str(reaction.emoji) == ":snake:":
                print("emoji was snake ")
                await user.add_roles(Python_role)
            if str(reaction.emoji) == ":m:":
                print("emoji was m ")
                await user.add_roles(Mindstorm_role)
            if str(reaction.emoji) == ":cat:":
                print("emoji was cat ")
                await user.add_roles(Scratch_role)
        """
    async def on_raw_reaction_add(selfself, payload):

#        print(str(payload))
#        channel = client.get_channel(payload.channel_id)
#        user = client.get_user(payload.user_id)
#        message = await channel.fetch_message(payload.message_id)
#        await channel.send(str(user) + " reacted on:\n\n" + str(message.content) + "\n\nwith:\n\n" + str(payload.emoji))
        pass

    async def on_member_join(self, member):
        await member.send("Willkommen auf dem Server des oLaF " + str(member).split('#')[0] + ". Bitte lies dir die Regeln durch.")
        await member.send('''########## Willkomen ##########

Willkommen auf dem offiziellen Server des oLaF! Dem nerdigen, Meme-haltigen, toleranten Server für alle Mac, Windows & Linux Nutzer.
Hier kann gemeinsam gezockt, gelacht, geredet, diskutiert, debattiert und programmiert werden.

Folgende 5 Regeln sind zu beachten:
- Bitte postet NSFW-Memes oder ähnliches nur in die dafür vorgesehenen Channel.
- Bitte geht respektvoll miteinander um und seid tolerant.
- Kein Spam/keine bösen Links.
- Bitte diskutiert sachlich und macht Sarkasmus und politische Meinung erkenntlich.

Ach und noch was, hier auf dem Server werden selbstgebaute Bots getestet. Bei Risiken oder Nebenwirkungen essen sie die Packungsbeilage und blamen sie 077.

Bei Änderungsvorschlägen am Server oder an Bots, schreibt sie ruhig alle in #vorschläge-server 

############################''')



client = MyClient()
client.run("your token here")
