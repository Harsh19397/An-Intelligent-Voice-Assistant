import numpy as np
import Speaker_Identification_utils as si
from keras.models import load_model
import os

X_test=[]
temp_file_list_= os.listdir('./content/test_images/')
for filename in temp_file_list_:
  X_test.append(str('./content/test_images/'+filename))

#(Sainity testing)
#Same pair test.
idx1,idx2 = si.same_label_index(X_test)
X1=[np.zeros((1,150,150,3)) for i in range(2)]

img1 = si.load_img(X_test[idx1])
img1 = np.array(img1)
img1 = img1/255
img2 = si.load_img(X_test[idx2])
img2 = np.array(img2)
img2 = img2/255

X1[0][0,:,:,:]=img1
X1[1][0,:,:,:]=img2

#Different pair.
idx1,idx2 = si.different_label_index(X_test)
X2=[np.zeros((1,150,150,3)) for i in range(2)]

img1 = si.load_img(X_test[idx1])
img1 = np.array(img1)
img1 = img1/255
img2 = si.load_img(X_test[idx2])
img2 = np.array(img2)
img2 = img2/255


X2[0][0,:,:,:]=img1
X2[1][0,:,:,:]=img2

model=load_model('./SpeakerID_best.hdf5')
print(model.predict(X1))
print(model.predict(X2))
