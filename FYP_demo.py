#import the main app class
from kivy.app import App
#import the classes to build UI
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
#import diy function
from test_python import random_python_test
#import web for simulating social media launch (doesn't work from WSL2)
import webbrowser
#import os to call windows powershell to open URL (rediculous, but it works)
import os
#import sound player
from kivy.core.audio import SoundLoader

#screen manager too confusing right now - I'll just add, remove widgets for now
#using kv file for refactoring is too confusing right now - not enough time

#Instantiate class layout with buttons
class AppLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        #Something about inheritance and OOP (later in my bootdev back-end course path)

        self.orientation = "vertical"



        self.exit_button = Button(text="Exit", size_hint=(1, 0.05))
        self.exit_button.bind(on_press=self.exit_app)
        self.add_widget(self.exit_button)

        self.FYP_image = Image(source="FYP Splash.jpg", size_hint=(1, 0.75))
        self.add_widget(self.FYP_image)

        self.ss_button = Button(text="Welcome!", size_hint=(1, 0.25))
        self.ss_button.bind(on_press=self.page_test)
        self.ss_button.bind(on_press=self.play_sound)
        self.add_widget(self.ss_button)

    #add sounds to buttons (hopefully)
    def play_sound(self, button):
        sound = SoundLoader.load("bop pop bap sound.m4a")
        if sound:
            sound.play()

    #don't remove exit button
    def exit_app(self, exit_button):
        App.get_running_app().stop()

    def page_test(self, ss_button):
        self.remove_widget(self.ss_button)
        self.remove_widget(self.FYP_image)

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

        self.Option1.bind(on_press=self.page_select_social)
        self.Option1.bind(on_press=self.play_sound)

        self.add_widget(self.Option1)
        self.add_widget(self.Option2)
        self.add_widget(self.Option3)
        self.add_widget(self.Option4)

    def page_select_social(self, Option1):
        self.remove_widget(self.Q)
        self.remove_widget(Option1)
        self.remove_widget(self.Option2)
        self.remove_widget(self.Option3)
        self.remove_widget(self.Option4)

        #assign buttons to variables and "self?" and set the text
        #the "self" gets added to the Boxlayout?
        #the BoxLayout gets added to main app build method via __init__ constructor?
        self.Button1 = Button(text="Youtube", size_hint=(1,0.3))
        self.Button2 = Button(text="Instagram", size_hint=(1,0.3))
        self.Button3 = Button(text="Facebook", size_hint=(1,0.3))

        #bind buttons to function
        self.Button1.bind(on_press=self.launch_youtube) #test with new_label function
        #if it was "new_label()" the function would get called immediately.
        #new_label must not get called until button gets pressed
        self.Button2.bind(on_press=self.launch_instagram)
        self.Button3.bind(on_press=self.launch_facebook)

        #add the buttons to the layout
        self.add_widget(self.Button1)
        self.add_widget(self.Button2)
        self.add_widget(self.Button3)

    def launch_youtube(self, Button1):
        os.system("powershell.exe start https://www.youtube.com")
        App.get_running_app().stop()

    def launch_instagram(self, Button2):
        os.system("powershell.exe start https://instagram.com")
        App.get_running_app().stop()

    def launch_facebook(self, Button3):
        os.system("powershell.exe start https://facebook.com")
        App.get_running_app().stop()

#too complicated for now
    # def launch_social(self, Button1):
    #     list_social = [Button1.lower()]
    #     webbrowser.open(f"https://{list_social}.com")
        

#test button 1 with add_widget function
    # def new_label(self, Button1):
    #     #make label
    #     self.label1 = Label(text=str(random_python_test()))
    #     #add label to layout
    #     self.add_widget(self.label1)
    #     #remove button that was pressed via argument (thus no "self" needed)
    #     self.remove_widget(Button1)
    #     #I want to remove the other buttons too so I'll have to use "self."
    #     #(yeah, I know it's sub-optimal at best, but just gotta make it work for now, alright)
    #     self.remove_widget(self.Button2)
    #     self.remove_widget(self.Button3)

#instantiate the main app class
class FYP(App):
    def build(self):
    #defines the function to build the layout with all the buttons etc.?
    #when does it get called tho...
        return AppLayout()


#run the app
if __name__ == '__main__':
    FYP().run()