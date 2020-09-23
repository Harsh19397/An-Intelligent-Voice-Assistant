# An-Intelligent-Voice-Assistant
An Intelligent voice assistant is an application that can understand voice commands and completes the task for user. Some of the examples of this application are Alexa, Siri and Google Assistant. Here, I have build a prototype of the same appplication with some functionalities which can be extended by anyone according to their needs. It takes user's voice as input, process them and performs actions based on it. It uses state of art process in Speech to Text, Natural language understanding, deep learning and Text to Speech. I have created 5 different modules for this prototype which are integrated together to make this prototype a successful one. These 4 modules are responsible for handling all the key functinalities. These modules are:
  1.  Deep Speaker - Responsible for recognising the speakers voice.
  2.  Intent Detection - Responsible for detecting the intent of the user.
  3.  Trigger word detection - Responsible for detecting the trigger when the user speaks the hot word.
  4.  Speech to Text - Responsible for recognising the voice commands of the user.
  5.  Text to Speech - Responsible for converting the text to speech to interact with the user.

## Deep Speaker
Deep speaker module is responsible for recognising the speakers voice. I have leveraged Siamese neural network used for one short learning to predict the user's identity. The user is asked to speak out the activation keyword that he wants to set for his assistant's activation, which is then recorded and saved as .wav file. This recording is then converted into a spectogram and saved as an image in the database. When the same user tries to activate the assistant with his voice, his audio signal is then again converted to a spectogram which is then fed to the siamese network which outputs the similarity score of the audio signal with the one already stored in the database. If the similarity score is high, the voices match and we can identify the speaker. This is one of the key module used for identifying the speaker's voice and its applications are vast. We can even set voice locks as well without really requiring hours of audio data from the user.

## Intent Detection
Intent detection module deals with the intent of the user. A user can make a request for a task in several ways in English language. Hence it won’t be a wise decision to decide to hardcode the vocab used by a user to get some task completed. In order to deal with this problem, a neural network has been trained on a dataset of some user commands. This neural network will predict the intent of the user no matter what way the user uses to command the assistant for a specific task. For future scope and to make the intent detection even more successful a check can be made whenever a user says a new command which is not stored in the database but the neural network predicts the intent mapped across it, that command can be automatically added to the database. Further the neural network can be trained on a regular interval to achieve a higher accuracy for intent detection.

## Trigger Word detection
Trigger word detection module is responsible for activating the assistant only when the user speaks the activation word that has been assigned for that specific user. Coupling this trigger word detection module with the deep speaker module gives us the power to activate the assistant only when the logged in user speaks that activation word and not by anyone else. This functionality makes the assistant more secure and cannot be used by any unauthorized user to access the data of the authorized user. Google speech to text api is used, which translates the user’s voice commands into the text which is then compared with the activation word stored in the database for the active user. Once those two matches, assistant activates and is ready to take commands by the user to perform all the tasks assigned.

## Speech to Text
Speech to text module is responsible for translating the human speech to text form. Here in this project the free speech to text API provided by Google is being used as it has very high accuracy and this functionality requires very high accuracy as if this doesn’t happen the entire user experience becomes bad. 

## Text to Speech
Text to Speech module is responsible for translating text to speech. Here in this project the free text to speech API provided by Google is being used as it has very high accuracy and this functionality requires very high accuracy, as if this doesn’t happen the entire user experience gets bad. 

## How to use this project
User guide of this intelligent voice assistant prototype can be divided into 4 sections which are namely:
1.	Cloning this GitHub repository
2.	Installing the dependencies
3.	Training the model / Use the existing trained model stored in .h5 format
4.	Running the main.h5 file to have all the fun

In order to use the below steps make sure that python 3.7 has been installed on your system and python has been added to the environment variable.

### Cloning this GitHub Repository
Clone this github repository by running "git clone https://github.com/Harsh19397/An-Intelligent-Voice-Assistant.git"

### Installing the dependancies
To be updated.

### Training the model (optional)
1. Training the Deep Speaker model by running the command "python Deep_Speaker/conv_models.py"
2. Training the Intent Detection model  by running the command "python Intent_detection/intentDetection.py"

### Use the assistant to have fun
Run the command "python main.py"

