import os
import requests
import time
from colorama import init
from colorama import Fore, Back

os.system("mode con cols=130 lines=30")

url = 'https://v6.mixerno.space/api/youtube-channel-counter/user/UCZf__ehlCEBPop-_sldpBUQ'

yt_data = requests.get(url).json()

init(autoreset=True)
print(Fore.GREEN + "██   ██ ██ ██   ██  █████  ██   ██ ██ ███    ██ ████████ ██    ██     ███████ ████████  █████  ████████ ██    ██ ███████ ")
print(Fore.GREEN + "██   ██ ██ ██  ██  ██   ██ ██  ██  ██ ████   ██    ██    ██    ██     ██         ██    ██   ██    ██    ██    ██ ██      ")
time.sleep(1)
print(Fore.GREEN + "███████ ██ █████   ███████ █████   ██ ██ ██  ██    ██    ██    ██     ███████    ██    ███████    ██    ██    ██ ███████ ")
time.sleep(1)
print(Fore.GREEN + "██   ██ ██ ██  ██  ██   ██ ██  ██  ██ ██  ██ ██    ██     ██  ██           ██    ██    ██   ██    ██    ██    ██      ██ ")
time.sleep(1)
print(Fore.GREEN + "██   ██ ██ ██   ██ ██   ██ ██   ██ ██ ██   ████    ██      ████       ███████    ██    ██   ██    ██     ██████  ███████ ")
time.sleep(1)

print("\n\n--------------------------------------------------------------------------------")
print("ヒカキンTVのチャンネルのステータスはこちらです。\n")

print("登録者数", yt_data["counts"][0]["count"], "人")
print("総再生回数", yt_data["counts"][3]["count"], "回")
print("動画数", yt_data["counts"][5]["count"], "個")


def main():
    new_data = requests.get(url).json()
    os.system('cls')
    init(autoreset=True)
    print(Fore.GREEN + "██   ██ ██ ██   ██  █████  ██   ██ ██ ███    ██ ████████ ██    ██     ███████ ████████  █████  ████████ ██    ██ ███████ ")
    print(Fore.GREEN + "██   ██ ██ ██  ██  ██   ██ ██  ██  ██ ████   ██    ██    ██    ██     ██         ██    ██   ██    ██    ██    ██ ██      ")
    print(Fore.GREEN + "███████ ██ █████   ███████ █████   ██ ██ ██  ██    ██    ██    ██     ███████    ██    ███████    ██    ██    ██ ███████ ")
    print(Fore.GREEN + "██   ██ ██ ██  ██  ██   ██ ██  ██  ██ ██  ██ ██    ██     ██  ██           ██    ██    ██   ██    ██    ██    ██      ██ ")
    print(Fore.GREEN + "██   ██ ██ ██   ██ ██   ██ ██   ██ ██ ██   ████    ██      ████       ███████    ██    ██   ██    ██     ██████  ███████ ")
    time.sleep(1)
    print("\n\n--------------------------------------------------------------------------------")
    print("ヒカキンTV最新のステータスはこちらです。\n")
    print("登録者数", new_data["counts"][0]["count"], "人")
    print("総再生回数", new_data["counts"][3]["count"], "回")
    print("動画数", new_data["counts"][5]["count"], "個")

while True:

    inpt = input('最新の情報に更新しますか？ (y/n)')
    if inpt == 'y':
        main()    
    elif inpt == 'n':
        break
    else:
        print("yかnで答えてください。")
