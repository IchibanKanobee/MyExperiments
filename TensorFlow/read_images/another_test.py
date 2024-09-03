#https://stackoverflow.com/questions/43567552/tf-slice-input-producer-not-keeping-tensors-in-sync

import tensorflow as tf

truth_filenames_np = ['dir/%d.jpg' % j for j in range(66)]
truth_filenames_tf = tf.convert_to_tensor(truth_filenames_np)
# get the labels
labels = [f.rsplit("/", 1)[1] for f in truth_filenames_np]
labels_tf = tf.convert_to_tensor(labels)

# My list is also already shuffled, so I set shuffle=False
truth_image_name, truth_label = tf.train.slice_input_producer(
    [truth_filenames_tf, labels_tf], shuffle=False)

# # Another key step, where I batch them together
# truth_images_batch, truth_label_batch = tf.train.batch(
#     [truth_image_name, truth_label], batch_size=11)

epochs = 7

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    for i in range(epochs):
        print("Epoch ", i)
        X_truth_batch = truth_image_name.eval()
        X_label_batch = truth_label.eval()
        # Here I display all the images in this batch, and then I check
        # which file numbers they actually are.
        # BUT, the images that are displayed don't correspond with what is
        # printed by X_label_batch!
        print(X_truth_batch)
        print(X_label_batch)
    coord.request_stop()
    coord.join(threads)

