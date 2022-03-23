from random import choice
from tempfile import TemporaryFile
from urllib.request import OpenerDirector
import pyttsx3
import speech_recognition as sr
from utils import opening_text
from utils import greetings
import subprocess as sp
import cv2
import wikipedia
from utils import wikipedia1
import sys
from googlesearch import search
from utils import goodbye
import webbrowser
from utils import findings
from utils import wishings
import spotipy
import json
from pynput.keyboard import Key, Controller
#from Private import email, email_password
from PyDictionary import PyDictionary as Diction
import os
import numpy as np
import pyautogui as p
import math
import time
from functions import *
from cube import *
import smtplib
from intents import screenshot

my_list = screenshot
i = []
element = []
for index in i:
    element.append(my_list[index])
print(element)


keyboard = Controller()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("   ")
    engine.say(text)
    print("   ")
    engine.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language = 'en-in')
            print(f"You said : {query}")
        
        except Exception as e:
            return "none"
        
        return query

def Taskexe():
    
    global screenshot
    global choice
    p.press('esc')
    print("Welcome back sir")
    speak("Welcome back sir")

    while True:
        query = takecommand()
    
        if 'hello' in query:
            speak(choice(greetings))
 
        elif "Google search" in query:
            speak(choice(findings))
            query_command = query.replace("jarvis", "")
            query_command = query.replace("Google search", "")
            web = "https://www.bing.com/search?q=" + query_command
            webbrowser.open(web)
            speak("Done sir")
    
        elif "Youtube search" in query:
            speak(choice(findings))
            query_command = query.replace("jarvis", "")
            query_command = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query_command
            speak("Done sir")
            webbrowser.open(web)
            
        elif 'camera' in query:
                speak(choice(opening_text))
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    raise IOError("Cannot open camera")
        
                while True:
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA)
                    cv2.imshow('Input', frame)
            
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        
                cap.release()
                cv2.destroyAllWindows()
                
        elif 'Wikipedia inquiry for' in query:
                speak(choice(findings))
                query_command = query.replace("Edith", "")
                query_command = query.replace("Wikipedia inquiry for", "")
                query_command = query.replace("Wikipedia inquiry", "")
                query_command = query.replace("Wiki", "")
                query_command = query.replace("Wikipedia", "")
                web = 'https://en.wikipedia.org/wiki/' + query_command
                webbrowser.open(web)
                speak("Launched")
    
        elif "that's all" in query:
                speak(choice(goodbye))
                break
                
        elif 'website' in query:
            speak(choice(findings))
            query_command = query.replace("Edith", "")
            query_command("Website", "")
            web1 = query.replace("open", "")
            web2 = "https://www." + web1 + ".com"
            webbrowser.open(web2)
            speak("Launched")
        
        elif "I'm doing good" in query:
            speak(choice(wishings))

        elif 'start' in query:
            p.press('spacebar')
        
        elif 'pause' in query:
            p.press('k')
        
        elif 'restart' in query:
            p.press('0')
            
        elif 'mute' in query:
            p.press('m')
        
        elif 'scan' in query:
            speak("opening camera")
            cascPath = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            video_capture = cv2.VideoCapture(0)
            
            while True:
                ret, frame = video_capture.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor = 1.1,
                    minNeighbors = 5,
                    minSize = (30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
                
                cv2.imshow('Video', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
             
            video_capture.release()
            cv2.destroyAllWindows()
        
        elif 'email' in query :
            def mail(sender_email, sender_password, receiver_email, msg):
                try:
                    mail = smtplib.SMTP('smtp.gmail.com', 587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login(sender_email, sender_password)
                    mail.sendemail(sender_email, receiver_email, msg)
                    mail.close()
                    return True
                except Exception as e:
                    print(e)
                    return False
            mail()
            
        elif screenshot in query :
            speak("Ok sir, what would be the file name")
            path = takecommand()
            path1name = path + ".png"
            path1 = 'C:/Users/kshit/.conda/screenshots/' + path1name
            speak("Taking screenshot")
            kk = p.screenshot()
            kk.save(path1)
            os.startfile('C:/Users/kshit/.conda/screenshots')
            speak("Here is your screenshot")
        
        
            

Taskexe()

'''
   
def Face_recognition():   
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('C:/Users/kshit/.conda/trainer/trainer.yml')
    cascPath = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
    FaceCascade = cv2.CascadeClassifier(cascPath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 2

    names = ['', 'Kshithij', 'Kshithij']

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img = cam.read()
    
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = FaceCascade.detectMultiScale(
            converted_image, 
            scaleFactor = 1.3,
            minNeighbors = 5,
            minSize =(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
            )
    
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+y, y+h), (0,255,0), 2)
        
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])
        
            if (accuracy < 50):
                id = names[id]
                accuracy = " {0}%".format(round(50 - accuracy))
        
            else:
                id = "unknown"
                accuracy = " {0}%".format(round(50 - accuracy))
        
            cv2.putText(img, str(id), (x+5, y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255,255,0), 1)
    
        cv2.imshow('camera', img)
    
        k = cv2.waitKey(10) & 0xFF
        if k == 27:
            break

    print("Thanks for using this program, have a good day")
    cam.release()
    cv2.destroyAllWindows()

Face_recognition()

'''
'''''
        def hello():
            query = takecommand()
            if 'hello' in query:
                speak(choice(greetings))
        hello()
     
    

        def google_search():
            query = takecommand()
            if "Google search" or "Can you do a google search for me" or "Do a google search for me" or "I need to search something up" in query:
                speak("ok sir")
                speak("what would you like to search sir")
                query_search = takecommand()
                for i in search(query_search, tld="co.in", num=10, stop=10, pause=2):
                    print(i)
                    
        google_search()


           
        def youtube_search():
            query = takecommand()
            if "youtube search" or "youtube" or "search on youtube" in query:
                speak("Ok sir this is what I found for your search")
                query = query.replace("jarvis", "")
                query = query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                speak("Done sir")
                webbrowser.open(web)
        youtube_search()


def camera():
            query = takecommand()
            if 'camera' in query:
                speak(choice(opening_text))
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    raise IOError("Cannot open camera")
        
                while True:
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA)
                    cv2.imshow('Input', frame)
            
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        
                cap.release()
                cv2.destroyAllWindows()
        camera()
        
        def wiki():
            query_command = takecommand()
            if 'Wikipedia inquiry for' or 'Wikipedia' or 'Wiki' or 'Wikipedia inquiry' in query_command:
                speak("sure sir, this is what I found")
                query = query_command.replace("Edith", "")
                query = query_command.replace("Wikipedia inquiry for", "")
                query = query_command.replace("Wikipedia inquiry", "")
                query = query_command.replace("Wiki", "")
                query = query_command.replace("Wikipedia", "")
                web = 'https://en.wikipedia.org/wiki/' + query
                webbrowser.open(web)
        wiki()

        def off():
            query = takecommand()
            if "goodbye" or 'bye' or 'you need a break' or 'shutdown' or "that's all" in query:
                speak(choice(goodbye))
                sys.exit()        
        off()

        elif "some music" in query:
            username = [USERNAME]
            clientID = [CLIENTID]
            clientSecret = [CLIENTSECRET]
            redirectURI = [REDIRECTURI]

            oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI)
            token_dict = oauth_object.get_access_token()
            token = token_dict['access_token']
            spotifyObject = spotipy.Spotify(auth=token)

            user = spotifyObject.current_user()
            (json.dumps(user, sort_keys=True, indent=4))
            
            speak("What song would you like to play sir")
            searchQuery = takecommand()
            searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
            tracks_dict = searchResults['tracks']
            tracks_items = tracks_dict['items']
            song = tracks_items[0]['external_urls']['spotify']
            webbrowser.open(song)  
        
        elif "play" in query:
            username = USERNAME
            clientID = CLIENTID
            clientSecret = CLIENTSECRET
            redirectURI = REDIRECTURI 
            oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
            token_dict = oauth_object.get_access_token()
            token = token_dict['access_token']
            spotifyObject = spotipy.Spotify(auth=token)
            user = spotifyObject.current_user()
            print(json.dumps(user,sort_keys=True, indent=4))
            while True:
                print("Welcome, "+ user['display_name'])
                print("0 - Exit")
                print("1 - Search for a Song")
                choice = int(input("Your Choice: "))
                if choice == 1:
                    # Get the Song Name.
                    searchQuery = input("Enter Song Name: ")
                    # Search for the Song.
                    searchResults = spotifyObject.search(searchQuery,1,0,"track")
                    # Get required data from JSON response.
                    tracks_dict = searchResults['tracks']
                    tracks_items = tracks_dict['items']
                    song = tracks_items[0]['external_urls']['spotify']
                    # Open the Song in Web Browser
                    webbrowser.open(song)
                    print('Song has opened in your browser.')
                elif choice == 0:
                    break
                else:
                    print("Enter valid choice.")
        '''