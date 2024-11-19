import numpy as np

def get_norm_quat_image(img, quat):
    norm_quat = quat / np.linalg.norm(quat)
    quat_shape = quat.shape
    img_shape = img.shape
    quat_image = np.zeros((img_shape[0], img_shape[1], quat_shape[0]))
    for i in range(img_shape[0]):
        for j in range (img_shape[1]):
            for k in range (quat_shape[0]):
                quat_image[i][j][k] = img[i][j] * norm_quat[k]
    return quat_image

img = np.array([[1.0, 1.0], [2.0, 2.0]])
print img.shape
quat = np.array([1.0, 1.0, 1.0, 1.0])
print quat.shape

quat_img = get_norm_quat_image(img, quat)
print quat_img.shape
print quat_img
