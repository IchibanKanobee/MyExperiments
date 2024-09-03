from data_io import data_input
import time
import numpy as np
import tensorflow as tf
from tensorflow.contrib.slim import fully_connected as fc
import random


def trainer(model_object, train_image_dataset, validation_image_dataset, train_slices_dataset, validation_slices_dataset, image_width, image_height, slice_width, slice_height, channels, learning_rate, batch_size, max_slice_count, model_path, num_epoch=100, n_z=1024, log_step=5):
    model = model_object(image_width, image_height, channels, model_path,
        learning_rate=learning_rate, batch_size=batch_size, training=True, n_z=n_z)

    train_writer = tf.summary.FileWriter('training_summary/autoencoder')
    valid_writer = tf.summary.FileWriter('validation_summary/autoencoder')

    train_count = train_image_dataset.shape[0]
    validation_count = validation_image_dataset.shape[0]

    train_index_order = list(range(train_count))
    random.shuffle(train_index_order)

    validation_index_order = list(range(validation_count))
    random.shuffle(validation_index_order)

    for epoch in range(num_epoch):
        start_time = time.time()
        count = train_count // batch_size

        for iter in range(count):
            # Get a batch
            np_image_batch, np_slice_batch, np_slice_index_batch = data_input.get_next_input_batch_fixed_slice_count(
                train_image_dataset, train_slices_dataset, iter, batch_size, max_slice_count, (image_width, image_height), (slice_width, slice_height), train_index_order)
            x_hat, losses, grads, summary = model.run_single_step(np_image_batch)
            print("Loss for iteration " + str(iter) + " out of " + str(count) + " is " + str(losses))
            train_writer.add_summary(summary, iter)
            train_writer.flush()

        val_count = validation_count // batch_size
        for iter in range(val_count):
            # Get a batch
            np_image_batch, np_slice_batch, np_slice_index_batch = data_input.get_next_input_batch_fixed_slice_count(
                validation_image_dataset, validation_slices_dataset, iter, batch_size, max_slice_count, (image_width, image_height), (slice_width, slice_height), validation_index_order)
            z, x_hat, losses, summary = model.run_single_test_step(np_image_batch)
            print("Validation loss for iteration " + str(iter) + " out of " + str(val_count) + " is " + str(losses))
            valid_writer.add_summary(summary, iter)
            valid_writer.flush()

        model.save_model(epoch)

        end_time = time.time()

 #       if epoch % log_step == 0:
        if True:
            log_str = '[Epoch {}] '.format(epoch)
            for k, v in losses.items():
                log_str += '{}: {:.3f}  '.format(k, v)
            log_str += '({:.3f} sec/epoch)'.format(end_time - start_time)
            print(log_str)

    print('Done!')
    return model


class Autoencoder(object):

    def __init__(self, width, height, channels, model_path, learning_rate, batch_size, training, n_z=1024):
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.n_z = n_z
        self.training = training
        self.model_path = model_path

 #       tf.reset_default_graph()
        self.build(width, height, channels)

#      My aux variables
#        self.latent_loss_exp = 0

#        self.sess = tf.InteractiveSession()
        self.saver = tf.train.Saver()
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    # Build the netowrk and the loss functions
    def build(self, width, height, channels):
        self.x = tf.placeholder(
            name='x', dtype=tf.float32, shape=[None, width, height, channels])
#            name = 'x', dtype = tf.float32, shape = [BATCH_SIZE, view_count, width, height, channels])

        # Encode
        # x -> z_mean, z_sigma -> z
        reshaped = tf.reshape(self.x, [-1, width, height, channels])
        tf.summary.image('input', reshaped)

        conv1 = tf.layers.conv2d(reshaped, filters=128, kernel_size=[5, 5], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), bias_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="conv1")

        conv2 = tf.layers.conv2d(conv1, filters=256, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), bias_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="conv2")

        conv3 = tf.layers.conv2d(conv2, filters=256, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), bias_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="conv3")

        conv4 = tf.layers.conv2d(conv3, filters=512, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), bias_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="conv4")

        conv5 = tf.layers.conv2d(conv4, filters=256, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), bias_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="conv5")

        conv5_shape = conv5.shape
        conv5_reshaped = tf.reshape(conv5, [-1, conv5_shape[1] * conv5_shape[2] * conv5_shape[3]])


        self.z = tf.layers.dense(conv5_reshaped, self.n_z)

        drop = tf.layers.dropout(self.z)

        # Decode
        # z -> x_hat

        dense_back = tf.layers.dense(drop, conv5_shape[1] * conv5_shape[2] * conv5_shape[3])
        deconv_back = tf.reshape(dense_back, [-1, conv5_shape[1], conv5_shape[2], conv5_shape[3]])

        deconv5 = tf.layers.conv2d_transpose(deconv_back, filters=256, kernel_size=[3, 3], kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), strides=(1, 1), padding = "same", activation = tf.nn.relu, name="deconv5")

        deconv4 = tf.layers.conv2d_transpose(deconv5, filters=512, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="deconv4")

        deconv3 = tf.layers.conv2d_transpose(deconv4, filters=256, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="deconv3")

        deconv2 = tf.layers.conv2d_transpose(deconv3, filters=256, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="deconv2")

        deconv1 = tf.layers.conv2d_transpose(deconv2, filters=128, kernel_size=[3, 3], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="deconv1")

        deconv = tf.layers.conv2d_transpose(deconv1, filters=1, kernel_size=[5, 5], strides=(2, 2), kernel_initializer=tf.contrib.layers.xavier_initializer(uniform=False), padding = "same", activation = tf.nn.relu, name="deconv")

        tf.summary.image('output', deconv)

        self.x_hat = tf.reshape(deconv, [-1, width, height, channels])
        # Loss
        # Reconstruction loss
        # Minimize the cross-entropy loss
        # H(x, x_hat) = -\Sigma x*log(x_hat) + (1-x)*log(1-x_hat)

#        recon_loss = -tf.reduce_sum(
#            self.x * tf.log(epsilon+self.x_hat) +
#            (1-self.x) * tf.log(epsilon+1-self.x_hat),
#            axis=1
#        )
        recon_loss = tf.square(self.x - self.x_hat)
        recon_loss = tf.reduce_mean(recon_loss)

        self.recon_loss = tf.sqrt(recon_loss)


        self.total_loss = self.recon_loss
        tf.summary.scalar('loss', self.total_loss)

        optimizer = tf.train.AdamOptimizer(
            learning_rate=self.learning_rate)

        self.grads = optimizer.compute_gradients(self.total_loss)
        tf.summary.merge([tf.summary.histogram("%s-grad" % g[1].name, g[0]) for g in self.grads])

        self.train_op = optimizer.minimize(self.total_loss)
        
        self.losses = {
            'total_loss': self.total_loss,
        }

        self.merged = tf.summary.merge_all()
        return

    # Execute the forward and the backward pass
    def run_single_step(self, x):
        _, z, x_hat, losses, grads, summary = self.sess.run(
            [self.train_op, self.z, self.x_hat, self.losses, self.grads, self.merged],
            feed_dict={self.x: x})
        return x_hat, losses, grads, summary


    def run_single_test_step(self, x):
        z, x_hat, losses, summary = self.sess.run(
            [self.z, self.x_hat, self.losses, self.merged],
            feed_dict={self.x: x})
        return z, x_hat, losses, summary


    # x -> x_hat
    def reconstructor(self, x):
        x_hat = self.sess.run(self.x_hat, feed_dict={self.x: x})
        return x_hat

    # z -> x
    def generator(self, z):
        x_hat = self.sess.run(self.x_hat, feed_dict={self.z: z})
        return x_hat
    
    # x -> z
    def transformer(self, x):
        z = self.sess.run(self.z, feed_dict={self.x: x})
        return z

    def save_model(self, epoch):
        self.saver.save(self.sess, self.model_path + str(epoch) + ".ckpt")







