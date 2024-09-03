#http://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python


from PIL import Image
from os import listdir
from os.path import isfile, isdir, join


def get_images(root, folders, index):
    img = []
    count = len(folders)
    for i in range(count):
        folder_path = join(root, folders[i])
        files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        path = join(folder_path, files[index])
        img.append(path)
    return img


BORDER_WIDTH = 5
BORDER_HEIGHT = 5

COLUMN_COUNT = 10
ROW_COUNT = 9

ROOT_DIR = '/media/ara/HDD/TechSummitImages/vae_shapeNet_yaw_changing_100_views'

images = []


#Images from different folders but same name
folders = [f for f in listdir(ROOT_DIR) if isdir(join(ROOT_DIR, f))]


folder0 = join(ROOT_DIR, folders[0])
files = [f for f in listdir(folder0) if isfile(join(folder0, f))]
count = len(files)

file0 = join(folder0, files[0])

img = Image.open(file0)
img_width, img_height = img.size

canvas_width = COLUMN_COUNT * (img_width + BORDER_WIDTH) + BORDER_WIDTH
canvas_height = ROW_COUNT * (img_height + BORDER_HEIGHT) + BORDER_HEIGHT

for k in range(count):
    background = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))
    images = get_images(ROOT_DIR, folders, k)

    for i in range(ROW_COUNT):
        for j in range (COLUMN_COUNT):
            img = Image.open(images[i * COLUMN_COUNT + j])

            offset = ((img_width + BORDER_WIDTH) * j + BORDER_WIDTH, (img_height + BORDER_HEIGHT) * i + BORDER_HEIGHT)

            background.paste(img, offset)

    background.save("Movies/out_" + str(k) + ".png")

