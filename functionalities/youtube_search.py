import webbrowser
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def youtube_search(text):
    url ='https://www.youtube.com/results?search_query='
    text = text.lower()
    
    #Cleaning the text
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
    clean = re.sub(r'youtube', "", clean)
    clean = re.sub(r'search', "", clean)
    word_tokens = word_tokenize(clean)
    
    #Removing the stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    
    #Getting the URL ready
    uri = ""
    for x in filtered_sentence:
        uri = uri + x + " "
    for x in uri.split():
        url += x + '+'  
    url = url[:-1]
    
    #Openning up youtube in the chrome browser 
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome"))
    webbrowser.get('chrome').open(url)
    
    

        