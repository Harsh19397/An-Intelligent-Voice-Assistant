# An-Intelligent-Voice-Assistant
An Intelligent voice assistant is an application that can understand voice commands and completes the task for user. Some of the examples of this application are Alexa, Siri and Google Assistant. Here, I have build a prototype of the same appplication with some functionalities which can be extended by anyone according to their needs. It takes user's voice as input, process them and performs actions based on it. It uses state of art process in Speech to Text, Natural language understanding, deep learning and Text to Speech. I have created 5 different modules for this prototype which are integrated together to make this prototype a successful one. These 4 modules are responsible for handling all the key functinalities. These modules are:
  1.  Deep Speaker - Responsible for recognising the speakers voice.
  2.  Intent Detection - Responsible for detecting the intent of the user.
  3.  Trigger word detection - Responsible for detecting the trigger when the user speaks the hot word.
  4.  Speech to Text - Responsible for recognising the voice commands of the user.
  5.  Text to Speech - Responsible for converting the text to speech to interact with the user.

## Deep Speaker
Deep speaker module is responsible for recognising the speakers voice. I have leveraged Siamese neural network used for one short learning to predict the user's identity. The user is asked to speak out the activation keyword that he wants to set for his assistant's activation, which is then recorded and saved as .wav file. This recording is then converted into a spectogram and saved as an image in the database. When the same user tries to activate the assistant with his voice, his audio signal is then again converted to a spectogram which is then fed to the siamese network which outputs the similarity score of the audio signal with the one already stored in the database. If the similarity score is high, the voices match and we can identify the speaker. This is one of the key module used for identifying the speaker's voice and its applications are vast. We can even set voice locks as well without really requiring hours of audio data from the user.

