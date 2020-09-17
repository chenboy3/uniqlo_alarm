import json
import requests
import os
import time

# shirts
NEZUKO_URL = "https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-GetAvailability?pid=431957COL11SMA003000&Quantity=1"
ZENITSU_URL = "https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-GetAvailability?pid=431958COL46SMA003000&Quantity=1"

# sizes
SM = "SMA003000"
MD = "SMA004000"
LG = "SMA005000"

# PIDs
NEZUKO = "431957COL11"
ZENITSU = "431958COL46"

UNIQLO_URL_TEMPLATE = "https://www.uniqlo.com/on/demandware.store/Sites-UniqloUS-Site/default/Product-GetAvailability"
UNIQLO_PURCHASE_TEMPLATE = "https://www.uniqlo.com/us/en/manga-ut-demon-slayer-short-sleeve-graphic-t-shirt-"

HEADER = {"authority": "www.uniqlo.com",
          "accept": "application/json, text/javascript, */*; q=0.01",
          "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
          "referer": "https://www.uniqlo.com/us/en/manga-ut-demon-slayer-short-sleeve-graphic-t-shirt-431957.html",
          "x-requested-with": "XMLHttpRequest",
          "sec-fetch-site": "same-origin",
          "sec-fetch-mode": "cors",
          "sec-fetch-dest": "empty",
          "accept-language": "en-US,en;q=0.9",
         }

MIN = 60

ALARM = "kessen_spirit.mp3"


def query_endpoint_base(url):
    response = requests.get(url, headers = HEADER)
    # print(response.json())
    return json.dumps(response.text)

def query_endpoint(url, pid, size):
    response = requests.get(f"{UNIQLO_URL_TEMPLATE}?pid={pid}{size}&Quantity=1", headers = HEADER)
    # print(response.json())
    return response.json()

def uniqlo_status(uniqlo_json):
    if uniqlo_json["status"] == "IN_STOCK":
        ats = uniqlo_json["ats"]
        print(f"{ats} shirts are still in stock")
        return True
    else:
        return False

# os.system(f"afplay {ALARM}")
print(f"Running crawler every {MIN} seconds")
SHIRTS = [(NEZUKO, SM), (NEZUKO, MD), (ZENITSU, SM)]
while True:
    for shirt, size in SHIRTS:
        if(uniqlo_status(query_endpoint(UNIQLO_URL_TEMPLATE, shirt, size))):
            # call alarm
            print(f"{shirt} at {size} in stock!")
            print(f"Purchase Link: {UNIQLO_PURCHASE_TEMPLATE}{shirt[:6]}.html")
            os.system(f"afplay {ALARM}")
    time.sleep(MIN)
