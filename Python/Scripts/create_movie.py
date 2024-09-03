import os, shutil
import subprocess
import Image


BASE_PATH = '/raid/train_log/vae_mvcnn/m40_256/samples/presentation/'
MOVIE_PATH = BASE_PATH + "movie/"

if os.path.exists(MOVIE_PATH):
    shutil.rmtree(MOVIE_PATH)
os.makedirs(MOVIE_PATH)

step_count = 600
copied_index = 39

size = 256
rows = 10
cols = 8
gap = 32


def tile_images(dir, index, size, rows, cols):
    #tile 80 images from the dir into 1 10x8 image
    tiled_image = Image.new("L", ((size + gap) * rows + gap, (size + gap) * cols + gap), '#ffffff')

    for i in range (0, rows):
        for j in range (0, cols):
            img = Image.open(dir + 'image_{:04d}.png'.format(i * cols + j))
            tiled_image.paste(img, ((size + gap) * i + gap, (size + gap) * j + gap))

    tiled_image.save(dir + "tiled_{:d}.png".format(index))


#Copy source files into movie folder
for i in range (step_count):
    tile_images(BASE_PATH + 'output/object_{:04d}/'.format(i), i, size, rows, cols)
    src = BASE_PATH + 'output/object_{:04d}/'.format(i) + 'image_{:04d}.png'.format(copied_index)
    dst = MOVIE_PATH + 'object_{:d}.png'.format(i)
    shutil.copyfile(src, dst)


#Create the movie with ffmpeg
os.chdir(MOVIE_PATH)
subprocess.call(['ffmpeg', '-i', 'object_%d.png', '-r', '10', 'output.avi'])
