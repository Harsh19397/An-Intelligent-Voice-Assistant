#Importing bunch of libraries.
import librosa
import cv2
import os
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import pyaudio
import wave
import Speaker_Identification_utils as si

model=load_model('SpeakerID_best.hdf5')
count = 5

def record_audio():
    filename = "recorded" + str(count) + ".wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = 5
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()

#Converts the audio into spectrogram.
  
#This loop takes each file and converts them into spectrogram and save them as jpeg image.
#replace the below list with actual audios
files_list=['1034-121119-0000.flac','1040-133433-0007.flac','1040-133433-0004.flac','Sudhashu2.flac','Vik2.flac','Vik.flac','Sudhanshu.flac','Vik3.flac']
for i in range(len(files_list)):
    filepath='Test_audio_files/'+files_list[i]
    new_name=files_list[i].split('.')[0]
    savepath='Generated_images/'+new_name+'.jpg'
    si.create_spectrogram(filepath,savepath)
    
#This part contains the list of all file names and a function which compares them with the supplied input.
#Call from DB
all_files_list=["recorded1.jpg", "recorded2.jpg", "recorded3.jpg", "recorded4.jpg", "recorded5.jpg"]

def match_file(filename):
    score_list=[]
    img1=si.load_img('Generated_images/'+filename)
    img1=img1/255
    for i in range(len(all_files_list)):
        
        img2=si.load_img('Generated_images/'+all_files_list[i])
        img2=img2/255
        X=[np.zeros((1,150,150,3)) for i in range(2)]
        Y=[np.zeros(1,)]
        X[0][0,:,:,:]=img1
        X[1][0,:,:,:]=img2
        score_list.append(model.predict(X))
    score_list=np.array(score_list)
    idx=np.argmax(score_list)
    return all_files_list[idx],score_list

name,score=match_file('recorded.jpg')

print(name)

