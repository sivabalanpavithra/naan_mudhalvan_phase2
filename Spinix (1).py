import datetime
import os
import psutil
import pyttsx3
import pyautogui
import wikipedia
import pyjokes
import speech_recognition as sr
import requests, json
import webbrowser
import sympy as sp
from textblob import TextBlob

# to initialise the engine
Engine = pyttsx3.init()
Engine.setProperty('rate', 200)
voices = Engine.getProperty('voices')
Engine.setProperty('voices', voices[0].id)
Engine.setProperty('volume', 1)

_name__ = "main1"
Engine1 = ""
query = ""
EQ1 = Engine1 or query

# change voice
def voice_ch():
    speak('this is my one of my voices')
    set_voice(Engine, voices[1].id)
    rate = Engine.getProperty('rate')
    Engine.setProperty('rate', rate - 50)
    volume = Engine.getProperty('volume')
    Engine.setProperty('volume', (volume + 0.25))
    speak('this is my one of my voices')



def set_voice(engine, voice_id):
    engine.setProperty('voice', voice_id)


# used to  speak
def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()

# get the Cpu perfomance :
def cpu():
    c = 'Cpu usage is at:'
    usage = str(psutil.cpu_stats())
    print('Cpu usage is at:')

    print(usage)
    speak(c + usage)

    battery = psutil.sensors_battery()
    print('Battery percentage is at:', str(battery.percent))
    k = str('battery percentage is at:')
    speak(k + str(battery.percent))


# get the date
def date():
    year = str(int(datetime.datetime.now().year))
    month = str(int(datetime.datetime.now().month))
    date = str(int(datetime.datetime.now().day))
    print("Then current date:")
    day = str("" + date + '/' + month + '/' + year + "")
    print(day)
    speak(date), speak(month), speak(year)


# function to list the function of the dragon Ai
def functions():
    feat = str('the feature that i have:')
    f = str('I can help to do lot of things like.....')
    f1 = str('I can tell you the current time and date .')
    f2 = str('I can tell you the current weather of a city.')
    f3 = str('I can tell you the battery percentage and cpu usage.')
    f4 = str('I can create remainder list ')
    f5 = str('I can take screenshots.')
    f6 = str('I can tell you a non funny jokes.')
    f7 = str('I can open website.')
    f8 = str('I can search some thing on wikipedia.')
    f9 = str('I can change my voice from male to female  and vice-versa and yes more things.')
    boss = str('My boss is working on this system to add more features.....')
    waa = str('Tell me what can i do for you ?.')
    print(feat)
    speak(feat)
    print(f)
    speak(f)
    print(f1)
    speak(f1)
    print(f2)
    speak(f2)
    print(f3)
    speak(f3)
    print(f4)
    speak(f4)
    print(f5)
    speak(f5)
    print(f6)
    speak(f6)
    print(f7)
    speak(f7)
    print(f8)
    speak(f8)
    print(f9)
    speak(f9)
    print(boss)
    speak(boss)
    print(waa)
    speak(waa)


# function to greet the user
def greetme():
    print("hello..")
    speak('hello')
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak('Good Morning')

    elif (hour >= 12 and hour < 18):
        speak('Good afternoon')

    elif (hour >= 18 and hour < 24):
        speak('Good Evining')
    else:
        speak('Good Night sweetdreams')


# Get the current time
def time():
    Time = datetime.datetime.now().strftime("%H:%M")
    k = str('the current time:')
    t = str(Time)
    print(k)
    speak(k)
    print(t)
    speak(t)



def conversation(engine1):
    engine1 = engine1.lower()  # Convert input to lowercase for consistent matching

    if "hi" in engine1 or "hello" in engine1 or "hey" in engine1:
        response = "Hello! How can I help you today?"
        print(response)
        speak(response)

    elif "whatare you doing now" in engine1:
        response2 = "I am here to assist you. What can I do for you?"
        print(response2)
        speak(response2)

    elif "how are you" in engine1:
        response = "I am just a program, but thank you for asking!"

        speak(response)
    elif "your name" in engine1:
        response = "I am your Dragon AI the desktop Assistant. Nice to meet you!"
        print(response)
        speak(response)
    elif "thank you" in engine1:
        response = "You are welcome!"
        print(response)
        speak(response)
    else:
        response = "I am sorry,\n I didn’t understand that. Can you please repeat?"
        print(response)
        speak(response)

# get joke
def joke():
    jok = str(pyjokes.get_joke("en"))
    print(jok)
    speak(jok)

# get the personal information about Ai
def persional():
    info = str(
        'I am spinix AI version Beta\nI am an AI assistent,\nI have speed 1 Terahertz memory 1 gega byte \nI am developed by Karthik at 2024')
    print(info)
    # it is used to speak the about itself
    speak(info)
    print('I hope you no me')
    # it is used to speak the above statement
    speak('I hope you no me')

# remainder
def remainder():
    speak(str('What is the remainder:'))
    # data=take_audio()
    data1 = str(input(""))
    speak('you said to remember that' + data1)
    remainder_file = open("data.txt", 'a')
    remainder_file.write('\n')
    remainder_file.write(data1)
    remainder_file.close()

# remainder list
def re_list():
    remainder_file = open("data.txt", "r")
    speak(str('You said me to remember this:') + remainder_file.read())
    print(remainder_file.read())

# play song
def song():
 try:
    pl = str('playing')
    p2='Enter song name:'
    speak(p2)
    print(p2)
    s =get_input()
    print(pl + ".....")
    song_dir = "C:\\Users\\DK_89K13\\Music\\Playlists"
    song_list= os.listdir(song_dir)
    matched_songs = [song for song in song_list if s.lower() in song.lower()]
    os.startfile(os.path.join(song_dir,matched_songs[0]))
 except Exception as e:
     speak('sorry,the song is not in the list')
     print('the song is not in the list')

# play songs in online
def Song2():
    p2='Enter song name:'
    print(p2)
    speak(p2)
    song=get_input()
    pl = str('playing')
    url = "https://open.spotify.com/search/"+song
    webbrowser.open_new_tab(url)
    speak(pl)

# Used to take the screenshot
def screen():
    img = pyautogui.screenshot()
    img.save("C:\\Users\II-YEAR\Pictures\\test_shot.png")

# search in chrome
def search(engine1):
    if ('search ' in engine1):
        engine1 = engine1.replace("search", "")
    webbrowser.open("http://google.com/search?q=" + query or Engine1)

# get city weather report
def weather():
    # api that is generated from the open source
    api = "e881d729851b8a9f57345dd811ac1042"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    speak(str('Tell me the city'))
    # city=takeCommand()
    city = input("tell me the city:")
    speak(str(city))
    # used to get the url for the api key
    comp_url = base_url + city + "&appid=" + api
    responce = requests.get(comp_url)
    wea = responce.json()
    if wea["cod"] != "404":
        y = wea["main"]
        cur_temp = y["temp"]
        cur_pres = y["pressure"]
        cur_humi = y["humidity"]
        z = wea["weather"]
        wea_desc = z[0]["description"]
        r = ("In " + city + " Temperature is :" + str(
            int(cur_temp - 273.15)) + " Degree Clecius" + ", Atmospheric preesure : " + str(
            cur_pres) + " hpa unit " + ",humidity is " + str(cur_humi) + " percentage "" and " + str(wea_desc))
        k = str(r)
        print(k)
        speak(k)
    else:
        print("City is not Founded")
        speak('city not founded')

def search_wikipedia():
    sent = str(engine1)
    sent1 = sent
    if ('wikipedia' in sent or 'what' in sent or 'who' in sent or 'where' in sent or 'when' in sent):
        # print("Searching.....")
        print("Searching.....")
        if ('wikipedia ' in sent):
            sent = sent.replace("wikipedia", "")
        elif ('search' in sent):
            sent = sent.replace("search", "")
        elif ('what' in sent):
            sent = sent.replace("what", "")
        elif ('when' in sent):
            sent = sent.replace("when", "")
        elif ('what' in sent):
            sent = sent.replace("where", "")
        elif ('what' in sent):
            sent = sent.replace("who ", "")
        elif('who' in sent):
            sent=sent.replace("who","")
        else:
            sent = sent.replace("is", "")
        result = wikipedia.summary(sent, sentences=2)
        print(sent1, "\n")
        print(result)
        speak(result)

# to sign out
def wish_end():
    sin = str('I am Signing off....')
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        print("Good Morning...")
    elif (hour >= 12 and hour < 18):
        print("Good Afternoon...")
    elif (hour >= 18 and hour < 24):
        print("Good evining...")
    else:
        print("Good Nigh...Sweetdreams")
    print(sin)
    speak(sin)
    quit()

# get the input from user
def get_input():
    input1 = str(input())
    if input1:
        return input1
    else:
        Engine1 = str(take_command())
        return Engine1

# get the audio input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Tell me what should i do...")
        audio = recognizer.listen(mic)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You tell me: {text}")
            speak('wait a second')
        except sr.UnknownValueError():
            print("I cannot could not understand you")
        except sr.RequestError as e:
            print("could you please say that again :")
    return text

# open youtube
def youtube():
    url = "https://www.youtube.com"
    webbrowser.open_new_tab(url)

# open face book
def facebook():
    url = "https://www.facebook.com/login/"
    webbrowser.open_new_tab(url)

# open instagram:
def instagram():
    url = "https://www.instagram.com/accounts/login/"
    webbrowser.open_new_tab(url)

# open indianews
def english_H():
    qustion ="which wep site you want to open"
    print(qustion)
    speak(qustion)
    option="The Hindu\ntimes of india\nindian exprss\nindia today\nndtv"
    print(option)
    speak(option)
    choice=get_input()
    tk='ok boss'
    if choice== 1 or'the hindu':
        url1 = "https://www.thehindu.com/"
        webbrowser.open_new_tab(url1)
    elif choice== 2 or'times of india' :
        url2 = "https://timesofindia.indiatimes.com/home/headlines"
        webbrowser.open_new_tab(url2)
    elif choice == 2 or 'times of india':
        url3 = "https://indianexpress.com/"
        webbrowser.open_new_tab(url3)
    elif choice == 2 or 'times of india':
        url4 = "https://www.indiatoday.in/"
        webbrowser.open_new_tab(url4)
    elif choice == 2 or 'times of india':
        url5 = "https://www.ndtv.com/"
        webbrowser.open_new_tab(url5)
    speak(tk)

# open tamilnews:
def tamil_H():
    qustion = "which wep site you want to open"
    print(qustion)
    speak(qustion)
    option = "dailythanthi\nsamayam\nnews18\nvikatan\nindian exprss"
    print(option)
    speak(option)
    choice = get_input()
    tk = 'ok boss'
    if choice == 1 or 'dailythanthi':
        url1 = "https://www.dailythanthi.com/News/"
        webbrowser.open_new_tab(url1)
    elif choice == 2 or 'samayam':
        url2 = "https://tamil.samayam.com/"
        webbrowser.open_new_tab(url2)
    elif choice == 2 or 'news18':
        url3 = "https://tamil.news18.com/"
        webbrowser.open_new_tab(url3)
    elif choice == 2 or 'vikatan':
        url4 = "https://www.vikatan.com/news"
        webbrowser.open_new_tab(url4)
    elif choice == 2 or 'indian exprss':
        url5 = "https://tamil.indianexpress.com/"
        webbrowser.open_new_tab(url5)
    speak(tk)

# open browser:
def chrome():
    if ('search on chrome' in engine1 or 'in chrome' in engine1 or 'search in chrome' in engine1 or 'searchinchrome' in engine1):
        engine1.replace('search', '')
        engine1.replace('searchinchrome ','')
        engine1.replace('in chrome', '')
        engine1.replace('search in chrome', '')
    url = ("https://www.google.com/search?q=" + engine1)
    webbrowser.open_new_tab(url)

# open edge browser
def edge():
    if ('searchinedge' in engine1 or 'in edge' in engine1 or 'search in edge' in engine1 or 'search on edge' in engine1 or 'on edge' in engine1):
        engine1.replace('search', '')
        engine1.replace('searchinchrome','')
        engine1.replace('in chrome', '')
        engine1.replace('search in chrome', '')
        url = ("https://www.bing.com/search?q=" + engine1)
        webbrowser.open_new_tab(url)

# perform maths
def symbol(input1):
    target = ('+' or '-' or '/' or '*')
    r = 'it is a expression'
    positions = []

    for position, char in enumerate(input1):
        if char == target:
            print(r)
            positions.append(position)

    if r != 'it is a string':
        try:
            result = sp.sympify(input1)
            print(f'the out put of the expresion is {result}')
            speak(f'the out put of the expresion is {result}')
        except Exception as e:
            return f"Error: {e}"

#inventor
def father():
    print('i am developed by Karthik develpor')
    speak('i am developed by Karthikeyan develpor')
    print("he is a second year student\n studing in GCE Erode college")
    speak("he is a second year student\n studing in GCE Erode college")

#Train ticket booking system
#def train_ticket():

#conversation2
def feeling(engine1):
    if 'predict my mood' in engine1 or "can you find how I am feeling now" in engine1:
        res = "Yeah, I can predict how you are feeling now by asking some questions."
        print(res)
        speak(res)

        questions = (
            "How are you feeling today?",
            "What has been on your mind lately?",
            "Is there anything bothering you?",
            "What made you smile recently?",
            "How do you feel about your day so far?"
        )
        ans_response = []

        # Analyze the mood
        def analyze_mood(response2):
            analysis = TextBlob(response2)
            if analysis.sentiment.polarity < -0.5:
                return "depressed"
            elif analysis.sentiment.polarity < 0.0:
                return "sad"
            elif analysis.sentiment.polarity > 0.5:
                return "happy"
            elif analysis.sentiment.polarity > 0.0 and analysis.sentiment.polarity < 0.5:
                return "neutral"
            else:
                return "angry"

        # Get input from user
        for question in questions:
            speak(question)
            response = input(question + " ")
            ans_response.append(response)

        # Analyze the mood based on responses
        overall_mood = "neutral"
        for response in ans_response:
            mood = analyze_mood(response)
            if mood == "happy":
                overall_mood = "happy"
                break
            elif mood == "angry":
                overall_mood = "angry"
                break
            elif mood == "depressed":
                overall_mood = "depressed"
                break
            elif mood == "sad" and overall_mood != "happy":
                overall_mood = "sad"
                break
            else:
                overall_mood = 'neutral'

        # Provide feedback based on overall mood
        if overall_mood == "happy":
            print("I'm glad to hear that you're feeling happy! Keep smiling!")
            speak("I'm glad to hear that you're feeling happy! Keep smiling")
        elif overall_mood == "sad":
            print("I'm sorry to hear that you're feeling sad.\n It's okay to feel this way sometimes.")
            speak("I'm sorry to hear that you're feeling sad.\n It's okay to feel this way sometimes.")
        elif overall_mood == "depressed":
            print("It sounds like you're feeling really down.\n Please take care of yourself and consider talking to someone.")
            speak("It sounds like you're feeling really down.\n Please take care of yourself and consider talking to someone.")
        elif overall_mood == "angry":
            print("It seems like you're feeling angry.\n It's important to express your feelings and find healthy ways to cope.")
            speak("It seems like you're feeling angry.\n It's important to express your feelings and find healthy ways to cope.")
        else:
            print("It seems like you're feeling neutral. Sometimes, \nthat's just how life goes.")
            speak("It seems like you're feeling neutral. Sometimes,\n that's just how life goes.")

# program starts where
greetme()
if _name__ == "main1":
    i = 1
    while (True):

        query = get_input()
        engine1 = str(query or Engine1)
        engine1 = engine1.lower()

        if ("cpu performance" in engine1 or "cpu" in engine1 or "tell me cpu stat" in engine1 or "cpu stat" in engine1):
            cpu()
        elif ("who is your creater" in engine1 or "who is your father" in engine1):
            father()
        elif ("hi" in engine1 or "hello" in engine1 or "hey" in engine1 or "what are you doing now" in engine1 or "what is your name" in engine1):
            conversation(engine1)
        # time
        elif ("time" in engine1 or "current time" in engine1 or "tell me current time" in engine1 or "show me the current time" in engine1 or "what is the time now" in engine1):
            time()
        # date
        elif ("date" in engine1 or "today date" in engine1 or "todays date" in engine1 or "Todaydate" in engine1 or "tell me the date" in engine1 or "show me the current date" in engine1):
            date()
        # joke
        elif ("say a joke" in engine1 or "joke" in engine1 or "tell me a joke" in engine1):
            joke()
        # personal information
        elif ("about yourself" in engine1 or "tell about yourself" in engine1 or "aboutyou" in engine1):
            persional()
        # what the AI can do
        elif ("features you have" in (Engine1 or query) or "tell me features you have" in (Engine1 or query) or "help" in (Engine1 or query) or "tell me your power" in (Engine1 or query) or "your power" in (Engine1 or query)):
            functions()
        # play song offline
        elif ("play a song" in (Engine1 or query) or "play song" in (Engine1 or query) or "play song offline" in engine1 or "play offline songs" in engine1):
            song()
        # play song online
        elif ("play a song in online" in (Engine1 or query) or "play a online song" in (Engine1 or query) or "play song on online" in engine1 or "play online song" in engine1 or "play song in online" in engine1 or "play online on songs" in engine1 or "online song" in engine1 or "play song online" in engine1):
            Song2()
        # create a reminder
        elif ("create a reminder list" in (Engine1 or query) or "reminder" in (Engine1 or query) or "note this as reminder" in engine1 or "take reminder" in engine1 or "takereminder" in engine1 or "note this reminder" in engine1 or "note as reminder" in engine1):
            remainder()
        # list the reminder
        elif ("do you know anything" in (Engine1 or query) or "reminder list" in (Engine1 or query) or "list the reminder" in (Engine1 or query) or "show me reminders" in engine1):
            re_list()
        # take screenshot
        elif ("take a screenshot" in (Engine1 or query) or "screenshotthis" in (Engine1 or query)):
            screen()
        # sign out
        elif ("signout" in (Engine1 or query) or "logout" in (Engine1 or query) or "turnoff" in (
                Engine1 or query) or "quit" in (Engine1 or query)):
            wish_end()
        # weather
        elif ("what is the weather" in (Engine1 or query) or "current weather" in (Engine1 or query) or "weather in" in (Engine1 or query)):
            weather()
        #wikipeia
        elif ("wikipedia" in engine1 or "what" in engine1 or "who" in engine1 or "where" in engine1 or "when" in engine1):
            search_wikipedia()
        # voice change
        elif ("change voice" in (Engine1 or query) or "change your voice" in (Engine1 or query) or "voice change" in (Engine1 or query) or "voicechange" in (Engine1 or query)):
            voice_ch()
        # open browser
        elif ("browser open" in engine1 or "open browser" in engine1):
            search(engine1)
        # chrome
        elif ("search on chrome" in engine1 or "in chrome" in engine1 or "search in chrome" in engine1 or "open chrome" in engine1 or "openchrome" in engine1):
            chrome()
        # edge
        elif ("search on edge" in engine1 or "on edge" in engine1 or "search in edge" in engine1 or "open edge" in engine1 or "openedge" in engine1):
            edge()
        # english headlines
        elif ("openenglishnews" in engine1 or "open english news" in engine1 or "english news" in engine1 or "englishnew" in engine1 or "english headlines" in engine1 or "englishheadlines" in engine1):
            english_H()
        # tamil headlines
        elif ("opentamilnews" in engine1 or "open tamil news" in engine1 or "tamil news" in engine1 or "tamilnew" in engine1 or "tamil headlines" in engine1 or "tamilheadlines" in engine1):
            tamil_H()
        # youtube
        elif ("open youtube" in engine1 or "openyoutube" in engine1 or "youtube" in engine1):
            youtube()
        # open facebook
        elif ("open facebook" in engine1 or "openfacebook" in engine1 or "facebook" in engine1):
            facebook()
        # instagram
        elif ("open instagram" in engine1 or "openinstagram" in engine1 or "instagram" in engine1):
            instagram()
        # mathematical operation
        elif ("multiple" in engine1 or "subtract" in engine1 or "addition" in engine1 or "divide" in engine1 or "*" in engine1 or "-" in engine1 or "+" in engine1 or "/" in engine1):
            symbol(engine1)
        elif('can you find how iam feeling now'in engine1 or 'predict my mood' in engine1 or'sad' in engine1 or 'happy' in engine1 or 'boring' in engine1 or 'depresed' in engine1 or 'angry' in engine1):
            feeling(engine1)
        # tell you
        # if it cannot undestand what you are telling
        else:
            k = str('i cannot Understand what you are telling..')
            print(k)
            speak(k)