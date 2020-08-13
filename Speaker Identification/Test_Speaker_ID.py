#Importing bunch of libraries.
import librosa
import cv2
import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import pyaudio
import wave

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
def create_spectrogram(filepath,save_path):
  plt.interactive(False)
  clip,sample_rate=librosa.load(filepath,sr=None)
  fig=plt.figure(figsize=[0.72,0.72])
  ax=fig.add_subplot(111)
  ax.axes.get_xaxis().set_visible(False)
  ax.axes.get_yaxis().set_visible(False)
  ax.set_frame_on(False)
  S=librosa.feature.melspectrogram(y=clip,sr=sample_rate)
  librosa.display.specshow(librosa.power_to_db(S,ref=np.max))
  fig.savefig(save_path,dpi=400,bbox_inches='tight',pad_inches=0)
  plt.close()
  fig.clf()
  plt.close(fig)
  plt.close('all')
  del filepath,save_path,clip,sample_rate,fig,ax,S
  
  
def load_img(path):
  img=cv2.imread(path)
  img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  img=cv2.resize(img,(150,150))
  return img

#This loop takes each file and converts them into spectrogram and save them as jpeg image.

files_list=['1034-121119-0000.flac','1040-133433-0007.flac','1040-133433-0004.flac','Sudhashu2.flac','Vik2.flac','Vik.flac','Sudhanshu.flac','Vik3.flac']
for i in range(len(files_list)):
    filepath='Test_audio_files/'+files_list[i]
    new_name=files_list[i].split('.')[0]
    savepath='Generated_images/'+new_name+'.jpg'
    create_spectrogram(filepath,savepath)
    
#This part contains the list of all file names and a function which compares them with the supplied input.
#Call from DB
all_files_list=["recorded1.jpg", "recorded2.jpg", "recorded3.jpg", "recorded4.jpg", "recorded5.jpg"]

def match_file(filename):
    score_list=[]
    img1=load_img('Generated_images/'+filename)
    img1=img1/255
    for i in range(len(all_files_list)):
        
        img2=load_img('Generated_images/'+all_files_list[i])
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

