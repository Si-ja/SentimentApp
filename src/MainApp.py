from functions.dependencies import Sentiment
from functions.dependencies import JSON_FUN
import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

class MainWindow(Screen):
    """Main Window of the App"""
    def get_sentence(self):
        """Get the sentence the user wants to analyse and re-save it into a json"""
        
        """Get the object for handling everything related for us to JSON"""
        json_obj = JSON_FUN()
        
        """Perform main work on reading and saving of the information"""
        data = json_obj.load_json()
        data["text"] = self.ids.sentence.text
        json_obj.save_json(data)
        
        # Also check if the input window needs to be cleared
        if data["sentence"]:
            label = self.ids.sentence
            label.text = ""
            
class InformationWindow(Screen):
    """Some information on the App"""
    pass

class SettingsWindow(Screen):
    """Possible settings a user can toggle"""    
    def checkbox_click_sentence(self, instance, value):
        """Mainly prepare the object for working with JSON objects"""
        json_obj = JSON_FUN()       
        
        """Apply conditions for updaiting the check boxes"""
        if value is True:
            sentence_set = True
            data["sentence"] = True
            json_obj.save_json(data)
        else:
            sentence_set = False
            data["sentence"] = False
            json_obj.save_json(data)
    
    def checkbox_click_sentence_get(self, instance):
        return sentence_set
    
    def checkbox_click_percentage(self, instance, value):
        """Mainly prepare the object for working with JSON objects"""
        json_obj = JSON_FUN() 
        
        """Apply conditions for updaiting the check boxes"""
        if value is True: 
            percentage_set = True
            data["percentage"] = True
            json_obj.save_json(data)
        else:
            percentage_set = False
            data["percentage"] = False
            json_obj.save_json(data)
            
    def checkbox_click_percentage_get(self, instance):
        return percentage_set
            
    def checkbox_click_input(self, instance, value):
        """Mainly prepare the object for working with JSON objects"""
        json_obj = JSON_FUN()
        
        if value is True:
            input_set = True 
            data["input"] = True
            json_obj.save_json(data)
        else:
            input_set = False
            data["input"] = False
            json_obj.save_json(data)
            
    def checkbox_click_input_get(self, instance):
        return input_set

class AnalysisWindow(Screen):
    def sentence_analysis(self):
        """Analyse the sentence and prepare the output screen"""
        
        """Mainly prepare the object for working with JSON objects"""
        json_obj = JSON_FUN()
        
        # Make all the necessary preparations
        data = json_obj.load_json()
        sent_obj = Sentiment()
        
        # Perform the analysis
        feeling, neg, neu, pos = sent_obj.analysis(str(data["text"]))
        
        # Check if the entered sentence needs to be visible:
        if data["input"]:
            label = self.ids.my_sentence
            label.text = "Sentence: {}".format(str(data["text"]))
        else:
            label = self.ids.my_sentence
            label.text = ""
            
        # Return the sentiment
        label = self.ids.my_sentiment
        label.text = str(feeling)
        
        # Check if the percentages on emotions should be written and return them
        if data["percentage"]:
            label = self.ids.my_percentage
            label.text = "Positive: {}% Neutral: {}% Negative: {}%".format(round(pos, 2), round(neu, 2), round(neg, 2))
        else:
            label = self.ids.my_percentage
            label.text = ""

class WindowManager(ScreenManager):
    """App windows' manager"""
    pass

kv = Builder.load_file("sentiment.kv")

class SentimentApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    SentimentApp().run()