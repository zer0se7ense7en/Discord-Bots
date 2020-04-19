import discord

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep Bop. Ich diene Spandau. Bop Beep.")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return #bei eigener nachricht nichts machen

        if message.content.startswith("Hello Big Brother"):
            await message.channel.send("Hello " + str(message.author) + ". I'm watching you.")

    async def on_member_join(self, member):
        await member.send("Willkommen auf dem Server Spandauer Outlaws " + str(member) + ". Bitte lies dir die Regeln durch.")
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
client.run("<Insert your own token here>")
