import numpy as np
from os import listdir
from os.path import isfile, join, isdir, splitext
#import re
from scipy import misc
from random import randrange


def get_tinkercad_dataset(root_dir):
    dataset = []
    onlydirs = [f for f in listdir(root_dir) if isdir(join(root_dir, f))]
    for dir in onlydirs:
        path = join(root_dir, dir)
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        r = re.compile(".*00.png")
        re_files = list(filter(r.match, onlyfiles))
        count = len(re_files)
        for i in range(count):
            re_files[i] = join(path, re_files[i])
        dataset.append(np.array(re_files))
    dataset = np.array(dataset)
    count = dataset.shape[0]
    training_count = int(0.5 * count)
    testing_count = int(0.2 * count)

    training_dataset = dataset[:training_count]
    testing_dataset = dataset[training_count : training_count + testing_count]
    validation_dataset= dataset[training_count + testing_count:]
    return training_dataset, testing_dataset, validation_dataset



def get_shapenet_dataset(root_dir):
    dataset = []
    onlydirs = [f for f in listdir(root_dir) if isdir(join(root_dir, f))]
    for dir in onlydirs:
        path = join(root_dir, dir)
        onlydirs2 = [f for f in listdir(path) if isdir(join(path, f))]
        for dir2 in onlydirs2:
            path2 = join(path, dir2)
            onlyfiles = [f for f in listdir(path2) if isfile(join(path2, f))]
            count = len(onlyfiles)
            for i in range(count):
                ext = splitext(onlyfiles[i])[1]
                if (ext == '.png'):
                    onlyfiles[i] = join(path2, onlyfiles[i])
            dataset.append(np.array(onlyfiles))
    dataset = np.array(dataset)
    np.random.shuffle(dataset)
    count = dataset.shape[0]
    training_count = int(0.5 * count)
    testing_count = int(0.2 * count)

    training_dataset = dataset[:training_count]
    testing_dataset = dataset[training_count : training_count + testing_count]
    validation_dataset= dataset[training_count + testing_count:]

    np.savetxt("Training_dataset.txt", training_dataset, fmt="%s")
    np.savetxt("Testing_dataset.txt", testing_dataset, fmt="%s")
    np.savetxt("Validation_dataset.txt", validation_dataset, fmt="%s")

    return training_dataset, testing_dataset, validation_dataset


def get_slicenet_lists_for_one_class(root_dir, class_name):
    image_paths = []
    slices_paths = []
    path = join(root_dir, class_name)

    models = [f for f in listdir(path) if isdir(join(path, f))]

    for model in models:
        model_path = join(path, model)
        multi_path = join(model_path, "white_bknd_multiview")
        image_path = join(multi_path, "img-18-00.png")
        if not isfile(image_path):
            continue
        slices_path = join(model_path, "slices")
        if not isdir(slices_path):
            continue
        slice_files = [f for f in listdir(slices_path) if isfile(join(slices_path, f))]
        count = len(slice_files)
        for i in range (count):
            slice_files[i] = join(slices_path, slice_files[i])
        image_paths.append(image_path)
        slices_paths.append(slice_files)


    count = len(models)
    validation_count = int (0.2 * count)
    test_count = int(0.3 * count)
    train_count = count - validation_count - test_count

    train_image_dataset = image_paths[:train_count]
    test_image_dataset = image_paths[train_count:train_count+test_count]
    validation_image_dataset = image_paths[train_count+test_count:train_count+test_count+ validation_count]

    train_slices_dataset = slices_paths[:train_count]
    test_slices_dataset = slices_paths[train_count:train_count+test_count]
    validation_slices_dataset = slices_paths[train_count+test_count:train_count+test_count+ validation_count]

    return train_image_dataset, test_image_dataset, validation_image_dataset, train_slices_dataset, test_slices_dataset, validation_slices_dataset


def get_slicenet_dataset(root_dir):
    train_image_dataset = []
    test_image_dataset = []
    val_image_dataset = []
    train_slices_dataset = []
    test_slices_dataset = []
    val_slices_dataset= []

    onlydirs = [f for f in listdir(root_dir) if isdir(join(root_dir, f))]

    for dir in onlydirs:
        class_train_image_dataset, class_test_image_dataset, class_validation_image_dataset, class_train_slices_dataset, class_test_slices_dataset, class_validation_slices_dataset = get_slicenet_lists_for_one_class(root_dir, dir)
        train_image_dataset.extend(class_train_image_dataset)
        test_image_dataset.extend(class_test_image_dataset)
        val_image_dataset.extend(class_validation_image_dataset)

        train_slices_dataset.extend(class_train_slices_dataset)
        test_slices_dataset.extend(class_test_slices_dataset)
        val_slices_dataset.extend(class_validation_slices_dataset)

        #break #temp break to shorten process

    training_image_dataset = np.array(train_image_dataset)
#    np.random.shuffle(training_image_dataset)

    testing_image_dataset = np.array(test_image_dataset)
#    np.random.shuffle(testing_image_dataset)

    validation_image_dataset = np.array(val_image_dataset)
#    np.random.shuffle(validation_dataset)

    training_slices_dataset = np.array(train_slices_dataset)
    #    np.random.shuffle(training_image_dataset)

    testing_slices_dataset = np.array(test_slices_dataset)
    #    np.random.shuffle(testing_image_dataset)

    validation_slices_dataset = np.array(val_slices_dataset)
    #    np.random.shuffle(validation_dataset)

    return training_image_dataset, testing_image_dataset, validation_image_dataset, training_slices_dataset, testing_slices_dataset, validation_slices_dataset

#    np.savetxt("modelnet40_training_dataset.txt", training_dataset, fmt="%s")
#    np.savetxt("modelnet40_testing__dataset.txt", testing_dataset, fmt="%s")
#    np.savetxt("modelnet40_validation_dataset.txt", validation_dataset, fmt="%s")

#    return training_dataset, testing_dataset, validation_dataset



def get_next_input_batch_fixed_slice_count(image_dataset, slice_dataset, index, batch_size, max_slice_count, input_image_size, slice_image_size, index_order):
    image_batch = []
    slice_batch = []
    slice_index_batch = []
    indices = index_order[index:index+batch_size]
    part_image_dataset = np.array(image_dataset)[indices]
    part_slice_dataset = np.array(slice_dataset[indices])

#    pair = utils.get_random_pair_of_views(6)
#    pair = utils.get_random_pair_of_views(view_count)
#    pair = (0, 18)

    for i in range (batch_size):
        input_image_path = part_image_dataset[i]
        input_slices = part_slice_dataset[i]
        slice_count = len(input_slices)
        slice_index = randrange(max_slice_count)

        input_image  = misc.imread(input_image_path, flatten=True)
        shape = input_image.shape
        if (shape != input_image_size):
            input_image  = misc.imresize(input_image, image_size)

        if (slice_index >= slice_count):
            slice_image = np.zeros((slice_image_size[0], slice_image_size[1]))
        else:
            slice_image  = misc.imread(input_slices[slice_index], flatten=True)
            shape = slice_image.shape
            if (shape != slice_image_size):
                slice_image  = misc.imresize(slice_image, slice_image_size)

        image_batch.append(input_image)
        slice_batch.append(slice_image)
        slice_index_batch.append(slice_index)

    np_image_batch = np.array(image_batch)
    np_image_batch = np_image_batch[..., np.newaxis]
    np_slice_batch = np.array(slice_batch)
    np_slice_batch = np_slice_batch[..., np.newaxis]
    np_slice_index_batch = np.array(slice_index_batch)
    np_slice_index_batch = np_slice_index_batch[..., np.newaxis]
    return np_image_batch, np_slice_batch, np_slice_index_batch



def get_next_input_batch_variable_slice_count(image_dataset, slice_dataset, index, batch_size, input_image_size, slice_image_size, index_order):
    image_batch = []
    slice_batch = []
    slice_index_batch = []
    indices = index_order[index:index+batch_size]
    part_image_dataset = np.array(image_dataset)[indices]
    part_slice_dataset = np.array(slice_dataset[indices])

    for i in range (batch_size):
        input_image_path = part_image_dataset[i]
        input_slices = part_slice_dataset[i]
        slice_count = len(input_slices)
        slice_index = randrange(slice_count)

        input_image  = misc.imread(input_image_path, flatten=True)
        slice_image  = misc.imread(input_slices[slice_index], flatten=True)
        shape = input_image.shape
        if (shape != input_image_size):
            input_image  = misc.imresize(input_image, image_size)

        shape = slice_image.shape
        if (shape != slice_image_size):
            slice_image  = misc.imresize(slice_image, slice_image_size)

        image_batch.append(input_image)
        slice_batch.append(slice_image)
        slice_index_batch.append(slice_index)

    np_image_batch = np.array(image_batch)
    np_image_batch = np_image_batch[..., np.newaxis]
    np_slice_batch = np.array(slice_batch)
    np_slice_batch = np_slice_batch[..., np.newaxis]
    np_slice_index_batch = np.array(slice_index_batch)
    np_slice_index_batch = np_slice_index_batch[..., np.newaxis]
    return np_image_batch, np_slice_batch, np_slice_index_batch


