#Importing Libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import gc
import Speaker_Identification_utils as si
import cv2
from keras.callbacks import ModelCheckpoint,EarlyStopping
import model_NN as mn

#Finding all files in a directory.
train_list=[]
path = './content/train_data_wav/LibriSpeech/train-clean-100/'
train_list = si.finding_files_in_directory(train_list, path)

#Finding all files in a directory.
test_list=[]
path = './content/test_data_wav/LibriSpeech/test-clean/'
test_list = si.finding_files_in_directory(test_list, path)

if os.path.isdir('.content/train_images') and os.path.isdir('.content/test_images') == False:
    #Creating spectrograms and storing to their respective directory.
    #Train_data
    si.storing_img_data(train_list)
    gc.collect()
    
    #Test data
    si.storing_img_data(test_list)
    gc.collect()

    
#Testing the image
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
  

def batch_generator(X,batch_size):
  while True:
    data=[np.zeros((batch_size,150,150,3)) for i in range(2)]
    tar=[np.zeros(batch_size,)]

    #Generating same pairs.
    for i in range(0,batch_size//2):
      idx1,idx2=si.same_label_index(X)
      img1=si.load_img(X[idx1])
      img1=img1/255
      img2=si.load_img(X[idx2])
      img2=img2/255

      data[0][i,:,:,:]=img1
      data[1][i,:,:,:]=img2
      tar[0][i]=1

    #Generating different pairs.
    for k in range(batch_size//2,batch_size):
      idx1,idx2=si.different_label_index(X)
      img1=si.load_img(X[idx1])
      img1=img1/255
      img2=si.load_img(X[idx2])
      img2=img2/255

      data[0][k,:,:,:]=img1
      data[1][k,:,:,:]=img2
      tar[0][k]=0
    np.delete(data[0],np.where(~data[0].any(axis=1))[0], axis=0)
    np.delete(data[1],np.where(~data[1].any(axis=1))[0], axis=0)
    yield data,tar
    
if os.path.isfile('SpeakerID_best.hdf5') == False:
    #Build the model
    encoder=mn.get_encoder((150,150,3))
    siamese_net=mn.get_siamese_network(encoder,(150,150,3))
    siamese_net.compile(loss='binary_crossentropy',optimizer='adam')
    
    #Training the model on training data
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10, min_delta=0.0001) 
    mc = ModelCheckpoint('SpeakerID_best.hdf5', monitor='val_loss', verbose=1, save_best_only=True, mode='min')
    history=siamese_net.fit_generator(batch_generator(X_train,10),steps_per_epoch=150,epochs=50,validation_data=batch_generator(X_test,10),
                                validation_steps=20,callbacks=[es,mc],shuffle=True)
