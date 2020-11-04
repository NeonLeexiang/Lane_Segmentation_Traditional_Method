"""
    date:       2020/11/3 7:31 下午
    written by: neonleexiang
"""
import random
import numpy as np
import os
import shutil

img_dir_name = 'original_data/traffic_marking/'
label_dir_name = 'original_data/traffic_marking_labels/'

name_list = os.listdir(img_dir_name)

for i in range(len(name_list)):
    name_list[i] = name_list[i].replace('.jpg', '')

print('-------------------------------')
print(name_list)


def get_random_index(n, x):
    # index range [0, n), choice x
    index = random.sample(range(n), x)
    return index


def get_random_index_numpy(n, x):
    index = np.random.choice(np.arange(n), size=x, replace=False)
    return index


# we choose our test_index and random_index
list_size = len(name_list)
test_size = int(list_size * 0.3)

test_index = np.array(get_random_index(list_size, test_size))
train_index = np.delete(np.arange(list_size), test_index)

training_data_name = []
testing_data_name = []

for c in test_index:
    testing_data_name.append(name_list[c])

for c in train_index:
    training_data_name.append(name_list[c])

print('-------------------------------')

print('testing data: --------')
print(testing_data_name)

print('training data:--------')
print(training_data_name)

print('----------------------')

print(len(name_list))
print(len(training_data_name), len(testing_data_name), len(training_data_name) + len(testing_data_name))

print('----------------------')

training_data_img_new_dir = 'datasets/training_data/marking/'
training_data_label_new_dir = 'datasets/training_data/label/'

testing_data_img_new_dir = 'datasets/testing_data/marking/'
testing_data_label_new_dir = 'datasets/testing_data/label/'

for n in training_data_name:
    shutil.copy(os.path.join(img_dir_name, n + '.jpg'), training_data_img_new_dir)
    shutil.copy(os.path.join(label_dir_name, n + '.xml'), training_data_label_new_dir)
    print('copying ---', n, 'successfully')

for n in testing_data_name:
    shutil.copy(os.path.join(img_dir_name, n + '.jpg'), testing_data_img_new_dir)
    shutil.copy(os.path.join(label_dir_name, n + '.xml'), testing_data_label_new_dir)
    print('copying ---', n, 'successfully')







