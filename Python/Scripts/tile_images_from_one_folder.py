#http://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python


from PIL import Image
from os import listdir
from os.path import isfile, join, isdir



BORDER_WIDTH = 5
BORDER_HEIGHT = 5

COLUMN_COUNT = 10
ROW_COUNT = 2

ROOT_DIR = '/home/ara/stool_20/'

images = []

#Assuming images were split by our utility assigning names IMG-%d.png

#Images from the same folder

files = [f for f in listdir(ROOT_DIR) if isfile(join(ROOT_DIR, f))]
count = len(files)

for i in range (count):
    images.append("IMG-" + str(i) + ".png")


#Images from different folders but same name
folders = [f for f in listdir(ROOT_DIR) if isdir(join(ROOT_DIR, f))]
count = len(folders)

print images


img = Image.open(join(ROOT_DIR, images[0]))

img_width, img_height = img.size

canvas_width = COLUMN_COUNT * (img_width + BORDER_WIDTH) + BORDER_WIDTH
canvas_height = ROW_COUNT * (img_height + BORDER_HEIGHT) + BORDER_HEIGHT


background = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))

for i in range(ROW_COUNT):
    for j in range (COLUMN_COUNT):
        img = Image.open(join(ROOT_DIR, images[i * COLUMN_COUNT + j]))

        offset = ((img_width + BORDER_WIDTH) * j + BORDER_WIDTH, (img_height + BORDER_HEIGHT) * i + BORDER_HEIGHT)

        print offset
        background.paste(img, offset)

background.save('Images/out.png')

