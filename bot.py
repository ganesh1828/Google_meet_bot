from time import sleep
import pyautogui as auto
import schedule, webbrowser
#URL of your Google meet
link = "meet.google.com/pxk-vkcx-gqw"
#Time at which you want to join the meet
time = "22:51"


def join():
    webbrowser.open_new_tab('https://' + link)
    sleep(7)
    #To mute the audio
    auto.hotkey('ctrl', 'd')
    #To off the video
    auto.hotkey('ctrl', 'e')

    # auto.hotkey('command', 'd')
    # auto.hotkey('command', 'e')
    #Cordinates of your Ask to join button on the web bowser window
    auto.click(1328,606)


schedule.every().day.at(time).do(join)

while True:
    schedule.run_pending()
    sleep(1)




