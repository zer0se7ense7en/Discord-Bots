import discord

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep Bop. Ich diene Spandau. Bop Beep.")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        print("Nachricht von " + str(message.author) + " enthält " + str(message.content))

client = MyClient()
client.run("[Use your own token here]")


# Sample Output:
# Ich habe mich eingeloggt. Beep Bop. Ich diene Spandau. Bop Beep.
# Nachricht von zer0se7ense7en#4074 enthält test
# Nachricht von zer0se7ense7en#4074 enthält test123
