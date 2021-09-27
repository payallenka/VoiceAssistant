from shutil import register_unpack_format
from requests.models import Response
import speech_recognition as sr
import pyttsx3
import tkinter
from tkinter import Canvas, Frame, Image, Label, StringVar, Tk, font
from tkinter.constants import ANCHOR, BOTTOM, E, END, GROOVE, RAISED, RIDGE, RIGHT, SUNKEN, TOP, W, Y
from typing import Text
import os



'''
#API
window = tkinter.Tk()
window.title("App name")
window.geometry("320x640")
f = Frame(window)
x = f.grid_size()

# Add image file
bg = tkinter.PhotoImage(file = "backgroundf.png")
# Show image using label
background = tkinter.Label( window, image = bg)
background.place(x = 0, y = 0)

userimg = tkinter.PhotoImage(file = 'user1.png')
userlabel = tkinter.Label(window, image = userimg, bg = '#3D4154')
userlabel.grid(row = 0, column = 1, sticky=E,pady=(50,0))

window.columnconfigure((0,1), weight=1)

'''
listener = sr.Recognizer() #Listener for the speech recoginition module
engine = pyttsx3.init() #Engine for Pythontts
voices = engine.getProperty('voices') #get a property called voice form the sr module
engine.setProperty('voice', voices[1].id) #Set the properties of the voice
'''
def voicerecog():
    with sr.Microphone() as source: #mic = source
            listener.adjust_for_ambient_noise(source,duration=1) #According to Background noise it changes.
            Atxt.set("Listening...")
            voice = listener.listen(source) #the listener will listen to the source
            v = listener.recognize_google(voice) #To convert the speech to using google api
            return v
choice = None
def clicked():
    global choice
    choice = "Clicked"

def mic():
    while True:
        global choice
        if choice == "Clicked":
            d = voicerecog()
            return d


Utxt = tkinter.StringVar()
Utxt.set("User Text Here")
text = tkinter.Label(window, textvariable = Utxt, bg = "#8B7DF6", wraplength= 250, pady = 1, padx = 1, fg = '#020402')
text.grid(row = 1, column=1, sticky=E)

Atxt = tkinter.StringVar()
Atxt.set("Assistant Reply here")
text1 = tkinter.Label(window, textvariable = Atxt, wraplength= 250, pady = 1, padx = 1, bg = '#8B7DF6',fg = '#020402')
text1.grid(row = 2, column=0, sticky = W)

window.resizable(0, 0)

'''


f = open("C:\\Users\\Administrator\\OneDrive\\Documents\\CS project 12th\\Command.txt", "r") #User command file
g = open("C:\\Users\\Administrator\\OneDrive\\Documents\\CS project 12th\\Reply.txt","r")#The reply of the Voice Assistant
list2 = g.readlines()


def movie_info(title):
    import requests
    #
    api_key = 'a203edc8'
    url = f'http://www.omdbapi.com/?apikey={api_key}&'
    params = {'t': title, 'j': 'json'}
    r = requests.get(url, params=params)
    return r.json()


def wolfarmapla_api(query):
    import wolframalpha
    app_id = 'JHUURP-6T6EQ4Q8RV'
    client = wolframalpha.Client(app_id)
    #
    res = client.query(query)
    answer = next(res.results).text
    return answer


def coronavirus_update(region = 'global'):
    ''' returns graph of coronavirus in different countries'''
    import requests
    import shutil
    #
    url = 'https://corona.dnsforfamily.com/graph.png?c='
    r = requests.get(url + region, stream = True)
    filename = 'graph.png'
    
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        return 'Image sucessfully Downloaded: ',filename
    else:
        return 'Image Couldn\'t be retreived'


def weather_info(query:str):
    import requests
    url = "https://weatherapi-com.p.rapidapi.com/timezone.json"
    querystring = {"q":query}
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "a977f43547msh295a12c68272218p1c3bb8jsn2da4807b3f1c"}
    r = requests.request("GET", url, headers=headers, params=querystring)
    return r.json()



def speak(message):
    engine.say(message)
    engine.runAndWait()

def mic():
    listener.adjust_for_ambient_noise(source,duration=1) #According to Background noise it changes.
    voice = listener.listen(source) #the listener will listen to the source
    v = listener.recognize_google(voice) #To convert the speech to using google api
    return v

while True:
    try:
        with sr.Microphone() as source: #mic = source
            print("How may i help you?")
            st = mic()
            print(st)
            if "updates" in st:#Covid-Updates
                msg = "Please tell your country code"
                print(msg)
                speak(msg)
                ctid = mic()
                print(ctid)
                print(coronavirus_update(ctid))
                

                #region = mic()
            elif "movie information" in st:
                msg = "Please name the movie"
                print(msg)
                speak(msg)
                
                minfo = mic()
                mi = movie_info(minfo)
                #mi = title
                if mi['Response'] == 'True':
                    for item in mi['Ratings']:
                        items = item['Source']+' - '+item['Value']
                    temp = f'''Title:{mi['Title']}\n Released: {mi['Released']}\nRated: {mi['Rated']}\nRuntime: {mi['Runtime']}\nGenre:{mi['Genre']}\nDirector: {mi['Director']}\nActors: {mi['Actors']}\nLanguage: {mi['Language']}\n Ratings:{items}\nPlot: {mi['Plot']}\nPoster: {mi['Poster']}''' 
                    speak(temp)
                    print(temp)
                else:
                    speak("Movie not found")

            elif "weather information" in st:
                msg = "Please name your city/country"
                print(msg)
                speak(msg)
                ctid = mic()
                #query = ctid
                wi = weather_info(ctid)
                if 'error' in wi:
                    speak("Weather or Country Name Unavailable")
                else:
                    a = wi['location']
                    temp = f'''Name: {a['name']}\nRegion: {a['region']}\nCountry: {a['country']}\nLatitude: {a['lat']}\nLongitude: {a['lon']}\nTimezone: {a['tz_id']}\nLocal Date and Time: {a['localtime']}'''
                    print(temp)
                    speak(temp)

            elif "Question" in st:
                try:
                    msg = "Please ask your question"
                    speak(msg)
                    print(msg)
                    q = mic()
                    query = q
                    print(temp)
                    speak(temp)
                except:
                        print("Invalid Question")     
            elif 'close' in st:
                break       
            else:
                index = 0
                ans = mic()
                for line in f: 
                    if st in line: #Searching for the string at a particular line in the command file
                        ans = list2[index]
                        break
                    index += 1
                if ans == "":
                    speak("Invalid Question")
                else:
                    speak(ans)
                    print(ans)
    except:
        speak("Failed recoginizing your voice")
'''
photo = tkinter.PhotoImage(file = "mic.png")
micbtn = tkinter.Button(window, text = 'Click Me !', image = photo, bg = '#8B7DF6', border = 0, command = clicked).place(x = 155,y=580)

window.mainloop()
'''