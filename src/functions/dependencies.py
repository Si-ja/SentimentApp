class Support:
    '''Class responsible for assistance methods to the project'''
    def packages():
        try:
            import nltk
            print(">You have an nltk package installed under {} version.".format(nltk.__version__))
            if nltk.__version__ != "3.4.5":
                print("\t>>It is recommended to switch to the 3.4.5 version, as under it the original build took place.")
        except:
            print(">You are missing an nltk package.")
    
        try:
            import kivy
            print(">You have a kivy package installed under {} version.".format(kivy.__version__))
            if kivy.__version__ != "1.11.1":
                print("\t>>It is recommended to switch to the 1.11.1 version, as under it the original build took place.")
        except:
            print(">You are missing a kivy package.")
            
        try:
            import json
            print(">You have a json package installed under {} version.".format(json.__version__))
        except:
            print(">You are missing a json package.")
            
class Sentiment:
    '''Class responsible for performing of the sentiment analysis'''
    def __init__(self):
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        self.sent_obj = SentimentIntensityAnalyzer()
    
    def analysis(self, text = ""):
        """Actuall perform the analysis of the text"""
        sentiment_dict = self.sent_obj.polarity_scores(text)
        
        #Assess the information from the input
        feeling = None
        if sentiment_dict['compound'] >= 0.05 :
            feeling = "I sense POSITIVE vibes!"
        elif sentiment_dict['compound'] <= - 0.05 : 
            feeling = "I get a sense of somberness..."
        else: 
            feeling = "I assume you are being very neutral."
        
        feeling_neg = sentiment_dict["neg"]*100
        feeling_neu = sentiment_dict["neu"]*100
        feeling_pos = sentiment_dict["pos"]*100
        
        return str(feeling), feeling_neg, feeling_neu, feeling_pos
    
class JSON_FUN:
    """Class that helps to work with JSON files further on"""
    def __init__(self):
        pass
    
    def load_json(self):
        """Load the information from the only json file we have"""
        import json
        with open('settings.json') as json_file:
            data = json.load(json_file)
        return data
    
    def save_json(self, data):
        import json
        """Save to a json file the whole data"""
        with open('settings.json', 'w') as json_file:
            json.dump(data, json_file)