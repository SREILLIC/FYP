#import kivy packages (API's?)
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

#import media loaders
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image

#import quiz bank
from python_quiz import random_python_test

#import python revision bank
from python_examples import get_py_rev

#for running code on appropriate platform
from kivy.utils import platform

#os for general testing of code in WSL2, using windows powershell
import os

#import java class to launch android app through python
from jnius import autoclass

###############################################################################################################

#global functions
def exit_app(exit_button):
    App.get_running_app().stop()

#define app launching by getting java packages
def launch_app(package_name):
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    PackageManager = autoclass('android.content.pm.PackageManager')

    activity = PythonActivity.mActivity #deef
    pm = activity.getPackageManager() #deef
    intent = pm.getLaunchIntentForPackage(package_name) #fed

    if intent:
        activity.startActivity(intent)
    else:
        print(f"App {package_name} not found.")

#make class to define sound/image/video
#can I define these things without adding class?
def sound_splash():
    if platform == "android":
        sound = SoundLoader.load("bop_pop_bap_sound.WAV")
        sound.play()
    else:
        print("Sound only works on android")

def sound_correct():
    #play camera flash
    if platform == "android":
        sound = SoundLoader.load("camera_flash.mp3")
        sound.play()
    else:
        print("Sound only works on android")

##############################################################################################################

#make class for screens
#define each screen  (add widgets)
class SplashPage(BoxLayout):
    #construct it
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"

        self.exit_button = Button(text="Exit", size_hint=(1, 0.05))
        self.exit_button.bind(on_press=exit_app)
        self.add_widget(self.exit_button)

        self.FYP_image = Image(source="FYP_Splash.jpg", size_hint=(1, 0.75))
        self.add_widget(self.FYP_image)

        self.welcome = Button(text="Welcome!", size_hint=(1, 0.25))
        self.welcome.bind(on_press=self.switch)
        self.add_widget(self.welcome)

        sound_splash()

    def switch(self, item):
        sound_correct()
        fyp.screen_manager.transition = SlideTransition(direction="left")
        fyp.screen_manager.current = "QuizPage"

#classes for each page
class QuizPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"

        self.exit_button = Button(text="Exit", size_hint=(1, 0.05))
        self.exit_button.bind(on_press=exit_app)
        self.add_widget(self.exit_button)

        dict_test = random_python_test()
        Q = dict_test["Q"]
        self.Q = Label(text=Q, size_hint=(1,0.2))
        self.add_widget(self.Q)

        Option1 = dict_test["Option 1"]
        Option2 = dict_test["Option 2"]
        Option3 = dict_test["Option 3"]
        Option4 = dict_test["Option 4"]

        self.Option1 = Button(text=Option1, size_hint=(1,0.2))
        self.Option2 = Button(text=Option2, size_hint=(1,0.2))
        self.Option3 = Button(text=Option3, size_hint=(1,0.2))
        self.Option4 = Button(text=Option4, size_hint=(1,0.2))

        self.Option1.bind(on_press=self.switch) #hardcoded for now

        self.add_widget(self.Option1)
        self.add_widget(self.Option2)
        self.add_widget(self.Option3)
        self.add_widget(self.Option4)


    def switch(self, item):
        sound_correct()
        fyp.screen_manager.transition = SlideTransition(direction="left")
        fyp.screen_manager.current = "PythonRevisionPage"

class PythonRevisionPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"

        self.exit_button = Button(text="Exit", size_hint=(1, 0.05))
        self.exit_button.bind(on_press=exit_app)
        self.add_widget(self.exit_button)

        self.revision_lbl = Label(text="Revision Page", size_hint=(1, 0.1))
        self.add_widget(self.revision_lbl)

        #call get_py_rev() function
        rev_list_six = get_py_rev()

        for i in rev_list_six:
            example = Label(text=i, size_hint=(1, 0.3))
            self.add_widget(example)

        self.onwards_b = Button(text="Onwards!", size_hint=(1, 0.1))
        self.onwards_b.bind(on_press=self.switch)
        self.add_widget(self.onwards_b)

    def switch(self, item):
        sound_correct()
        fyp.screen_manager.transition = SlideTransition(direction="left")
        fyp.screen_manager.current = "SocialPage"

class SocialPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"

        self.exit_button = Button(text="Exit", size_hint=(1, 0.05))
        self.exit_button.bind(on_press=exit_app)
        self.add_widget(self.exit_button)

        #assign buttons to variables and "self?" and set the text
        #the "self" gets added to the Boxlayout?
        #the BoxLayout gets added to main app build method via __init__ constructor?
        self.Button1 = Button(text="Youtube", size_hint=(1,0.3))
        self.Button2 = Button(text="Instagram", size_hint=(1,0.3))
        self.Button3 = Button(text="TikTok", size_hint=(1,0.3))

        #bind buttons to function
        self.Button1.bind(on_press=self.launch_youtube) #test with new_label function
        #if it was "new_label()" the function would get called immediately.
        #new_label must not get called until button gets pressed
        self.Button2.bind(on_press=self.launch_instagram)
        self.Button3.bind(on_press=self.launch_tiktok)

        #add the buttons to the layout
        self.add_widget(self.Button1)
        self.add_widget(self.Button2)
        self.add_widget(self.Button3)

    def launch_youtube(self, Button1):
        if platform == "android":
            launch_app("com.google.android.youtube")
        else:
            print("App launch only works on android")
            os.system("powershell.exe start https://www.youtube.com")
            App.get_running_app().stop()

    def launch_instagram(self, Button1):
        if platform == "android":
            launch_app("com.instagram.android")
        else:
            print("Only works on android")

    def launch_tiktok(self, Button1):
        if platform == "android":
            launch_app("com.zhiliaoapp.musically")
        else:
            print("Only works on android")

    def switch(self, item):
        exit_app()

###############################################################################################################

#make main class
class FYP(App):
    #construct main class
    def build(self):
        #don't remove exit button

        #make screen manager
        self.screen_manager = ScreenManager()

        #make screen page
        self.splash_page = SplashPage()
        #name it
        screen = Screen(name="SplashPage")
        #add it to the screen manager
        screen.add_widget(self.splash_page)
        #add screen manager to the app display screen
        self.screen_manager.add_widget(screen)

        #repeat above for other quiz page
        self.quiz_page = QuizPage()
        screen = Screen(name="QuizPage")
        screen.add_widget(self.quiz_page)
        self.screen_manager.add_widget(screen)

        #add social page
        self.social_page = SocialPage()
        screen = Screen(name="SocialPage")
        screen.add_widget(self.social_page)
        self.screen_manager.add_widget(screen)

        #add python revision page
        self.py_rev_page = PythonRevisionPage()
        screen = Screen(name="PythonRevisionPage")
        screen.add_widget(self.py_rev_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

#run main class
fyp = FYP()
fyp.run()