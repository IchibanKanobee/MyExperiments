import tensorflow as tf
import numpy as np


np_a = np.array([["/raid/data/ShapeNet/ShapeNetCore.v2_simplified_black_on_white_no_depth/airplane,aeroplane,plane/train/1a9b552befd6306cc8f2d5fe7449af61/img-00-00.png","/raid/data/ShapeNet/ShapeNetCore.v2_simplified_black_on_white_no_depth/airplane,aeroplane,plane/train/1a9b552befd6306cc8f2d5fe7449af61/img-00-01.png"], ["/raid/data/ShapeNet/ShapeNetCore.v2_simplified_black_on_white_no_depth/airplane,aeroplane,plane/train/1a32f10b20170883663e90eaf6b4ca52/img-00-00.png","/raid/data/ShapeNet/ShapeNetCore.v2_simplified_black_on_white_no_depth/airplane,aeroplane,plane/train/1a32f10b20170883663e90eaf6b4ca52/img-00-01.png"]])
np_b = np.array([[1,2], [3,4]])

dataset = tf.data.Dataset.from_tensor_slices((np_a, np_b))
print(dataset)


it = iter(dataset)
n = next(it)
print(n[0].numpy(), n[1].numpy())
n = next(it)
print(n[0].numpy(), n[1].numpy())
