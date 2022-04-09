import requests
import json
from notifypy import Notify
from time import sleep
from sys import exit

# sleep(10)


def json_to_dic(json_object):
    dic = json.loads(json.dumps(json_object))
    return dic


def todays_name_day():
    time = 10
    for attempt in range(1, 4):
        try:
            response = requests.get("https://svatky.adresa.info/json").json()[0]
            break
        except requests.exceptions.ConnectionError or requests.exceptions.InvalidURL:
            notification.title = f"Nelze se připojit k serveru ({attempt}/3)"
            notification.message = f"Zkusíme to znovu za {time} sekund"
            notification.send()

            sleep(time)
            time += 5

            if attempt != 3:
                continue
            else:
                notification.title = f"Nepodařilo se připojit k serveru"
                notification.message = f"Ukončování aplikace..."
                notification.send()
                exit()

    response = json_to_dic(response)
    name_day = response["name"]
    day = response["date"]

    notification.title = f"Dnes {day[:2].strip('0')}. {day[2:].strip('0')}"
    notification.message = f"má svátek {name_day}"
    notification.send()


notification = Notify(default_notification_application_name="Kdo má dnes svátek?", default_notification_icon="icon.ico")
todays_name_day()
