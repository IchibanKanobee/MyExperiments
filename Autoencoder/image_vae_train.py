import numpy as np
from data_io import data_input
from networks import vae_images
import random


DATA_DIR = "/raid/data/ShapeNet/Slices"
#DATA_DIR = "/raid/data/ShapeNet/Slices_small"
BATCH_SIZE = 4
CHANNELS = 1
LEARNING_RATE = 1e-4
MODEL_PATH = 'saved_model/slicenet_image_vae_256x256/model_'
IMAGE_SIZE = (256, 256)
MAX_SLICE_COUNT = 1024
SLICE_SIZE = (1024, 1024)

CHECKPOINT = 0


train_image_dataset, test_image_dataset, validation_image_dataset, train_slices_dataset, test_slices_dataset, validation_slices_dataset = data_input.get_slicenet_dataset(DATA_DIR)

# Train a model
model = vae_images.trainer(vae_images.VAE, train_image_dataset, validation_image_dataset, train_slices_dataset, validation_slices_dataset, IMAGE_SIZE[0], IMAGE_SIZE[1], SLICE_SIZE[0], SLICE_SIZE[1], CHANNELS, LEARNING_RATE, BATCH_SIZE, MAX_SLICE_COUNT, MODEL_PATH)




