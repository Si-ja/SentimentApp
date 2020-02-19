from functions.dependencies import Sentiment
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox

# Conditions for the settings menu
global prediction_set
global percentage_set
global input_set
prediction_set, percentage_set, input_set = True, False, True


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
        else:
            prediction_set = False
            
    def checkbox_click_prediction_get(self, instance):
        return prediction_set
    
    def checkbox_click_percentage(self, instance, value):
        if value is True:
            percentage_set = True
        else:
            percentage_set = False
            
    def checkbox_click_percentage_get(self, instance):
        return percentage_set
            
    def checkbox_click_input(self, instance, value):
        if value is True:
            input_set = True 
        else:
            input_set = False
            
    def checkbox_click_input_get(self, instance):
        return input_set

class AnalysisWindow(Screen):
    """Actual sentence Analysis window"""
    pass

class WindowManager(ScreenManager):
    """App windows' manager"""
    pass

kv = Builder.load_file("sentiment.kv")

class SentimentApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    SentimentApp().run()
