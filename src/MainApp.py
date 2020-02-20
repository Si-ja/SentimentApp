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

# Conditions for the settings menu (not bad, not terrible)
global prediction_set
global percentage_set
global input_set
global data

# Read the json file with settings and decide how the application needs to start
json_data = "settings.json"
with open('settings.json') as json_file:
    data = json.load(json_file)
prediction_set = data["prediction"]
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
    pass

class InformationWindow(Screen):
    """Some information on the App"""
    pass

class SettingsWindow(Screen):
    """Possible Settings a user can toggle"""    
    def checkbox_click_prediction(self, instance, value):
        if value is True:
            prediction_set = True
            data["prediction"] = True
            save_json()
        else:
            prediction_set = False
            data["prediction"] = False
            save_json()
    
    def checkbox_click_prediction_get(self, instance):
        return prediction_set
    
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
    def verify(self):
        with open('settings.json') as json_file:
            data = json.load(json_file)
        prediction_set = data["prediction"]
        return prediction_set

class WindowManager(ScreenManager):
    """App windows' manager"""
    pass

kv = Builder.load_file("sentiment.kv")

class SentimentApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    SentimentApp().run()
