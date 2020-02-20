from functions.dependencies import Sentiment
from functions.dependencies import Support
import json
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

# Conditions for the settings menu (not bad, not terrible)
global sentence_set
global percentage_set
global input_set
global data

global sentence_get
sentence_get = ""

# Read the json file with settings and decide how the application needs to start
json_data = "settings.json"
with open('settings.json') as json_file:
    data = json.load(json_file)
sentence_set = data["sentence"]
percentage_set = data["percentage"]
input_set = data["input"]

#help = Support
#help.packages()

def save_json(data = data):
    """Save to a json file the whole data"""
    with open('settings.json', 'w') as json_file:
        json.dump(data, json_file)

class MainWindow(Screen):
    """Main Window of the App"""
    def get_sentence(self):
        """Get the sentence the user wants to analyse"""
        data["text"] = self.ids.sentence.text
        save_json()
        
        # Also check if the input window needs to be cleared
        if data["sentence"]:
            label = self.ids.sentence
            label.text = ""
            
        # Here analysis needs to be performed
        pass
            
        
          
class InformationWindow(Screen):
    """Some information on the App"""
    pass

class SettingsWindow(Screen):
    """Possible Settings a user can toggle"""    
    def checkbox_click_sentence(self, instance, value):
        if value is True:
            sentence_set = True
            data["sentence"] = True
            save_json()
        else:
            sentence_set = False
            data["sentence"] = False
            save_json()
    
    def checkbox_click_sentence_get(self, instance):
        return sentence_set
    
    def checkbox_click_percentage(self, instance, value):
        if value is True:
            percentage_set = True
            data["percentage"] = True
            save_json()
        else:
            percentage_set = False
            data["percentage"] = False
            save_json()
            
    def checkbox_click_percentage_get(self, instance):
        return percentage_set
            
    def checkbox_click_input(self, instance, value):
        if value is True:
            input_set = True 
            data["input"] = True
            save_json()
        else:
            input_set = False
            data["input"] = False
            save_json()
            
    def checkbox_click_input_get(self, instance):
        return input_set

class AnalysisWindow(Screen):
    """Actual sentence Analysis window"""
    def sentence_analysis(self):
        pass
        #Get the sentence:
        #sentence = self.root.ids.sentence.text
        #print(sentence)

    def verify(self):
        # Check the conditions user has set to work with by loading them
        with open('settings.json') as json_file:
            data = json.load(json_file)
    
        # Check if the sentence needs to be entered:
            if data["input"]:
                label = self.ids.my_sentence
                label.text = "Sentence: {}".format(str(data["text"]))
            else:
                label = self.ids.my_sentence
                label.text = ""
        
        
        
        
        
        

        
        
        
        percentage_set = data["sentence"]
        
        
        
        return

class WindowManager(ScreenManager):
    """App windows' manager"""
    pass

kv = Builder.load_file("sentiment.kv")

class SentimentApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    SentimentApp().run()
