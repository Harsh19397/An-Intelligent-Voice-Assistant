import random
import numpy as np
from Deep_Speaker.constant import SAMPLE_RATE, NUM_FRAMES
from Deep_Speaker.audio import read_mfcc
from Deep_Speaker.batcher import sample_from_mfcc
from Deep_Speaker.conv_models import DeepSpeakerModel
from Deep_Speaker.test_speaker import batch_cosine_similarity

# Reproducible results.
np.random.seed(123)
random.seed(123)

# Define the model here.
model = DeepSpeakerModel()

# Load the checkpoint.
model.m.load_weights('ResCNN_triplet_training_checkpoint_265.h5', by_name=True)

def get_speaker_identity(User_name):
    
    # Sample some inputs for WAV/FLAC files for the same speaker.
    # To have reproducible results every time you call this function, set the seed every time before calling it.
    # np.random.seed(123)
    # random.seed(123)
    filename = "recorded_"+User_name+".wav"
    validation_name = "recorded_validation_audio.wav"
    mfcc_001 = sample_from_mfcc(read_mfcc(filename, SAMPLE_RATE), NUM_FRAMES)
    mfcc_002 = sample_from_mfcc(read_mfcc(validation_name, SAMPLE_RATE), NUM_FRAMES)
    
    # Call the model to get the embeddings of shape (1, 512) for each file.
    predict_001 = model.m.predict(np.expand_dims(mfcc_001, axis=0))
    predict_002 = model.m.predict(np.expand_dims(mfcc_002, axis=0))
    
    # Compute the cosine similarity and check that it is higher for the same speaker.
    print('Similarity Index:', batch_cosine_similarity(predict_001, predict_002))
    
    if batch_cosine_similarity(predict_001, predict_002) > 0.72:
        return True
    else:
        return False