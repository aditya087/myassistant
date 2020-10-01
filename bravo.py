import pyttsx3
import os

pyttsx3.speak(
    "Hi, This is Bravo, Welcome to my tools")

while(1):

    print("Which application would you like to open: ", end=' ')

    p = input().lower()

    if(("open" in p) or ("start" in p)) and (("editor" in p) or ("notepad" in p)):

        pyttsx3.speak("Opening notepad")

        os.system("notepad")

    elif(("open" in p) or ("start" in p)) and ("chrome" in p):

        if 'incognito mode' not in p or 'private browser' not in p:

            p = input("Do you want incognito chrome/ private browser? ").lower()

            if ('incognito chrome' in p or 'private browser' in p or 'yes' in p):

                pyttsx3.speak("Opening Incognito chrome")

                os.system("start chrome -incognito")

            else:
                pyttsx3.speak("Opening Chrome")

                os.system("start chrome google.com")

    elif(("open" in p) or ("start" in p)) and (("song player" in p) or ("media player" in p)):

        pyttsx3.speak("Opening Windows Media Player")

        os.system("wmplayer")

    elif(("open" in p) or ("start" in p)) and (("explorer" in p) or ("file explorer" in p)):

        pyttsx3.speak("Opening file explorer")

        os.system("start explorer")

    elif(("open" in p) or ("start" in p)) and (("Task Manager" in p) or ("task manager" in p)):

        pyttsx3.speak("Opening Task Manager")

        os.system("taskmgr")

    elif(("open" in p) or ("start" in p)) and (("alarm" in p) or ("clock" in p)):

        pyttsx3.speak("Opening clock")

        os.system("start ms-clock:")

    elif(("open" in p) or ("start" in p)) and ("calendar" in p):

        pyttsx3.speak("Opening calender")

        os.system("start outlookcal:")

    elif(("open" in p) or ("start" in p)) and ("calculator" in p):

        pyttsx3.speak("Opening calculator")

        os.system("calc")

    elif(("open" in p) or ("start" in p)) and (("vs code" in p) or ("visual studio code" in p)):

        pyttsx3.speak("Opening vs code")

        os.system("code")

    elif(("open" in p) or ("start" in p)) and (('action center' in p) or ('notification' in p)):

        pyttsx3.speak("Opening action center")

        os.system("start ms-actioncenter:")

    elif("open" in p) and ("paint" in p):

        pyttsx3.speak("Opening paint")

        os.system("start ms-paint:")

    elif(("open" in p) or ("start" in p)) and (("Word" in p) or ("word" in p)):

        pyttsx3.speak("Opening Microsoft Word")

        os.system("winword")

    elif(("open" in p) or ("start" in p)) and (("Excel" in p) or ("excel" in p)):

        pyttsx3.speak("Opening Microsoft Excel")

        os.system("excel")

    elif(("open" in p) or ("start" in p)) and ("edge" in p):

        pyttsx3.speak("Opening Microsoft Edge")

        os.system('start microsoft-edge:')

    elif(("open" in p) or ("start" in p)) and ("mail" in p):

        pyttsx3.speak("Opening mail")

        os.system("start outlookmail:")

    elif(("open" in p) or ("start" in p)) and ("cmd" in p):

        pyttsx3.speak("Opening command prompt")

        os.system("start cmd.exe")

    elif("close" in p) or ("stop" in p) or ("exit" in p):

        pyttsx3.speak("Thank you for using me!")

        exit()

    else:

        pyttsx3.speak("I do not understand your command.")

        print("Try again\n")
