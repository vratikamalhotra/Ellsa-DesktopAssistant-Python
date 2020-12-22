import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon vratika!")
    else:
        speak("Good evening vratika!")
    
    speak("i am Elsa! How may i Help you?")

def takeCommand():

    ''' it takes mic input from user and return string output'''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('malhotravratika@gmail.com','password')
    server.sendmail('malhotravratika@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'personal documents' in query:
            speak("ok dear here it is")
            folder_path= 'C:\\Users\\vratika malhotra\\Desktop\\Vratika'
            os.startfile(folder_path) 

        elif 'resume' in query:
            speak("opening your resume")
            folder_path= 'C:\\Users\\vratika malhotra\\Desktop\\Vratika\\Vratika Malhotra.pdf'
            os.startfile(folder_path) 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Its {strTime}")
        
        elif 'send email' in query:
            try:
                speak(" Alrighty, to whom sould i address?")
                to=takeCommand()
                speak("ok")
                speak("What should i say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email sent")
            except Exception as e:
                print(e)
                speak("Sorry! not able to send the email at the moment")

        elif 'stop' in query:
            exit()     

            
        elif 'thank you' in query:
            speak("No problem. Here for your help")

