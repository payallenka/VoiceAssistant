import speech_recognition as sr
import pyttsx3
import tkinter

window = tkinter.Tk()
window.title("App name") #Renames the title of the window


listener = sr.Recognizer() #Listener for the speech recoginition module
engine = pyttsx3.init() #Engine for Pythontts
voices = engine.getProperty('voices') #get a property called voice form the sr module
engine.setProperty('voice', voices[1].id) #Set the properties of the voice

f = open("C:\\Users\\Administrator\\OneDrive\\Documents\\CS project 12th\\Command.txt", "r") #User command file
g = open("C:\\Users\\Administrator\\OneDrive\\Documents\\CS project 12th\\Reply.txt","r")#The reply of the Voice Assistant
list2 = g.readlines()



try:
    with sr.Microphone() as source: #mic = source
        listener.adjust_for_ambient_noise(source,duration=1) #According to Background noise it changes.
        voice = listener.listen(source) #the listener will listen to the source
        st = listener.recognize_google(voice) #To convert the speech to using google api
        print(st)
        index = 0
        for line in f: 
            if st in line: #Searching for the string at a particular line in the command file
                print(list2[index])
                engine.say(list2[index]) 
                engine.runAndWait()
                break
            index+=1

except:
    print("Failed recoginizing your voice")

