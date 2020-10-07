import requests, json, sys, logging, threading
from os import system, name 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
from colorama import init, Fore

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()



def clear():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 



def request_thread(code, headers):
    response = requests.get(code, headers=headers, verify=False)
    if "ok" in response.text:
        logging.info("Puntata presa [+{}]".format(response.text.replace("ok-", "")))
    else:
        logging.info("Puntata non valida [{}]".format(response.text))
    return True


if __name__ == "__main__":
    clear()
    input("Per permettere il corretto funzionamento del programma RICORDA:\n\n1)Inserisci il codice sessione all'interno del file 'config.json'\n2)Inserisci i link all'interno del file links.txt. \n\n3)Per far partire il programma premi [ENTER]")
    format = "[%(asctime)s] -  %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,)
    try:
        clear()
        configse = json.loads(open("config.json", "r").read())
        logging.info("Config loaded.")
        links = open("links.txt", "r", encoding="utf8")
        logging.info("Links loaded.")
    except:
        logging.warn("An error occurred.")
        sys.exit()
    for i in links:
        if "https://" in i:
            link = "https" + i.split("https")[-1].split("\n")[0]
            code = "https://it.bidoo.com/push_promotions.php?code=" + link.split("&")[0].replace("https://it.bidoo.com/?promocode=", "")
            headers = {
                "Host": "it.bidoo.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
                "Accept": "*/*",
                "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
                "X-Requested-With": "XMLHttpRequest",
                "Connection": "keep-alive",
                "Referer": link,
                "Cookie": "dess=" + configse["session_id"] + ";"
            }
            x = threading.Thread(target=request_thread, args=(code, headers))
            x.start()