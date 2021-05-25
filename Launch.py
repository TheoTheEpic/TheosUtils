import os
import time
import requests
import ctypes  

os.system("title Theo's Utils")

os.system("color 0c")

chosen = int(input("Select an option:\n\n[1]: Asset Logger\n[2]: Model botter\n[3]: Webhook Spammer\n[4]: Version Check\n[5]: Model Sales Botter\n[6]: Discord RPC\n\n"))
versioncheck = requests.get("https://pastebin.com/raw/wfXwmmks").text
currentversion = "V2.1"

os.system("cls")

if chosen == 1:
    print("Running Asset Logger, please wait.")
    os.system("title Asset Logger")
    os.system("node Files/ConsoleAssetLog.js")
if chosen == 2:
    print("Running Model Botter, please wait.")
    os.system("title Model Botter")
    os.system("node Files/ModelBotter.js")
if chosen == 3:
    print("Running Webhook Spammer, please wait.")
    os.system("title Webhook Spammer")
    os.system("py Files/WebhookSpammer.py")
if chosen == 4:
    print("Running Version Check, please wait.")
    os.system("title Version Check")
    if versioncheck == currentversion:
        os.system("cls")
        ctypes.windll.user32.MessageBoxW(0, "You are running the latest version.", "Theos Utils", 1)
    else:
        os.system("cls")
        ctypes.windll.user32.MessageBoxW(0, "You are NOT running the latest version, please update.", "Theos Utils", 1)
if chosen == 5:
    print("Running Model Sales Botter, please wait.")
    os.system("title Model Sales Botter")
    os.system("node Files/ModelSaleBotter.js")
if chosen == 6:
    print("Running DiscordRPC, please wait.")
    os.system("title DiscordRPC")
    os.system("node Files/DiscordRPC.js")
