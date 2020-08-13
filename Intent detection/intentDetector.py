import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import nltk
import re
from sklearn.preprocessing import OneHotEncoder
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Bidirectional, Embedding, Dropout
import speech_recognition as sr
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split


def load_dataset(filename):
  df = pd.read_csv(filename, encoding = "latin1", names = ["Sentence", "Intent"])
  print(df.head())
  intent = df["Intent"]
  unique_intent = list(set(intent))
  sentences = list(df["Sentence"])
  
  return (intent, unique_intent, sentences)

intent, unique_intent, sentences = load_dataset("Dataset.csv")
print(sentences[:5])

nltk.download("stopwords")
nltk.download("punkt")

#define stemmer
stemmer = LancasterStemmer()

def cleaning(sentences):
  words = []
  for s in sentences:
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", s)
    w = word_tokenize(clean)
    #stemming
    words.append([i.lower() for i in w])
    
  return words

cleaned_words = cleaning(sentences)
print(len(cleaned_words))
print(cleaned_words[:2])

def create_tokenizer(words, filters = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'):
  token = Tokenizer(filters = filters)
  token.fit_on_texts(words)
  return token


def max_length(words):
  return(len(max(words, key = len)))
  
word_tokenizer = create_tokenizer(cleaned_words)
vocab_size = len(word_tokenizer.word_index) + 1
max_length = max_length(cleaned_words)

print("Vocab Size = %d and Maximum length = %d" % (vocab_size, max_length))
def encoding_doc(token, words):
  return(token.texts_to_sequences(words))
  
encoded_doc = encoding_doc(word_tokenizer, cleaned_words)

def padding_doc(encoded_doc, max_length):
  return(pad_sequences(encoded_doc, maxlen = max_length, padding = "post"))

padded_doc = padding_doc(encoded_doc, max_length)

padded_doc[:5]

print("Shape of padded docs = ",padded_doc.shape)

#tokenizer with filter changed
output_tokenizer = create_tokenizer(unique_intent, filters = '!"#$%&()*+,-/:;<=>?@[\]^`{|}~')
                                    
output_tokenizer.word_index

encoded_output = encoding_doc(output_tokenizer, intent)


encoded_output = np.array(encoded_output).reshape(len(encoded_output), 1)

encoded_output.shape

def one_hot(encode):
  o = OneHotEncoder(sparse = False)
  return(o.fit_transform(encode))
  
output_one_hot = one_hot(encoded_output)


output_one_hot.shape

train_X, val_X, train_Y, val_Y = train_test_split(padded_doc, output_one_hot, shuffle = True, test_size = 0.2)


print("Shape of train_X = %s and train_Y = %s" % (train_X.shape, train_Y.shape))
print("Shape of val_X = %s and val_Y = %s" % (val_X.shape, val_Y.shape))

def create_model(vocab_size, max_length):
  model = Sequential()
  model.add(Embedding(vocab_size, 128, input_length = max_length, trainable = False))
  model.add(Bidirectional(LSTM(128)))
#   model.add(LSTM(128))
  model.add(Dense(64, activation = "relu"))
  model.add(Dropout(0.5))
  model.add(Dense(21, activation = "softmax"))
  
  return model

model = create_model(vocab_size, max_length)

model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
model.summary()


filename = 'model.h5'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

hist = model.fit(train_X, train_Y, epochs = 100, batch_size = 32, validation_data = (val_X, val_Y), callbacks = [checkpoint])

model = load_model('model.h5')

def speechToText():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            return r.recognize_google(audio)
            
        except Exception as e:
            print("Error: "+str(e))
        return "Error"
     
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

def predictions(text):
  clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
  test_word = word_tokenize(clean)
  test_word = [w.lower() for w in test_word]
  test_ls = word_tokenizer.texts_to_sequences(test_word)
  print(test_word)
  #Check for unknown words
  if [] in test_ls:
    test_ls = list(filter(None, test_ls))
    
  test_ls = np.array(test_ls).reshape(1, len(test_ls))
 
  x = padding_doc(test_ls, max_length)
  
  pred = model.predict_proba(x)
  
  
  return pred


def get_final_output(pred, classes):
  predictions = pred[0]
 
  classes = np.array(classes)
  ids = np.argsort(-predictions)
  classes = classes[ids]
  predictions = -np.sort(-predictions)
  return classes[np.argmax(predictions)]

#Testing
text = "Can you help me?"
pred = predictions(text)
get_final_output(pred, unique_intent)


#Speech Recognition

def detect_intent():
    while True:
        query = speechToText()
        pred = predictions(query)
        intent_harsh = get_final_output(pred, unique_intent)
    
        if intent_harsh == unique_intent[0]:
            speak("You can tell me everything.")
        
        elif intent_harsh == unique_intent[1]:
            speak("I will help you to register this program.")
        
        elif intent_harsh == unique_intent[2]:
            speak("I am a bot.")
        
        elif intent_harsh == unique_intent[3]:
            speak("Querry")
        
        elif intent_harsh == unique_intent[4]:
            speak(unique_intent[4][3:])
        
        elif intent_harsh == unique_intent[5]:
            speak("Borrow limit")
        
        elif intent_harsh == unique_intent[6]:
            speak("Your aadhar is missing!")
        
        elif intent_harsh == unique_intent[7]:
            speak("biz_new")
        
        elif intent_harsh == unique_intent[8]:
            speak("approval_time")
        
        elif intent_harsh == unique_intent[9]:
            speak(unique_intent[9][3:])
        
        elif intent_harsh == unique_intent[10]:
            speak(unique_intent[10][7:])
        
        elif intent_harsh == unique_intent[11]:
            speak(unique_intent[11][7:])
        
        elif intent_harsh == unique_intent[12]:
            speak(unique_intent[12][7:])
        
        elif intent_harsh == unique_intent[13]:
            speak(unique_intent[13][3:])
        
        elif intent_harsh == unique_intent[14]:
            speak(unique_intent[14][3:])
        
        elif intent_harsh == unique_intent[15]:
            speak(unique_intent[15][3:])
        
        elif intent_harsh == unique_intent[16]:
            speak(unique_intent[16][3:])
        
        elif intent_harsh == unique_intent[17]:
            speak(unique_intent[17][7:])
        
        elif intent_harsh == unique_intent[18]:
            speak(unique_intent[18][7:])
        
        elif intent_harsh == unique_intent[19]:
            speak(unique_intent[19][7:])
        
        elif intent_harsh == unique_intent[20]:
            speak(unique_intent[20][3:])
        
        else:
            speak("Jarvis: I cannot understand sir!")
            break

def main():
    detect_intent()
                   
if __name__ == "__main__":
    main()                                                                             

    
    
    
    


