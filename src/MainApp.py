from functions.dependencies import Sentiment
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

class MainWindow(Screen):
    """Main Window of the App"""
    pass

class InformationWindow(Screen):
    """Some information on the App"""
    pass

class SettingsWindow(Screen):
    """Possible Settings a user can toggle"""
    pass

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
