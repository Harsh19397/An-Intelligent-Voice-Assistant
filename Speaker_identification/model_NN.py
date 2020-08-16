from keras.layers import Lambda,Input
import keras.backend as K
from keras.models import Sequential,Model
from keras.layers import Conv2D,MaxPool2D,Dense,GlobalMaxPool2D,Dropout

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
