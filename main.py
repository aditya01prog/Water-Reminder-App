import time 
from plyer import notification

while True:
    print("Hey! It's time to drink some water")
    notification.notify(title = "Hey! Did you drink some water", 
                        message = "You need to drink some water") 
    time.sleep(60*60)