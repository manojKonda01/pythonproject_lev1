from datetime import datetime
from playsound import playsound
def alarmset(n):

    while True:
        if len(n) == 11:
            now=datetime.now()
            if n[9:].upper()== now.strftime("%p") and n[:2] == now.strftime("%I") and n[3:5] == now.strftime("%M") and n[6:8] == now.strftime("%S"):
                print('Wake Up dumb')
                playsound('wakeup-alarm-tone-21497.mp3')
                break
        else:
            print('Enter time as menioned format with 0s')

print(datetime.now().strftime('%I:%M:%S'))
n=input('Set time as HH:MM:SS:(am/pm) (ex 08:24:35:am) :')
alarmset(n)
