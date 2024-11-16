import speech_recognition as sr
import webbrowser
import time
import keyboard

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")

        audio = r.listen(source)
    try:
        print("Recognising....")
        text = r.recognize_google(audio, language='en-in')
        print(text)
        return text
    except Exception as e:
        print(e)
        return e
    
if __name__ == "__main__":
    while True:
        command = takecom()
        if "open curtain" in command or "open cur" in command or "rujal chor" in command:
            try:
                webbrowser.open("https://sgp1.blynk.cloud/external/api/update?token=CXWjPxWhRTGkyq8rO1_CL7ZiRsnc-VtS&d5=1")
                time.sleep(2)
                keyboard.press_and_release('ctrl + f4')
                time.sleep(1)
                webbrowser.open("https://sgp1.blynk.cloud/external/api/update?token=CXWjPxWhRTGkyq8rO1_CL7ZiRsnc-VtS&d5=0")
                time.sleep(2)
                keyboard.press_and_release('ctrl + f4')
            except Exception as e:
                print("Error in opening curtain:", e)

        elif "close curtain" in command or "close cur" in command:
            try:
                webbrowser.open("https://sgp1.blynk.cloud/external/api/update?token=CXWjPxWhRTGkyq8rO1_CL7ZiRsnc-VtS&d4=1")
                time.sleep(2)
                keyboard.press_and_release('ctrl + f4')
                time.sleep(1)
                webbrowser.open("https://sgp1.blynk.cloud/external/api/update?token=CXWjPxWhRTGkyq8rO1_CL7ZiRsnc-VtS&d4=0")
                time.sleep(2)
                keyboard.press_and_release('ctrl + f4')
            except Exception as e:
                print("Error in closing curtain:", e)

        elif "exit" in command:
            print("Bye Bye")
            break