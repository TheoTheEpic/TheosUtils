import os
import time
import math
import random
import requests
from discord_webhook import DiscordWebhook

targetwebhook = input("\n\nWelcome to Webhook spammer!\n Webhook URL: ")
webhookusername = input("Custom webhook username (leave blank for default): ")
messagedelay = int(input("Amount of seconds between webhook messages (0 for fastest speed): "))
totalmessages = int(input("Total amount of messages: "))
spamtype = int(input("Webhook spamming type:\n\n[1]: Arabic Allah Propaganda\n[2]: Channel flood\n[3]: Trollage\n[4]: Custom (from Config/CustomMessage.txt)\n[5]: Mass ping\n\nSelect a number option: "))
os.system("cls")
print("\n\nWorking...")
time.sleep(2)
os.system("cls")

##########

spamarray = []
if spamtype==1:
    spamarray = ["﷽"]
if spamtype==2:
    spamarray = ["```i``` ```a```m``` ```t```o```t```a```l```l```y``` ```n```o```t``` ```t```r```y```i```n```g``` ```t```o``` ```f```l```o```o```d``` ```y```o```u```r``` ```s```e```r```v```e```r``` ```e```n```j```o```y``` ```t```h```i```s``` ```w```h```i```l```e``` ```t```r```y```i```n```g``` ```t```o``` ```b```l```o```c```k``` ```y```o```u```r``` ```w```e```b```h```o```o```k``` ```<```3```"]
if spamtype==3:
    spamarray = ["Trollage https://tenor.com/view/trollge-troll-the-day-of-reckoning-gif-19655212"]
if spamtype==4:
    customspam = open("Config/CustomMessage.txt","r")
    custommsg = customspam.read()
    spamarray = [custommsg]

if spamtype==5:
    spamarray = ["@everyone @here enjoy the pings lmfao"]

##########

bar=""
percent="0%"
start=0
end=totalmessages
def main():
    os.system("cls")
    global bar
    global percent
    global start
    global end
    bar = ""
    start = start + 1
    percent = math.floor(start/end*100)
    for i in range(math.floor(percent/5)):
        bar = bar + "▓"
    for i in range(20-len(bar)):
        bar = bar + "░"
    print(f"\nMessages sent: {start}/{end}")
    print(f"Progress of webhook being spammed: \n[{bar}] {str(percent)}%")

    if webhookusername=="":
        DiscordWebhook(url=[str(targetwebhook)], content=random.choice(spamarray)).execute()
    else:
        DiscordWebhook(url=[str(targetwebhook)],username=webhookusername, content=random.choice(spamarray)).execute()

########## 

for i in range(totalmessages):
    time.sleep(messagedelay)
    main()

input("Webhook spammer finished spamming the webhook, press Enter to exit.")
