import tensorflow as tf
import pathlib

flowers_root = tf.keras.utils.get_file(
    'flower_photos',
    'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
    untar=True)

print(flowers_root)
#/home/ara/.keras/datasets/flower_photos - str

flowers_root_pl = pathlib.Path(flowers_root)
print(flowers_root_pl) #posix path

for item in flowers_root_pl.glob("*"):
  print(item.name)

list_ds = tf.data.Dataset.list_files(str(flowers_root_pl/'*/*')) #DatasetV1Adapter

for f in list_ds.take(5):
  print(f.numpy())

#for f in list_ds:
#  print(f.numpy())

def process_path(file_path):
  print (file_path)
  parts = tf.strings.split(file_path, '/')
  print(parts)
  return tf.io.read_file(file_path), parts[-2]

labeled_ds = list_ds.map(process_path)
print (labeled_ds)

for image_raw, label_text in labeled_ds.take(1):
  print(repr(image_raw.numpy()[:100]))
  print()
  print(label_text.numpy())
