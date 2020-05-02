import discord
import random


welcome_channel_id = 700694359091183646
welcome_message = "Hallo auf diesem Discord Server. Bitte reagiere mit :school_satchel: um Pokémontrainer zu werden und mit :desktop: um Zugang zu den Tech-Kanälen zu bekommen. Wenn du die Reaktion entfernst verlierst du die Rolle."

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep Bop. Ich diene Spandau. Bop Beep.")
        already_sent = False
        welcome_channel = client.get_channel(welcome_channel_id)
        async for message in welcome_channel.history():
            if message.content == welcome_message:
                already_sent = True
            else:
                return

        if already_sent == False:
            await welcome_channel.send(welcome_message)

#        messages = welcome_channel.history(limit=200)
#        for i in messages:
#            if welcome_message in messages.content:
#                pass
#            else:
#                await welcome_channel.send(welcome_message)

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print(str(message.channel.id))

        if message.author == client.user:
            return #bei eigener nachricht nichts machen

        if message.content.startswith("Hello Big Brother"):
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

    async def on_reaction_add(self, reaction, user):
        #await reaction.message.channel.send(str(user) + " reacted on:\n\n" + str(reaction.message.content) + "\n\nwith:\n\n" + str(reaction.emoji))
        #await reaction.message.channel.send("Count: " + str(reaction.count))
        Techie = discord.utils.get(user.guild.roles, name="Techie")
        Pokemontrainer = discord.utils.get(user.guild.roles, name="Pokémontrainer")
        if str(reaction.message.content) ==  welcome_message:
#            print("the reaction belonged to my welcome_message")
#            print(reaction.emoji)
            if str(reaction.emoji) == "🖥️": # U+1F5A5 desktop computer
#                print("emoji was desktop computer ")
                await user.add_roles(Techie)
            if str(reaction.emoji) == "🎒":  # U+1F392 backpack
#                print("emoji was backpack ")
                await user.add_roles(Pokemontrainer)

    async def on_reaction_remove(self, reaction, user):
        Techie = discord.utils.get(user.guild.roles, name="Techie")
        Pokemontrainer = discord.utils.get(user.guild.roles, name="Pokémontrainer")
        if str(reaction.message.content) == welcome_message:
#            print("the reaction belonged to my welcome_message")
            if str(reaction.emoji) == "🖥️": # U+1F5A5 desktop computer
#                print("emoji was desktop computer ")
                await user.remove_roles(Techie)
            if str(reaction.emoji) == "🎒":  # U+1F392 backpack
#                print("emoji was backpack ")
                await user.remove_roles(Pokemontrainer)

    async def on_raw_reaction_add(selfself, payload):
#        print(str(payload))
#        channel = client.get_channel(payload.channel_id)
#        user = client.get_user(payload.user_id)
#        message = await channel.fetch_message(payload.message_id)
#        await channel.send(str(user) + " reacted on:\n\n" + str(message.content) + "\n\nwith:\n\n" + str(payload.emoji))
        pass

    async def on_member_remove(self, member):
        pass

    async def on_member_update(self, before, after):
#        print(str(before.joined_at))
#        print(str(before.activities))
#        print(str(before.guild))
#        print(str(before.nick))
#        print(str(before.mobile_status))
#        print(str(before.desktop_status))
#        print(str(before.web_status))
#        print(str(before.roles))
#        after.ban()
#        after.unban()
#        after.kick()
#        after.move_to(channel=channel-id)
#        before.avatar()
#        before.avatar_url()

#        roles = discord.utils.get(after.guild.roles, name="Hat die AGB noch nicht akzeptiert")
#        await after.addroles(roles)

#        roles = discord.utils.get(after.guild.roles, name="Typ")
#        await after.add_roles(roles)
        pass

    async def on_member_join(self, member):
        await member.send("Willkommen auf dem Server Spandauer Outlaws " + str(member).split('#')[0] + ". Bitte lies dir die Regeln durch.")
        await member.send('''########## Willkomen ##########

Willkommen auf Spandauer Outlaws! Dem nerdigen, Meme-haltigen, toleranten Server für alle Mac, Windows & Linux Nutzer von 077.
Hier kann gemeinsam gezockt, gelacht, geredet, diskutiert, debattiert und programmiert werden.

Folgende 5 Regeln sind zu beachten:
- Bitte postet NSFW-Memes oder ähnliches nur in die dafür vorgesehenen Channel.
- Bitte geht respektvoll miteinander um und seit tolerant. Toleranz bedeutet: Niemand wird wegen seinem Betriebsystem gehatet, seiner Sprache, politischer Orientierung oder seiner Meinung.
- Kein Spam/keine bösen Links.
- Bitte diskutiert sachlich und mach Sarkasmus und politische Meinung erkenntlich.

Jeder kann einladen, aber nur einladen, wer den Anforderungen des Servers entspricht! Bei Unsicherheiten oder Fragen bitte an @Mega Cooler Typ , @Ultra Cooler Typ oder @CEO wenden^^. Wir tolerieren nur tolerante Wesen!

Bei Verstößen, bitte an die Zuständigen melden im Channel #anzeige-ist-raus .

Ach und noch was, hier auf dem Server werden selbstgebaute Bots getestet. Bei Risiken oder Nebenwirkungen essen sie die Packungsbeilage und blamen sie 077.

Bei Änderungsvorschlägen am Server oder an Bots, schreibt sie ruhig alle in #server-vorschläge 

############################''')











client = MyClient()
client.run("<Your own token>")
