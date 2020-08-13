#Importing Libraries
import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential,Model,load_model
from keras.layers import Conv2D,MaxPool2D,Dense,GlobalMaxPool2D,Dropout
import glob
from memory_profiler import memory_usage
import gc

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
  

#Finding all files in a directory.
train_list=[]
path = './content/train_data_wav/LibriSpeech/train-clean-100/'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.flac' in file:
            files.append(os.path.join(r, file))
for f in files:
    train_list.append(f)



#Finding all files in a directory.
test_list=[]
path = './content/test_data_wav/LibriSpeech/test-clean/'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.flac' in file:
            files.append(os.path.join(r, file))
for f in files:
    test_list.append(f)

#Creating spectrograms and storing to their respective directory.

#Train_data
for filepath in train_list:
  filename=filepath.split('/')[-1].split('.')[0]
  filename = filename.split('\\')[-1]
  create_spectrogram(filepath,'./content/train_images/'+filename+'.jpg')
gc.collect()

#Test data
for filepath in test_list:
  filename=filepath.split('/')[-1].split('.')[0]
  filename = filename.split('\\')[-1]
  create_spectrogram(filepath,'./content/test_images/'+filename+'.jpg')
gc.collect()

#Building the batch generator.
import cv2
def load_img(path):
  img=cv2.imread(path)
  img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  img=cv2.resize(img,(150,150))
  return img

def generate_idxs(X):
    idxs1=np.random.randint(0,len(X),1)[0]
    return idxs1

def same_label_index(X):

  while True:
    idx1=generate_idxs(X)
    idx2=generate_idxs(X)
    file1_dir=X[idx1]
    file2_dir=X[idx2]
    lb1=file1_dir.split("/")[-1].split("-")[0]
    lb2=file2_dir.split("/")[-1].split("-")[0]
    if lb1==lb2:
      break

  return idx1,idx2

def different_label_index(X):
  while True:
    idx1=generate_idxs(X)
    idx2=generate_idxs(X)
    file1_dir=X[idx1]
    file2_dir=X[idx2]
    lb1=file1_dir.split("/")[-1].split("-")[0]
    lb2=file2_dir.split("/")[-1].split("-")[0]
    if lb1!=lb2:
      break

  return idx1,idx2

def batch_generator(X,batch_size):
  while True:
    data=[np.zeros((batch_size,150,150,3)) for i in range(2)]
    tar=[np.zeros(batch_size,)]

    #Generating same pairs.
    for i in range(0,batch_size//2):
      idx1,idx2=same_label_index(X)
      img1=load_img(X[idx1])
      img1=img1/255
      img2=load_img(X[idx2])
      img2=img2/255

      data[0][i,:,:,:]=img1
      data[1][i,:,:,:]=img2
      tar[0][i]=1

    #Generating different pairs.
    for k in range(batch_size//2,batch_size):
      idx1,idx2=different_label_index(X)
      img1=load_img(X[idx1])
      img1=img1/255
      img2=load_img(X[idx2])
      img2=img2/255

      data[0][k,:,:,:]=img1
      data[1][k,:,:,:]=img2
      tar[0][k]=0
    np.delete(data[0],np.where(~data[0].any(axis=1))[0], axis=0)
    np.delete(data[1],np.where(~data[1].any(axis=1))[0], axis=0)
    yield data,tar
    

%matplotlib inline
img_test=cv2.imread('./content/train_images/587-54108-0035.jpg')
img_test=cv2.cvtColor(img_test,cv2.COLOR_BGR2RGB)
plt.imshow(img_test)


#Getting training images_list.
X_train=[]
temp_file_list_= os.listdir('./content/train_images/')
for filename in temp_file_list_:
  X_train.append(str('./content/train_images/'+filename))
  
#Getting test images_list.
X_test=[]
temp_file_list_= os.listdir('./content/test_images/')
for filename in temp_file_list_:
  X_test.append(str('./content/test_images/'+filename))
  

#Build the model
from keras.layers import Lambda,Input
import keras.backend as K
from keras.callbacks import ModelCheckpoint,EarlyStopping

def cosine_distance(vests):
    x, y = vests
    x = K.l2_normalize(x, axis=-1)
    y = K.l2_normalize(y, axis=-1)
    return -K.mean(x * y, axis=-1, keepdims=True)

def get_encoder(input_size):
  model=Sequential()
  model.add(Conv2D(32,(3,3),input_shape=(150,150,3),activation='relu'))
  model.add(Conv2D(64,(3,3),activation='relu'))
  model.add(MaxPool2D(2,2))
  model.add(Dropout(0.2))

  model.add(Conv2D(64,(3,3),activation='relu'))
  model.add(Conv2D(64,(3,3),activation='relu'))
  model.add(MaxPool2D(2,2))
  model.add(Dropout(0.2))

  model.add(Conv2D(128,(3,3),activation='relu'))
  model.add(Conv2D(128,(3,3),activation='relu'))
  model.add(MaxPool2D(2,2))
  model.add(Dropout(0.2))

  model.add(GlobalMaxPool2D())

  return model

def get_siamese_network(encoder,input_size):
  input1=Input(input_size)
  input2=Input(input_size)

  encoder_l=encoder(input1)
  encoder_r=encoder(input2)
  
  L1_layer = Lambda(lambda tensors:K.abs(tensors[0] - tensors[1]))
  L1_distance = L1_layer([encoder_l, encoder_r])

  output=Dense(1,activation='sigmoid')(L1_distance)
  siam_model=Model(inputs=[input1,input2],outputs=output)
  return siam_model

encoder=get_encoder((150,150,3))
siamese_net=get_siamese_network(encoder,(150,150,3))
siamese_net.compile(loss='binary_crossentropy',optimizer='adam')

#Training the model on training data
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10, min_delta=0.0001) 
mc = ModelCheckpoint('SpeakerID_best.hdf5', monitor='val_loss', verbose=1, save_best_only=True, mode='min')
history=siamese_net.fit_generator(batch_generator(X_train,10),steps_per_epoch=150,epochs=50,validation_data=batch_generator(X_test,10),
                            validation_steps=20,callbacks=[es,mc],shuffle=True)





#(Sainity testing)
#Same pair test.
idx1,idx2=same_label_index(X_test)
X1=[np.zeros((1,150,150,3)) for i in range(2)]

img1=load_img(X_test[idx1])
img1=np.array(img1)
img1=img1/255
img2=load_img(X_test[idx2])
img2=np.array(img2)
img2=img2/255

X1[0][0,:,:,:]=img1
X1[1][0,:,:,:]=img2

#Different pair.
idx1,idx2=different_label_index(X_test)
X2=[np.zeros((1,150,150,3)) for i in range(2)]

img1=load_img(X_test[idx1])
img1=np.array(img1)
img1=img1/255
img2=load_img(X_test[idx2])
img2=np.array(img2)
img2=img2/255


X2[0][0,:,:,:]=img1
X2[1][0,:,:,:]=img2

model=load_model('./SpeakerID_best.hdf5')
print(model.predict(X1))
print(model.predict(X2))
