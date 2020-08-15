import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import cv2

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
  
def finding_files_in_directory(ele_list, path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.flac' in file:
                files.append(os.path.join(r, file))
    for f in files:
        ele_list.append(f)
        
    return ele_list

def storing_img_data(ele_list):
    for filepath in ele_list:
      filename=filepath.split('/')[-1].split('.')[0]
      filename = filename.split('\\')[-1]
      create_spectrogram(filepath,'./content/train_images/'+filename+'.jpg')

#Building the batch generator.
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
